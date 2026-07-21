/* Materials Discovery Network — entry module.
 *
 * Boots the Cytoscape graph on desktop (≥768px) only and exposes a
 * tiny store on window.dafNetwork that filters.js, search.js, and
 * list.js push state into. The store composes a single predicate
 * (filter AND search) and notifies subscribers on every change.
 *
 * On mobile the Cytoscape import path is never executed: the store
 * still runs (so filters + search + list keep working) but the graph
 * canvas is hidden and the heavy ESM modules don't ship to the device.
 *
 * Library — Cytoscape.js with the fcose layout. (Justification in the
 * Phase-3 commit.)
 */

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
  quality: 'draft', // fewer refinement passes → far cheaper on the main thread
  randomize: true,
  animate: false,
  fit: true,
  padding: 30,
  nodeSeparation: 65,
  idealEdgeLength: 60,
  nodeRepulsion: 4500,
  gravity: 0.15,
};

async function attachCytoscape(mountEl, data) {
  // Self-hosted, same-origin Cytoscape bundle (fcose already registered
  // in vendor.js). Loaded lazily via dynamic import so the ~400 KB library
  // never touches the render path or a third-party CDN.
  const cytoUrl = mountEl.dataset.cytoUrl;
  const { default: cytoscape } = await import(cytoUrl);

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

  new MutationObserver(() => cy.style(buildStylesheet()).update()).observe(document.body, {
    attributes: true,
    attributeFilter: ['class'],
  });

  // Graph is live — drop the loading skeleton.
  const skel = mountEl.querySelector('.graph-skeleton');
  if (skel) skel.remove();

  return cy;
}

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

  const isDesktop = window.matchMedia('(min-width: 768px)').matches;
  let cy = null;

  // ── Composed-predicate store (always runs, with or without Cytoscape) ──
  const pred = { filter: () => true, search: () => true };
  const listeners = new Set();
  let lastVisible = new Set(data.nodes.map((n) => n.id));

  function recompute() {
    const visible = new Set();
    if (cy) {
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
    } else {
      for (const n of data.nodes) {
        if (pred.filter(n) && pred.search(n)) visible.add(n.id);
      }
    }
    lastVisible = visible;
    for (const cb of listeners) cb(visible);
  }

  function highlightNode(id, on) {
    if (!cy) return;
    const n = cy.getElementById(id);
    if (n && n.length) n.toggleClass('is-hovered', on);
  }

  const api = {
    cy,
    data,
    isDesktop,
    setFilterPredicate(fn) { pred.filter = fn || (() => true); recompute(); },
    setSearchPredicate(fn) { pred.search = fn || (() => true); recompute(); },
    reset() { pred.filter = () => true; pred.search = () => true; recompute(); },
    onChange(cb) { listeners.add(cb); cb(lastVisible); return () => listeners.delete(cb); },
    highlightNode,
    visibleIds: () => lastVisible,
    applyFilter(fn) { this.setFilterPredicate(fn); }, // back-compat
  };
  window.dafNetwork = api;
  recompute();

  // ── Lazy-boot Cytoscape (desktop only) ──
  // The list, filters and search are useful immediately, so they render
  // first. The heavy graph canvas is instantiated — and the ~400 KB
  // same-origin Cytoscape bundle fetched — only once the mount scrolls
  // near the viewport. On mobile the graph never paints at all.
  if (isDesktop) {
    const boot = () =>
      attachCytoscape(mountEl, data)
        .then((c) => { cy = c; api.cy = c; recompute(); })
        .catch((err) => {
          console.warn('[network] Cytoscape failed to load — continuing without graph.', err);
          mountEl.style.display = 'none';
        });
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries, obs) => {
        if (entries.some((e) => e.isIntersecting)) { obs.disconnect(); boot(); }
      }, { rootMargin: '300px' });
      io.observe(mountEl);
    } else {
      boot();
    }
  } else {
    mountEl.style.display = 'none';
  }

  return api;
}

const mount = document.getElementById('network-mount');
if (mount) init(mount);
