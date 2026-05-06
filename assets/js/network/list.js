/* Materials Discovery Network — list view + graph↔list sync (Phase 5).
 *
 * Renders cards for the currently-visible node set into a #network-list
 * element. Subscribes to api.onChange so it re-renders whenever the
 * filter or search predicate changes. Hovering a card highlights the
 * corresponding node; clicking a presentation/worksheet card triggers
 * a download (article cards just navigate via the <a> href).
 */

const TYPE_GLYPH = {
  article: '●',
  presentation: '■',
  worksheet: '◆',
};

const TYPE_LABEL = {
  article: 'Artikel',
  presentation: 'Foliensatz',
  worksheet: 'Arbeitsblatt',
};

function topicLabel(t) {
  if (!t) return '';
  return t.charAt(0).toUpperCase() + t.slice(1);
}

function levelLabel(course) {
  return (course || '').replace('kurs_', '').toUpperCase();
}

function cardHTML(n) {
  const isArticle = n.type === 'article';
  const url = n.url || '#';
  const meta = [TYPE_LABEL[n.type], levelLabel(n.course), topicLabel(n.topic)]
    .filter(Boolean)
    .join(' · ');
  const tags = (n.tags || [])
    .slice(0, 3)
    .map((t) => `<span class="tag">${t}</span>`)
    .join('');
  const placeholder = n.materials_status === 'placeholder'
    ? '<span class="placeholder-badge">Platzhalter</span>'
    : '';
  const titleHTML = isArticle
    ? `<a href="${url}">${n.title}</a>`
    : n.title;
  return `
    <article class="network-card${isArticle ? ' article' : ''}" data-topic="${n.topic || ''}" data-node-id="${n.id}">
      <span class="meta">${meta}</span>
      <h3 class="title">${titleHTML}</h3>
      ${placeholder}
      ${tags ? `<div class="tag-row">${tags}</div>` : ''}
      ${isArticle ? `<div class="type-row"><span class="glyph">${TYPE_GLYPH.article} Artikel</span><span class="glyph">${TYPE_GLYPH.presentation} Foliensatz</span><span class="glyph">${TYPE_GLYPH.worksheet} Arbeitsblatt</span></div>` : ''}
    </article>
  `;
}

export function init(api, mount) {
  if (!api || !mount) return;
  const nodesById = new Map(api.data.nodes.map((n) => [n.id, n]));

  // Sort by type (articles first), then by course, then by title.
  const TYPE_ORDER = { article: 0, presentation: 1, worksheet: 2 };
  function sortNodes(visibleIds) {
    const arr = [...visibleIds].map((id) => nodesById.get(id)).filter(Boolean);
    arr.sort((a, b) => {
      const t = (TYPE_ORDER[a.type] ?? 9) - (TYPE_ORDER[b.type] ?? 9);
      if (t !== 0) return t;
      const c = (a.course || '').localeCompare(b.course || '');
      if (c !== 0) return c;
      return (a.title || '').localeCompare(b.title || '', 'de');
    });
    return arr;
  }

  function render(visibleIds) {
    const arr = sortNodes(visibleIds);
    if (arr.length === 0) {
      mount.innerHTML = `
        <div class="network-empty" role="status">
          Keine Materialien entsprechen den aktuellen Filtern.
          Versuchen Sie, einen Filter zu lockern.
        </div>`;
      return;
    }
    mount.innerHTML = arr.map(cardHTML).join('');
  }

  api.onChange(render);

  // Bidirectional hover sync.
  mount.addEventListener('mouseover', (e) => {
    const card = e.target.closest('.network-card[data-node-id]');
    if (!card) return;
    api.highlightNode(card.dataset.nodeId, true);
  });
  mount.addEventListener('mouseout', (e) => {
    const card = e.target.closest('.network-card[data-node-id]');
    if (!card) return;
    api.highlightNode(card.dataset.nodeId, false);
  });

  // Card click for non-article downloads. Article cards already use a
  // plain <a>.
  mount.addEventListener('click', (e) => {
    const card = e.target.closest('.network-card[data-node-id]');
    if (!card) return;
    const node = nodesById.get(card.dataset.nodeId);
    if (!node || node.type === 'article') return;
    if (e.target.closest('a, button')) return;
    if (!node.url) return;
    const a = document.createElement('a');
    a.href = node.url;
    a.download = '';
    document.body.appendChild(a);
    a.click();
    a.remove();
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

const mount = document.getElementById('network-list');
if (mount) awaitApi((api) => init(api, mount));
