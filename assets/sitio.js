/* Interacción de la web: índice activo, visor de imágenes y animación de la Cruz de Malta.
   Todo es opcional: sin JavaScript la página se lee completa. */
(function () {
  "use strict";
  var TXT = window.TXT || {};
  var reducir = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ── Índice: marca la sección que se está leyendo ── */
  var enlaces = document.querySelectorAll(".indice a");
  if (enlaces.length && "IntersectionObserver" in window) {
    var mapa = {};
    enlaces.forEach(function (a) { mapa[a.getAttribute("href").slice(1)] = a; });
    var visibles = {};
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) { visibles[en.target.id] = en.isIntersecting; });
      var activo = null;
      document.querySelectorAll(".psec").forEach(function (s) { if (!activo && visibles[s.id]) activo = s.id; });
      if (!activo) return;
      enlaces.forEach(function (a) { a.removeAttribute("aria-current"); });
      if (mapa[activo]) mapa[activo].setAttribute("aria-current", "true");
    }, { rootMargin: "-80px 0px -55% 0px" });
    document.querySelectorAll(".psec").forEach(function (s) { obs.observe(s); });
  }

  /* ── Visor de imágenes ── */
  var vinculos = Array.prototype.slice.call(document.querySelectorAll("a[data-visor]"));
  if (vinculos.length) {
    var visor = document.createElement("div");
    visor.className = "visor"; visor.hidden = true;
    visor.setAttribute("role", "dialog"); visor.setAttribute("aria-modal", "true");
    visor.innerHTML =
      '<div class="visor-barra"><span class="visor-n"></span><button type="button" class="visor-cerrar">' + (TXT.cerrar || "×") + '</button></div>' +
      '<div class="visor-img"><img alt=""></div>' +
      '<div class="visor-pie"><button type="button" class="visor-ant">← ' + (TXT.anterior || "") + '</button>' +
      '<span class="visor-texto"></span><button type="button" class="visor-sig">' + (TXT.posterior || "") + ' →</button></div>';
    document.body.appendChild(visor);
    var img = visor.querySelector("img"), texto = visor.querySelector(".visor-texto"), n = visor.querySelector(".visor-n");
    var actual = 0, origen = null;
    var mostrar = function (i) {
      actual = (i + vinculos.length) % vinculos.length;
      var a = vinculos[actual], pie = a.parentNode.querySelector("figcaption");
      img.src = a.getAttribute("href");
      img.alt = a.querySelector("img").alt;
      texto.textContent = pie ? pie.textContent : "";
      n.textContent = (actual + 1) + " / " + vinculos.length;
    };
    var cerrar = function () {
      visor.hidden = true; document.body.classList.remove("visor-abierto");
      if (origen) origen.focus();
    };
    vinculos.forEach(function (a, i) {
      a.addEventListener("click", function (ev) {
        if (ev.metaKey || ev.ctrlKey || ev.shiftKey) return;
        ev.preventDefault(); origen = a; mostrar(i);
        visor.hidden = false; document.body.classList.add("visor-abierto");
        visor.querySelector(".visor-cerrar").focus();
      });
    });
    visor.querySelector(".visor-cerrar").addEventListener("click", cerrar);
    visor.querySelector(".visor-ant").addEventListener("click", function () { mostrar(actual - 1); });
    visor.querySelector(".visor-sig").addEventListener("click", function () { mostrar(actual + 1); });
    visor.addEventListener("click", function (ev) { if (ev.target === visor || ev.target.classList.contains("visor-img")) cerrar(); });
    document.addEventListener("keydown", function (ev) {
      if (visor.hidden) return;
      if (ev.key === "Escape") cerrar();
      else if (ev.key === "ArrowLeft") mostrar(actual - 1);
      else if (ev.key === "ArrowRight") mostrar(actual + 1);
      else if (ev.key === "Tab") {
        var b = visor.querySelectorAll("button"), pri = b[0], ult = b[b.length - 1];
        if (ev.shiftKey && document.activeElement === pri) { ev.preventDefault(); ult.focus(); }
        else if (!ev.shiftKey && document.activeElement === ult) { ev.preventDefault(); pri.focus(); }
      }
    });
  }

  /* ── Cruz de Malta: cinemática real de un mecanismo de 4 ranuras ── */
  document.querySelectorAll(".ginebra").forEach(function (fig) {
    var d = JSON.parse(fig.getAttribute("data-ginebra"));
    var cruz = fig.querySelector(".gin-cruz"), motriz = fig.querySelector(".gin-motriz");
    var estado = fig.querySelector(".gin-estado"), cursor = fig.querySelector(".gin-cursor");
    var btn = fig.querySelector(".gin-btn");
    var GRADO = Math.PI / 180, PERIODO = 4000;      // ms por vuelta de la rueda motriz
    var t0 = null, acumulado = 18 / 360 * PERIODO + PERIODO / 2, enMarcha = !reducir, enVista = true, ultimo = null;

    function pose(ms) {
      var fRaw = (ms / PERIODO) * 360 - 180;           // ángulo del pivote medido desde la línea de centros
      var vueltas = Math.floor((fRaw + 180) / 360);
      var f = ((fRaw + 180) % 360 + 360) % 360 - 180;  // (-180, 180]
      var theta;
      if (f > 45) theta = 45;
      else if (f < -45) theta = -45;
      else theta = Math.atan2(d.r * Math.sin(f * GRADO), d.a - d.r * Math.cos(f * GRADO)) / GRADO;
      theta += 90 * vueltas;
      cruz.setAttribute("transform", "rotate(" + theta.toFixed(2) + ")");
      motriz.setAttribute("transform", "translate(" + d.a + " 0) rotate(" + (180 - f).toFixed(2) + ")");
      cursor.style.left = ((f + 180) / 360 * 100).toFixed(2) + "%";
      var bloq = Math.abs(f) > 45;
      if (bloq !== ultimo) {
        ultimo = bloq;
        fig.classList.toggle("bloqueada", bloq);
        estado.textContent = fig.getAttribute(bloq ? "data-bloq" : "data-gira");
      }
    }
    function paso(ahora) {
      if (!enMarcha || !enVista) { t0 = null; return; }
      if (t0 === null) t0 = ahora - acumulado;
      acumulado = ahora - t0;
      pose(acumulado);
      requestAnimationFrame(paso);
    }
    function arrancar() { if (enMarcha && enVista) requestAnimationFrame(paso); }

    btn.hidden = false;
    btn.textContent = enMarcha ? TXT.pausa : TXT.reproducir;
    btn.addEventListener("click", function () {
      enMarcha = !enMarcha;
      btn.textContent = enMarcha ? TXT.pausa : TXT.reproducir;
      arrancar();
    });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) { enVista = en[0].isIntersecting; arrancar(); }).observe(fig);
    }
    pose(acumulado);
    arrancar();
  });
})();
