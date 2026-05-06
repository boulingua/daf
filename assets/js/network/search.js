/* Materials Discovery Network — Pagefind search (Phase 5).
 *
 * - Reads the search input + clear button from the DOM.
 * - Imports Pagefind dynamically from /pagefind/pagefind.js (built
 *   post-`hugo` in CI). Local dev without a Pagefind index degrades
 *   gracefully: the input becomes a tag-substring filter so typing
 *   still narrows the graph.
 * - Translates a query into a search predicate the main store
 *   composes with the facet predicate.
 * - Articles match if Pagefind matches their URL. Presentations and
 *   worksheets match if their `parent_article` matches.
 * - Empty query == no search constraint (predicate = always true).
 * - Keyboard: '/' focuses the input from anywhere; Esc clears + blurs.
 */

const DEBOUNCE = 80;

function debounce(fn, ms) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

async function loadPagefind(base) {
  try {
    const url = new URL('pagefind/pagefind.js', base).toString();
    /* @vite-ignore */
    const mod = await import(/* webpackIgnore: true */ url);
    if (typeof mod.init === 'function') await mod.init();
    return mod;
  } catch (err) {
    console.info('[network/search] Pagefind not available — falling back to tag substring match.', err.message);
    return null;
  }
}

function buildLocalIndex(nodes) {
  // Article-keyed index: every article's haystack = title + tags joined.
  const idx = new Map();
  for (const n of nodes) {
    if (n.type !== 'article') continue;
    const hay = [n.title, ...(n.tags || []), n.topic, n.course]
      .join(' ')
      .toLowerCase();
    idx.set(n.url, hay);
  }
  return idx;
}

export async function init(api, root) {
  if (!api || !root) return;
  const input = root.querySelector('input[type="search"]');
  const clear = root.querySelector('[data-action="search-clear"]');
  if (!input) return;
  input.disabled = false;
  input.placeholder = 'Suchen — Titel, Tag, Modul, Topic…';

  const articleByParent = new Map();
  for (const n of api.data.nodes) {
    if (n.type !== 'article') continue;
    articleByParent.set(n.id, n.url);
  }

  const pagefind = await loadPagefind(window.location.href);
  const localIndex = pagefind ? null : buildLocalIndex(api.data.nodes);

  const apply = async (query) => {
    const q = (query || '').trim().toLowerCase();
    if (!q) {
      api.setSearchPredicate(null);
      return;
    }
    let matchUrls = new Set();
    if (pagefind) {
      try {
        const results = await pagefind.search(q);
        const datas = await Promise.all(results.results.map((r) => r.data()));
        for (const d of datas) matchUrls.add(d.url);
      } catch (err) {
        console.warn('[network/search] Pagefind error:', err);
      }
    } else {
      for (const [url, hay] of localIndex) {
        if (hay.includes(q)) matchUrls.add(url);
      }
    }
    api.setSearchPredicate((n) => {
      if (n.type === 'article') return matchUrls.has(n.url);
      const pUrl = articleByParent.get(n.parent_article);
      return pUrl ? matchUrls.has(pUrl) : false;
    });
  };

  input.addEventListener('input', debounce((e) => apply(e.target.value), DEBOUNCE));
  if (clear) {
    clear.addEventListener('click', () => {
      input.value = '';
      apply('');
      input.focus();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
      e.preventDefault();
      input.focus();
      input.select();
    } else if (e.key === 'Escape' && document.activeElement === input) {
      input.value = '';
      apply('');
      input.blur();
    }
  });
}

function awaitApi(cb) {
  if (window.dafNetwork) return cb(window.dafNetwork);
  let tries = 0;
  const t = setInterval(() => {
    if (window.dafNetwork) { clearInterval(t); cb(window.dafNetwork); }
    else if (++tries > 100) clearInterval(t);
  }, 50);
}

const root = document.querySelector('[data-network-search]');
if (root) awaitApi((api) => init(api, root));
