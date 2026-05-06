/* Materials Discovery Network — filter rail (Phase 4).
 *
 * Reads facet chips out of the DOM (server-rendered by Hugo from
 * graph.json data so the first paint matches the URL state without a
 * flash). Holds a tiny FilterState; on every change:
 *
 *   1) recomputes the predicate,
 *   2) calls api.applyFilter(predicate) to dim non-matching graph nodes,
 *   3) recomputes per-facet live counts (count = nodes matching every
 *      OTHER active facet, regardless of this facet's selections),
 *   4) writes the URL via history.replaceState so the view is shareable.
 *
 * Facet algebra: within a facet OR, across facets AND. The 'tag' facet
 * matches against the node's tags array.
 *
 * No date facet — the DaF curriculum isn't temporal. (See
 * MATERIALS_NETWORK_PLAN.md §5.3 — "decision d1".)
 */

const KEYS = ['type', 'course', 'topic', 'tag'];

class FilterState {
  constructor() {
    this.s = Object.fromEntries(KEYS.map((k) => [k, new Set()]));
  }
  toggle(k, v) {
    const set = this.s[k];
    if (set.has(v)) set.delete(v);
    else set.add(v);
  }
  clear() {
    for (const k of KEYS) this.s[k].clear();
  }
  has(k, v) {
    return this.s[k].has(v);
  }
  toQS() {
    const p = new URLSearchParams();
    for (const k of KEYS) {
      if (this.s[k].size) p.set(k, [...this.s[k]].sort().join(','));
    }
    return p.toString();
  }
  fromQS(qs) {
    this.clear();
    const p = new URLSearchParams(qs);
    for (const k of KEYS) {
      const v = p.get(k);
      if (v) for (const x of v.split(',').filter(Boolean)) this.s[k].add(x);
    }
  }
  passes(node) {
    return this._matchExcept(node, null);
  }
  passesExcept(node, except) {
    return this._matchExcept(node, except);
  }
  _matchExcept(node, except) {
    for (const k of KEYS) {
      if (k === except) continue;
      const set = this.s[k];
      if (!set.size) continue;
      if (k === 'tag') {
        if (!(node.tags || []).some((t) => set.has(t))) return false;
        continue;
      }
      if (!set.has(node[k])) return false;
    }
    return true;
  }
}

function pluralise(n) {
  return n === 1 ? '1 Eintrag' : `${n} Einträge`;
}

export function init(api, root) {
  if (!api || !root) return;
  const nodes = api.data.nodes;
  const state = new FilterState();
  state.fromQS(window.location.search);

  // Apply pressed-state visuals to chips that match the URL on load.
  const chips = Array.from(root.querySelectorAll('.facet-chip[data-facet]'));
  const syncPressed = () => {
    for (const chip of chips) {
      const k = chip.dataset.facet;
      const v = chip.dataset.value;
      const on = state.has(k, v);
      chip.setAttribute('aria-pressed', on ? 'true' : 'false');
    }
  };

  const countLabel = root.querySelector('[data-count-total]');
  const updateCounts = () => {
    // Cross-facet count: how many nodes match every OTHER active facet
    // and have this chip's value? Lets users see what would happen if
    // they added this chip to the current selection.
    const subsets = Object.fromEntries(
      KEYS.map((k) => [k, nodes.filter((n) => state.passesExcept(n, k))])
    );
    let visible = 0;
    for (const n of nodes) if (state.passes(n)) visible++;

    for (const chip of chips) {
      const k = chip.dataset.facet;
      const v = chip.dataset.value;
      let c = 0;
      const pool = subsets[k];
      if (k === 'tag') {
        for (const n of pool) if ((n.tags || []).includes(v)) c++;
      } else {
        for (const n of pool) if (n[k] === v) c++;
      }
      const el = chip.querySelector('.count');
      if (el) el.textContent = c;
      chip.classList.toggle('is-empty', c === 0);
      // Accessibility: still focusable, but communicated as inert.
      if (c === 0 && !state.has(k, v)) {
        chip.setAttribute('aria-disabled', 'true');
      } else {
        chip.removeAttribute('aria-disabled');
      }
    }
    if (countLabel) {
      countLabel.innerHTML = `<strong>${visible}</strong> ${pluralise(visible)} sichtbar (von ${nodes.length})`;
    }
  };

  const apply = () => {
    api.applyFilter((n) => state.passes(n));
    syncPressed();
    updateCounts();
    const qs = state.toQS();
    const url = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
    history.replaceState(null, '', url);
  };

  for (const chip of chips) {
    chip.addEventListener('click', (e) => {
      e.preventDefault();
      const k = chip.dataset.facet;
      const v = chip.dataset.value;
      // Don't allow toggling on a chip that's already inert AND not
      // currently selected — clicking it would just leave the user
      // with zero results.
      if (chip.getAttribute('aria-disabled') === 'true' && !state.has(k, v)) return;
      state.toggle(k, v);
      apply();
    });
  }

  const reset = root.querySelector('[data-action="reset"]');
  if (reset) {
    reset.addEventListener('click', (e) => {
      e.preventDefault();
      state.clear();
      apply();
    });
  }

  // First paint: apply URL state (if any) before anything else, so the
  // graph already reflects the URL when the layout settles.
  apply();
}

// Auto-init once the graph API exists (it sets window.dafNetwork from
// main.js after fetch + cytoscape boot).
function awaitApi(cb) {
  if (window.dafNetwork) return cb(window.dafNetwork);
  let tries = 0;
  const t = setInterval(() => {
    if (window.dafNetwork) { clearInterval(t); cb(window.dafNetwork); }
    else if (++tries > 100) clearInterval(t);
  }, 50);
}

const root = document.querySelector('[data-network-rail]');
if (root) {
  awaitApi((api) => init(api, root));
}
