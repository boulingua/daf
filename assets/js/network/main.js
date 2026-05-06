/* Materials Discovery Network — entry module.
 *
 * Boots Cytoscape, then exposes a tiny store on window.dafNetwork that
 * filters.js, search.js, and list.js push state into. The store
 * composes a single predicate (filter AND search) and runs one
 * Cytoscape batch per change. Subscribers (the list view) get the
 * resulting visible-node set.
 *
 * Library choice — Cytoscape.js with the fcose layout. (Justification
 * in the Phase-3 commit.)
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
    { selector: 'node.is-dimmed', style: { 'opacity': 0.12 } },
    {
      selector: 'edge',
      style: {
        'curve-style': 'bezier',
        'width': (e) => Math.max(0.5, e.data('weight') * 0.5),
        'opacity': 0.35,
      },
    },
    { selector: 'edge[kind = "same-article"]', style: { 'line-color': fg, 'opacity': 0.3 } },
    {
      selector: 'edge[kind = "shared-tags"]',
      style: {
        'line-color': (e) => topicColor(e.source().data('topic')),
        'opacity': 0.18,
      },
    },
    { selector: 'edge.is-dimmed', style: { 'opacity': 0.04 } },
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

  cy.on('tap', 'node', (evt) => {
    const n = evt.target;
    const u = n.data('url');
    if (!u) return;
    if (n.data('type') === 'article') {
      window.location.href = u;
    } else {
      const a = document.createElement('a');
      a.href = u;
      a.download = '';
      document.body.appendChild(a);
      a.click();
      a.remove();
    }
  });

  // Light/dark theme swap.
  const restyle = () => cy.style(buildStylesheet()).update();
  new MutationObserver(restyle).observe(document.body, {
    attributes: true,
    attributeFilter: ['class'],
  });

  // ── Composed-predicate store ─────────────────────────────────────
  const pred = {
    filter: () => true,
    search: () => true,
  };
  const listeners = new Set();
  let lastVisible = new Set();

  function recompute() {
    const visible = new Set();
    cy.batch(() => {
      cy.nodes().forEach((n) => {
        const ok = pred.filter(n.data()) && pred.search(n.data());
        n.toggleClass('is-dimmed', !ok);
        if (ok) visible.add(n.id());
      });
      cy.edges().forEach((e) => {
        const dim = e.source().hasClass('is-dimmed') || e.target().hasClass('is-dimmed');
        e.toggleClass('is-dimmed', dim);
      });
    });
    lastVisible = visible;
    for (const cb of listeners) cb(visible);
  }

  function highlightNode(id, on) {
    const n = cy.getElementById(id);
    if (n && n.length) n.toggleClass('is-hovered', on);
  }

  const api = {
    cy,
    data,
    setFilterPredicate(fn) { pred.filter = fn || (() => true); recompute(); },
    setSearchPredicate(fn) { pred.search = fn || (() => true); recompute(); },
    reset() {
      pred.filter = () => true;
      pred.search = () => true;
      recompute();
    },
    onChange(cb) { listeners.add(cb); cb(lastVisible); return () => listeners.delete(cb); },
    highlightNode,
    visibleIds: () => lastVisible,
    // Back-compat shims for Phase-3 callers.
    applyFilter(fn) { this.setFilterPredicate(fn); },
  };
  window.dafNetwork = api;
  return api;
}

const mount = document.getElementById('network-mount');
if (mount) {
  init(mount);
}
