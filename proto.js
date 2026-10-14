/* WasabiRub 2027 — prototype controller. Live design/typeface toggles that
 * persist across pages (localStorage). Hide with ?proto=off, show with ?proto. */
(function () {
  "use strict";
  var KEY = "wrproto";
  var DEF = { typeface: "deck", accent: "lime", hero: "hot", band: "finish", nums: "off", hidden: false, collapsed: false };

  function load() {
    var s = {};
    try { s = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) {}
    var out = {}; for (var k in DEF) out[k] = (k in s) ? s[k] : DEF[k];
    return out;
  }
  function save(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }

  var s = load();
  // URL control of visibility
  var q = new URLSearchParams(location.search);
  if (q.has("proto")) { s.hidden = (q.get("proto") === "off"); save(s); }

  var JAR = { hot: "assets/jar-hot.png", og: "assets/jar-og.png", cold: "assets/jar-cold.png" };
  var BAND = { finish: "assets/life-finish.jpg", cycle: "assets/life-cycle.jpg", team: "assets/life-team.jpg", climb: "assets/life-climb.jpg" };

  function apply() {
    var el = document.documentElement;
    el.dataset.typeface = s.typeface;
    el.dataset.accent = s.accent;
    el.dataset.nums = s.nums;
    var hj = document.getElementById("hero-jar"); if (hj && JAR[s.hero]) hj.src = JAR[s.hero];
    var bp = document.getElementById("band-photo"); if (bp && BAND[s.band]) bp.src = BAND[s.band];
  }
  apply(); // apply settings even before DOM-ready for data-* (html exists)

  function seg(label, key, opts) {
    var g = document.createElement("div"); g.className = "proto-grp";
    var l = document.createElement("label"); l.textContent = label; g.appendChild(l);
    var row = document.createElement("div"); row.className = "proto-seg";
    opts.forEach(function (o) {
      var b = document.createElement("button"); b.type = "button"; b.textContent = o[1];
      if (s[key] === o[0]) b.className = "on";
      b.addEventListener("click", function () {
        s[key] = o[0]; save(s); apply();
        [].forEach.call(row.children, function (c) { c.classList.remove("on"); });
        b.classList.add("on");
      });
      row.appendChild(b);
    });
    g.appendChild(row); return g;
  }

  function thumbs(label, key, opts) {
    var g = document.createElement("div"); g.className = "proto-grp";
    var l = document.createElement("label"); l.textContent = label; g.appendChild(l);
    var row = document.createElement("div"); row.className = "proto-thumbs";
    opts.forEach(function (o) {
      var b = document.createElement("button"); b.type = "button"; b.title = o[1];
      var im = document.createElement("img"); im.src = o[2]; im.alt = o[1]; b.appendChild(im);
      if (s[key] === o[0]) b.className = "on";
      b.addEventListener("click", function () {
        s[key] = o[0]; save(s); apply();
        [].forEach.call(row.children, function (c) { c.classList.remove("on"); });
        b.classList.add("on");
      });
      row.appendChild(b);
    });
    g.appendChild(row); return g;
  }

  function buildPanel() {
    if (document.querySelector(".proto")) return;
    var p = document.createElement("div");
    p.className = "proto" + (s.collapsed ? " collapsed" : "");
    if (s.hidden) p.hidden = true;

    var head = document.createElement("div"); head.className = "proto-head";
    var b = document.createElement("b"); b.textContent = "PROTOTYPE";
    var min = document.createElement("button"); min.className = "proto-min"; min.type = "button";
    min.setAttribute("aria-label", "Collapse"); min.textContent = s.collapsed ? "+" : "−";
    min.addEventListener("click", function () {
      p.classList.toggle("collapsed");
      var c = p.classList.contains("collapsed"); s.collapsed = c; save(s);
      min.textContent = c ? "+" : "−";
    });
    head.appendChild(b); head.appendChild(min); p.appendChild(head);

    var body = document.createElement("div"); body.className = "proto-body";
    body.appendChild(seg("Typeface", "typeface", [["deck", "A · Deck"], ["editorial", "B · Editorial"], ["classic", "C · Classic"]]));
    body.appendChild(seg("Accent", "accent", [["lime", "Lime"], ["amber", "Amber"], ["sky", "Sky"]]));
    body.appendChild(seg("Hero product", "hero", [["hot", "Super Hot"], ["og", "Original"], ["cold", "Super Cold"]]));
    body.appendChild(thumbs("Statement band", "band", [
      ["finish", "Finish line", "assets/life-finish.jpg"],
      ["cycle", "Cyclists", "assets/life-cycle.jpg"],
      ["team", "Team", "assets/life-team.jpg"],
      ["climb", "Climbing", "assets/life-climb.jpg"]
    ]));
    body.appendChild(seg("Section numbers", "nums", [["off", "Off"], ["on", "On"]]));

    var note = document.createElement("p"); note.className = "proto-note";
    note.innerHTML = "Prototype only. Choices follow you across pages. Add <code>?proto=off</code> to the address to hide this; <code>?proto</code> brings it back.";
    body.appendChild(note);

    p.appendChild(body);
    document.body.appendChild(p);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", buildPanel);
  else buildPanel();
})();
