/*
 * Syntax highlighting for Hyperlambda code blocks.
 *
 * The site is built by GitHub Pages, whose highlighter (Rouge) has no Hyperlambda lexer and
 * cannot be given one, so a block fenced as "hyperlambda" arrives as plain text. This wraps
 * its tokens in the class names Rouge uses for other languages, which overrides.css already
 * colours, plus hl-x for expressions and hl-t for type prefixes.
 *
 * Hyperlambda is a tree, one node per line, as "name:value", nested by three spaces, so a
 * line-by-line pass is all it takes: comments, node names, values, and the two kinds of
 * string that can run over several lines, /* ... *\/ comments and @"..." strings.
 */
(function () {
  var TYPES = /^(bool|int|long|decimal|double|float|date|guid|time|node|string|object|byte|char|short|uint|ulong|ushort|sbyte):/;

  function esc(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function span(cls, s) {
    return s === '' ? '' : '<span class="' + cls + '">' + esc(s) + '</span>';
  }

  // Index of the quote ending a verbatim string, where a doubled quote is an escaped one.
  function closingQuote(line, from) {
    for (var i = from; i < line.length; i++) {
      if (line.charAt(i) === '"') {
        if (line.charAt(i + 1) === '"') { i++; continue; }
        return i;
      }
    }
    return -1;
  }

  function name(s) {
    return span(s.charAt(0) === '.' ? 'nv' : 'nt', s);
  }

  function highlight(text) {
    var lines = text.split('\n');
    var out = [];
    var inComment = false;
    var inVerbatim = false;

    lines.forEach(function (line) {
      if (inComment) {
        var end = line.indexOf('*/');
        if (end < 0) { out.push(span('cm', line)); return; }
        out.push(span('cm', line.slice(0, end + 2)) + esc(line.slice(end + 2)));
        inComment = false;
        return;
      }
      if (inVerbatim) {
        var close = closingQuote(line, 0);
        if (close < 0) { out.push(span('s', line)); return; }
        out.push(span('s', line.slice(0, close + 1)) + esc(line.slice(close + 1)));
        inVerbatim = false;
        return;
      }

      var indent = /^\s*/.exec(line)[0];
      var rest = line.slice(indent.length);
      if (rest === '') { out.push(line); return; }

      if (rest.indexOf('//') === 0) { out.push(indent + span('c1', rest)); return; }
      if (rest.indexOf('/*') === 0) {
        var stop = rest.indexOf('*/', 2);
        if (stop < 0) { inComment = true; out.push(indent + span('cm', rest)); return; }
        out.push(indent + span('cm', rest.slice(0, stop + 2)) + esc(rest.slice(stop + 2)));
        return;
      }

      var colon = rest.indexOf(':');
      if (colon < 0) { out.push(indent + name(rest)); return; }
      var value = rest.slice(colon + 1);
      var html;
      var type = TYPES.exec(value);
      if (/^x:/.test(value)) {
        html = span('hl-x', value);
      } else if (type) {
        html = span('hl-t', type[0]) + span('m', value.slice(type[0].length));
      } else if (value.indexOf('@"') === 0) {
        var shut = closingQuote(value, 2);
        if (shut < 0) { inVerbatim = true; }
        html = span('s', value);
      } else {
        html = span('s', value);
      }
      out.push(indent + name(rest.slice(0, colon)) + span('p', ':') + html);
    });
    return out.join('\n');
  }

  if (typeof module !== 'undefined') { module.exports = { highlight: highlight }; }

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function () {
      var blocks = document.querySelectorAll('div.language-hyperlambda pre code, div.language-hl pre code');
      Array.prototype.forEach.call(blocks, function (code) {
        // Already tokenised by Rouge or by an earlier run.
        if (code.children.length === 0) { code.innerHTML = highlight(code.textContent); }
      });
    });
  }
})();
