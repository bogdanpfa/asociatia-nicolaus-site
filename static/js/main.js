// Meniu mobil -- fără cadru JS, doar toggle simplu.
document.addEventListener("DOMContentLoaded", function () {
  var buton = document.querySelector(".nav-toggle");
  var meniu = document.querySelector(".nav-principal");
  if (buton && meniu) {
    buton.addEventListener("click", function () {
      var deschis = meniu.classList.toggle("deschis");
      buton.setAttribute("aria-expanded", deschis ? "true" : "false");
    });
  }

  // Consimțământ cookie-uri, granular -- doar necesare vs. accept tot.
  var banner = document.querySelector(".cookie-banner");
  if (banner) {
    var alegere = null;
    try { alegere = localStorage.getItem("nicolaus_cookies"); } catch (e) {}
    if (alegere) {
      banner.hidden = true;
    } else {
      banner.hidden = false;
    }
    banner.querySelectorAll("[data-cookie-alegere]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        try { localStorage.setItem("nicolaus_cookies", btn.dataset.cookieAlegere); } catch (e) {}
        banner.hidden = true;
      });
    });
  }

  // Buton flotant -- redeschide oricand preferintele de cookie-uri, indiferent de alegerea anterioara.
  var butonCookie = document.getElementById("btn-cookie-reopen");
  if (butonCookie && banner) {
    butonCookie.addEventListener("click", function () {
      banner.hidden = false;
    });
  }
});


// harta de contact -- incarcata abia la click, ca sa nu tragem continut de la Google inainte ca vizitatorul sa ceara asta
(function () {
  const facade = document.getElementById("harta-facade");
  const buton = document.getElementById("btn-harta");
  if (!facade || !buton) return;
  buton.addEventListener("click", function () {
    const iframe = document.createElement("iframe");
    iframe.src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2447.855101210913!2d27.102139675868358!3d47.31496330807169!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40cad7522ce4bdfd%3A0x3dfa44d211957dab!2sAsocia%C8%9Bia%20Nicolaus!5e1!3m2!1sro!2sro!4v1789234904919!5m2!1sro!2sro";
    iframe.loading = "lazy";
    iframe.referrerPolicy = "strict-origin-when-cross-origin";
    iframe.title = "Harta -- Asociația Nicolaus, Satu Nou, Belcești";
    facade.replaceChildren(iframe);
  });
})();

// lightbox generic -- marim orice poza dintr-un foto-card (mai putin harta) la click
(function () {
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = document.getElementById("lightbox-img");
  var lightboxCaption = document.getElementById("lightbox-caption");
  var butonInchide = document.getElementById("btn-lightbox-inchide");
  if (!lightbox || !lightboxImg || !butonInchide) return;

  function deschide(img) {
    lightboxImg.src = img.currentSrc || img.src;
    lightboxImg.alt = img.alt || "";
    lightboxCaption.textContent = img.alt || "";
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
  }
  function inchide() {
    lightbox.hidden = true;
    lightboxImg.src = "";
    document.body.style.overflow = "";
  }
  document.querySelectorAll(".foto-card:not(.harta-facade) img").forEach(function (img) {
    img.addEventListener("click", function () { deschide(img); });
  });
  butonInchide.addEventListener("click", inchide);
  lightbox.addEventListener("click", function (e) {
    if (e.target === lightbox) inchide();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !lightbox.hidden) inchide();
  });
})();

// filtrare pe categorie, generica -- folosita si de Galerie si de Jurnalul de santier,
// ca sa functioneze identic pe site-ul static (fara server care sa filtreze query string-uri)
function initFiltruCategorie(idContainer, selectorIteme) {
  var filtre = document.getElementById(idContainer);
  if (!filtre) return;
  var iteme = document.querySelectorAll(selectorIteme);
  filtre.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      filtre.querySelectorAll("a").forEach(function (a) { a.classList.remove("activ"); });
      link.classList.add("activ");
      var filtru = link.dataset.filtru;
      iteme.forEach(function (item) {
        var arata = filtru === "toate" || item.dataset.categorie === filtru;
        item.hidden = !arata;
      });
    });
  });
}
initFiltruCategorie("filtre-galerie", ".galerie-item");
initFiltruCategorie("filtre-santier", ".intrare");
