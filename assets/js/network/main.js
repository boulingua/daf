/* Materials Discovery Network — Phase 3 entry module.
 *
 * Fetches /network/graph.json, mounts a Cytoscape force-directed graph
 * onto a `#network-mount` element, and re-paints when the user toggles
 * the Coder colour scheme. Filtering, search, and list↔graph sync are
 * Phases 4 and 5; this module only exposes a tiny `applyFilter` hook
 * those phases will consume.
 *
 * Library choice — Cytoscape.js with the fcose layout. Justification:
 *   • Handles 200–2000 nodes smoothly.
 *   • First-class CSS-style stylesheet model — we read CSS custom
 *     properties at render time so the dark/light swap is one
 *     `cy.style(...).update()` call.
 *   • Mature plugin ecosystem (fcose for clustered layouts) and
 *     keyboard-navigation extensions (added in Phase 6 for a11y).
 *   • Smaller / better maintained than D3-force for this exact
 *     non-temporal graph; sigma is faster but harder to style;
 *     vis-network has too opinionated a default.
 *
 * Loading model — Cytoscape ships from a CDN as ESM via
 * <link rel="modulepreload">; this module imports it by URL.
 * esbuild marks the URL specifier as external (Hugo `js.Build` with
 * `externals`) so the bundle stays small and the browser fetches
 * Cytoscape in parallel with the page.
 */

import cytoscape from 'https://esm.sh/cytoscape@3.30.2';
import fcose from 'https://esm.sh/cytoscape-fcose@2.2.0';

cytoscape.use(fcose);

const TYPE_SHAPE = {
  article: 'ellipse',
  presentation: 'rectangle',
  worksheet: 'diamond',
};

function readVar(name, fallback) {
  const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  return v || fallback;
}

function topicColor(topic) {
  return readVar(`--network-topic-${topic}`, '#888');
}

function buildStylesheet() {
  const fg = readVar('--fg-color', '#222');
  const highlight = readVar('--network-highlight', '#E8C547');
  return [
    {
      selector: 'node',
      style: {
        'background-color': (n) => topicColor(n.data('topic')),
        'shape': (n) => TYPE_SHAPE[n.data('type')] || 'ellipse',
        'width': (n) => (n.data('type') === 'article' ? 22 : 14),
        'height': (n) => (n.data('type') === 'article' ? 22 : 14),
        'border-width': 0,
        'opacity': 0.95,
        'label': '',
      },
    },
    {
      selector: 'node:hover, node.is-hovered',
      style: {
        'border-width': 2,
        'border-color': highlight,
        'label': (n) => n.data('title'),
        'font-size': 11,
        'color': fg,
        'text-background-color': readVar('--network-surface', '#fff'),
        'text-background-opacity': 0.9,
        'text-background-padding': 4,
        'text-background-shape': 'roundrectangle',
        'text-margin-y': -8,
      },
    },
    {
      selector: 'node.is-dimmed',
      style: { 'opacity': 0.12 },
    },
    {
      selector: 'edge',
      style: {
        'curve-style': 'bezier',
        'width': (e) => Math.max(0.5, e.data('weight') * 0.5),
        'opacity': 0.35,
      },
    },
    {
      selector: 'edge[kind = "same-article"]',
      style: { 'line-color': fg, 'opacity': 0.3 },
    },
    {
      selector: 'edge[kind = "shared-tags"]',
      style: {
        'line-color': (e) => topicColor(e.source().data('topic')),
        'opacity': 0.18,
      },
    },
    {
      selector: 'edge.is-dimmed',
      style: { 'opacity': 0.04 },
    },
  ];
}

const FCOSE_OPTS = {
  name: 'fcose',
  quality: 'default',
  randomize: true,
  animate: false,
  fit: true,
  padding: 30,
  nodeSeparation: 65,
  idealEdgeLength: 60,
  nodeRepulsion: 4500,
  gravity: 0.15,
};

export async function init(mountEl) {
  if (!mountEl) return null;
  const url = mountEl.dataset.graphUrl || '/network/graph.json';

  let data;
  try {
    const r = await fetch(url, { credentials: 'omit' });
    if (!r.ok) throw new Error(`graph.json HTTP ${r.status}`);
    data = await r.json();
  } catch (err) {
    mountEl.innerHTML = `<div class="graph-legend" role="alert">Graph konnte nicht geladen werden: ${err.message}</div>`;
    return null;
  }

  const cy = cytoscape({
    container: mountEl,
    elements: [
      ...data.nodes.map((n) => ({ data: n, group: 'nodes' })),
      ...data.edges.map((e) => ({ data: e, group: 'edges' })),
    ],
    style: buildStylesheet(),
    layout: FCOSE_OPTS,
    minZoom: 0.15,
    maxZoom: 4,
    wheelSensitivity: 0.2,
    pixelRatio: 'auto',
  });

  // Click an article = navigate; click a presentation/worksheet = download.
  cy.on('tap', 'node', (evt) => {
    const n = evt.target;
    const url = n.data('url');
    if (!url) return;
    const type = n.data('type');
    if (type === 'article') {
      window.location.href = url;
    } else {
      const a = document.createElement('a');
      a.href = url;
      a.download = '';
      document.body.appendChild(a);
      a.click();
      a.remove();
    }
  });

  // Light/dark theme swap — restyle on body.class change (Coder swaps
  // colorscheme-light/dark there).
  const restyle = () => cy.style(buildStylesheet()).update();
  const obs = new MutationObserver(restyle);
  obs.observe(document.body, { attributes: true, attributeFilter: ['class'] });

  // Tiny API the Phase-4 filter rail will consume.
  const api = {
    cy,
    data,
    applyFilter(predicate) {
      cy.batch(() => {
        cy.nodes().forEach((n) => {
          const ok = predicate(n.data());
          n.toggleClass('is-dimmed', !ok);
        });
        cy.edges().forEach((e) => {
          const s = e.source().hasClass('is-dimmed');
          const t = e.target().hasClass('is-dimmed');
          e.toggleClass('is-dimmed', s || t);
        });
      });
    },
    reset() {
      cy.batch(() => cy.elements().removeClass('is-dimmed'));
    },
  };
  window.dafNetwork = api;
  return api;
}

// Auto-init if a mount is on the page.
const mount = document.getElementById('network-mount');
if (mount) {
  init(mount);
}
