/*
 * Loads the JSON declaration of a slot when its expandable section is opened.
 *
 * A slot page holds its declaration inline when it is small. The large ones, the read slots
 * run to 25 KB, are not in the page at all, so the page stays small for readers and scrapers
 * alike, and the declaration is fetched from the slot.json next to the page the first time
 * the section is opened. It is shown the way the other code blocks are, highlighted, with a
 * copy button.
 */
(function () {
  function esc(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // The class names Rouge uses for JSON, which overrides.css already colours.
  function highlight(text) {
    var token = /("(?:[^"\\]|\\.)*")(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[{}\[\],:]/g;
    return text.replace(token, function (match, str, colon, literal) {
      if (str !== undefined) {
        return colon
          ? '<span class="nt">' + esc(str) + '</span><span class="p">' + esc(colon) + '</span>'
          : '<span class="s2">' + esc(str) + '</span>';
      }
      if (literal !== undefined) { return '<span class="kc">' + match + '</span>'; }
      if (/^[{}\[\],:]$/.test(match)) { return '<span class="p">' + match + '</span>'; }
      return '<span class="mi">' + match + '</span>';
    });
  }

  function show(details, text) {
    var outer = document.createElement('div');
    outer.className = 'language-json highlighter-rouge';
    var inner = document.createElement('div');
    inner.className = 'highlight';
    var pre = document.createElement('pre');
    pre.className = 'highlight';
    var code = document.createElement('code');
    code.innerHTML = highlight(text.replace(/\n$/, ''));
    pre.appendChild(code);
    inner.appendChild(pre);
    outer.appendChild(inner);
    details.appendChild(outer);
    if (window.magicCopyCode) { window.magicCopyCode(outer); }
  }

  function load(details) {
    if (details.getAttribute('data-state')) { return; }
    details.setAttribute('data-state', 'loading');
    var status = document.createElement('p');
    status.textContent = 'Loading the declaration ...';
    details.appendChild(status);
    fetch(details.getAttribute('data-src'))
      .then(function (response) {
        if (!response.ok) { throw new Error('HTTP ' + response.status); }
        return response.text();
      })
      .then(function (text) {
        details.removeChild(status);
        details.setAttribute('data-state', 'loaded');
        show(details, text);
      })
      .catch(function (error) {
        status.textContent = 'Could not load the declaration (' + error.message + '). Open slot.json directly.';
        details.removeAttribute('data-state');
      });
  }

  function init() {
    var sections = document.querySelectorAll('details.slot-json');
    Array.prototype.forEach.call(sections, function (details) {
      details.addEventListener('toggle', function () {
        if (details.open) { load(details); }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
