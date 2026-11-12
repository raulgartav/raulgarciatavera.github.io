/* Interacción de la web. Todo es opcional: sin JavaScript la página se lee completa.
   1 barra y menú · 2 aparición al hacer scroll · 3 vídeo de portada · 4 progreso e índice
   5 visor de imágenes · 6 Cruz de Malta (cinemática real) */
(function () {
  "use strict";
  var TXT = window.TXT || {};
  var doc = document, raiz = doc.documentElement;
  var reducir = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hayIO = "IntersectionObserver" in window;
  var todos = function (sel, base) { return Array.prototype.slice.call((base || doc).querySelectorAll(sel)); };

  /* ── 1. Barra: línea inferior al bajar y menú en pantallas pequeñas ── */
  var barra = doc.querySelector(".barra");
  var btnMenu = doc.querySelector(".menu-btn"), nav = doc.getElementById("nav");
  if (btnMenu && nav) {
    btnMenu.hidden = false;
    var cerrarMenu = function () { nav.classList.remove("abierto"); btnMenu.setAttribute("aria-expanded", "false"); };
    btnMenu.addEventListener("click", function () {
      var abrir = !nav.classList.contains("abierto");
      nav.classList.toggle("abierto", abrir);
      btnMenu.setAttribute("aria-expanded", String(abrir));
    });
    nav.addEventListener("click", function (ev) { if (ev.target.closest("a")) cerrarMenu(); });
    doc.addEventListener("keydown", function (ev) { if (ev.key === "Escape" && nav.classList.contains("abierto")) { cerrarMenu(); btnMenu.focus(); } });
  }

  /* ── 2. Aparición al hacer scroll ── */
  var porVer = todos(".rv, .rv-foto");
  if (!hayIO || reducir) {
    porVer.forEach(function (el) { el.classList.add("visto"); });
  } else {
    var ver = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("visto");
        ver.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
    // una foto recortada por completo no "se ve": se vigila su proyecto y se destapa la foto
    porVer.forEach(function (el) {
      if (!el.classList.contains("rv-foto")) { ver.observe(el); return; }
      var foto = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return;
        el.classList.add("visto"); foto.disconnect();
      }, { rootMargin: "0px 0px -18% 0px", threshold: 0 });
      foto.observe(el.parentNode);
    });
  }

  /* ── 3. Vídeo de portada: se reproduce solo mientras está a la vista ── */
  todos("video[data-auto]").forEach(function (v) {
    var btn = v.parentNode.querySelector(".video-btn");
    var quiere = !reducir, aLaVista = false;
    var aplicar = function () {
      if (quiere && aLaVista) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
      else v.pause();
      if (btn) btn.textContent = quiere ? TXT.pausa : TXT.reproducir;
    };
    if (btn) {
      btn.hidden = false;
      btn.addEventListener("click", function () { quiere = !quiere; aplicar(); });
    }
    if (hayIO) new IntersectionObserver(function (en) { aLaVista = en[0].isIntersecting; aplicar(); }, { threshold: 0.35 }).observe(v);
    else { aLaVista = true; aplicar(); }
  });

  /* ── 4. Progreso de lectura, línea de la barra e índice del proyecto ── */
  var progreso = doc.querySelector(".progreso"), relleno = progreso && progreso.firstElementChild;
  var pendiente = false;
  var alDesplazar = function () {
    pendiente = false;
    var y = window.scrollY || raiz.scrollTop;
    if (barra) barra.classList.toggle("fijada", y > 8);
    if (relleno) {
      var total = raiz.scrollHeight - window.innerHeight;
      var f = total > 0 ? Math.min(1, Math.max(0, y / total)) : 0;
      relleno.style.transform = "scaleX(" + f.toFixed(4) + ")";
      progreso.setAttribute("aria-valuenow", Math.round(f * 100));
    }
  };
  window.addEventListener("scroll", function () { if (!pendiente) { pendiente = true; requestAnimationFrame(alDesplazar); } }, { passive: true });
  window.addEventListener("resize", alDesplazar);
  alDesplazar();

  var enlaces = todos(".indice a");
  if (enlaces.length && hayIO) {
    var mapa = {}, visibles = {}, secciones = todos(".psec");
    enlaces.forEach(function (a) { mapa[a.getAttribute("href").slice(1)] = a; });
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) { visibles[en.target.id] = en.isIntersecting; });
      var activo = null;
      secciones.forEach(function (s) { if (!activo && visibles[s.id]) activo = s.id; });
      if (!activo) return;
      enlaces.forEach(function (a) { a.removeAttribute("aria-current"); });
      if (mapa[activo]) mapa[activo].setAttribute("aria-current", "true");
    }, { rootMargin: "-80px 0px -55% 0px" });
    secciones.forEach(function (s) { obs.observe(s); });
  }

  /* ── 5. Visor de imágenes ── */
  var vinculos = todos("a[data-visor]");
  if (vinculos.length) {
    var visor = doc.createElement("div");
    visor.className = "visor"; visor.hidden = true;
    visor.setAttribute("role", "dialog"); visor.setAttribute("aria-modal", "true");
    visor.innerHTML =
      '<div class="visor-barra"><span class="visor-n"></span><button type="button" class="visor-cerrar">' + (TXT.cerrar || "×") + '</button></div>' +
      '<div class="visor-img"><img alt=""></div>' +
      '<div class="visor-pie"><button type="button" class="visor-ant">' + (TXT.anterior || "‹") + '</button>' +
      '<span class="visor-texto"></span><button type="button" class="visor-sig">' + (TXT.posterior || "›") + '</button></div>';
    doc.body.appendChild(visor);
    var img = visor.querySelector("img"), texto = visor.querySelector(".visor-texto"), n = visor.querySelector(".visor-n");
    var actual = 0, origen = null;
    var mostrar = function (i) {
      actual = (i + vinculos.length) % vinculos.length;
      var a = vinculos[actual], pie = a.parentNode.querySelector("figcaption");
      img.style.animation = "none"; void img.offsetWidth; img.style.animation = "";
      img.src = a.getAttribute("href");
      img.alt = a.querySelector("img").alt;
      texto.textContent = pie ? pie.textContent : "";
      n.textContent = (actual + 1) + " / " + vinculos.length;
    };
    var cerrar = function () {
      visor.hidden = true; doc.body.classList.remove("visor-abierto");
      if (origen) origen.focus();
    };
    vinculos.forEach(function (a, i) {
      a.addEventListener("click", function (ev) {
        if (ev.metaKey || ev.ctrlKey || ev.shiftKey) return;
        ev.preventDefault(); origen = a; mostrar(i);
        visor.hidden = false; doc.body.classList.add("visor-abierto");
        visor.querySelector(".visor-cerrar").focus();
      });
    });
    visor.querySelector(".visor-cerrar").addEventListener("click", cerrar);
    visor.querySelector(".visor-ant").addEventListener("click", function () { mostrar(actual - 1); });
    visor.querySelector(".visor-sig").addEventListener("click", function () { mostrar(actual + 1); });
    visor.addEventListener("click", function (ev) { if (ev.target === visor || ev.target.classList.contains("visor-img")) cerrar(); });
    doc.addEventListener("keydown", function (ev) {
      if (visor.hidden) return;
      if (ev.key === "Escape") cerrar();
      else if (ev.key === "ArrowLeft") mostrar(actual - 1);
      else if (ev.key === "ArrowRight") mostrar(actual + 1);
      else if (ev.key === "Tab") {
        var b = visor.querySelectorAll("button"), pri = b[0], ult = b[b.length - 1];
        if (ev.shiftKey && doc.activeElement === pri) { ev.preventDefault(); ult.focus(); }
        else if (!ev.shiftKey && doc.activeElement === ult) { ev.preventDefault(); pri.focus(); }
      }
    });
  }

  /* ── 6. Cruz de Malta: cinemática real de un mecanismo de 4 ranuras ──
     La rueda motriz gira de forma continua. Mientras su pivote está dentro de una ranura
     (±45° respecto a la línea de centros) arrastra la cruz 90°; el resto de la vuelta, la cruz
     queda bloqueada. El ángulo de la cruz sale de la geometría: θ = atan2(r·sen φ, a − r·cos φ). */
  todos("[data-ginebra]").forEach(function (fig) {
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
      if (cursor) cursor.style.left = ((f + 180) / 360 * 100).toFixed(2) + "%";
      var bloq = Math.abs(f) > 45;
      if (bloq !== ultimo) {
        ultimo = bloq;
        fig.classList.toggle("bloqueada", bloq);
        if (estado) estado.textContent = fig.getAttribute(bloq ? "data-bloq" : "data-gira");
      }
    }
    function paso(ahora) {
      if (!enMarcha || !enVista) { t0 = null; return; }
      if (t0 === null) t0 = ahora - acumulado;
      acumulado = ahora - t0;
      pose(acumulado);
      requestAnimationFrame(paso);
    }
    function arrancar() { if (enMarcha && enVista && t0 === null) requestAnimationFrame(paso); }

    if (btn) {
      btn.hidden = false;
      btn.textContent = enMarcha ? TXT.pausa : TXT.reproducir;
      btn.addEventListener("click", function () {
        enMarcha = !enMarcha;
        btn.textContent = enMarcha ? TXT.pausa : TXT.reproducir;
        arrancar();
      });
    }
    if (hayIO) new IntersectionObserver(function (en) { enVista = en[0].isIntersecting; arrancar(); }).observe(fig);
    pose(acumulado);
    arrancar();
  });
})();
