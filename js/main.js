// Petric Sonja : menu, révélations, images, galerie, vue en grand, formulaire et curseur.
// Aucune bibliothèque. Une seule boucle requestAnimationFrame pour le curseur.

const mouvementReduit = matchMedia("(prefers-reduced-motion: reduce)").matches;

document.addEventListener("DOMContentLoaded", () => {
  const annee = document.getElementById("annee");
  if (annee) annee.textContent = new Date().getFullYear();

  menu();
  revelations();
  images();
  galerie();
  formulaire();
  copier();
  curseur();
});

// Menu plein écran sur mobile : le mot « MENU » l'ouvre, Échap le ferme
function menu() {
  const bouton = document.querySelector(".menu-bouton");
  const nav = document.getElementById("menu");
  if (!bouton || !nav) return;
  const basculer = (ouvert) => {
    nav.classList.toggle("ouvert", ouvert);
    bouton.setAttribute("aria-expanded", ouvert);
    bouton.textContent = ouvert ? bouton.dataset.fermer : bouton.dataset.ouvrir;
    document.body.style.overflow = ouvert ? "hidden" : "";
  };
  bouton.addEventListener("click", () => basculer(!nav.classList.contains("ouvert")));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && nav.classList.contains("ouvert")) {
      basculer(false);
      bouton.focus();
    }
  });
}

// Apparition au défilement, une seule fois
function revelations() {
  const elements = document.querySelectorAll("[data-reveal]");
  if (mouvementReduit || !("IntersectionObserver" in window)) {
    elements.forEach((el) => el.classList.add("visible"));
    return;
  }
  const observateur = new IntersectionObserver(
    (entrees) => {
      entrees.forEach((entree) => {
        if (!entree.isIntersecting) return;
        entree.target.classList.add("visible");
        observateur.unobserve(entree.target);
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.05 }
  );
  elements.forEach((el) => observateur.observe(el));
}

// Fondu des images une fois chargées (depuis leur couleur dominante)
function images() {
  document.querySelectorAll("picture.fondu").forEach((picture) => {
    const img = picture.querySelector("img");
    const montrer = () => picture.classList.add("charge");
    if (img.complete && img.naturalWidth) montrer();
    else {
      img.addEventListener("load", montrer, { once: true });
      img.addEventListener("error", montrer, { once: true });
    }
  });
}

// Filtres, et vue en grand avec clavier (flèches, Échap)
function galerie() {
  const oeuvres = [...document.querySelectorAll(".galerie .oeuvre")];
  const filtres = [...document.querySelectorAll(".filtre")];

  filtres.forEach((filtre) => {
    filtre.addEventListener("click", () => {
      filtres.forEach((b) => b.setAttribute("aria-pressed", b === filtre));
      const cat = filtre.dataset.filtre;
      oeuvres.forEach((o) => {
        o.hidden = cat !== "tout" && o.dataset.categorie !== cat;
        if (!o.hidden) o.classList.add("visible");
      });
    });
  });
  // Filtre choisi par l'adresse, par exemple /realisations#enduits
  const depuisAdresse = filtres.find((b) => b.dataset.filtre === location.hash.slice(1));
  if (depuisAdresse) depuisAdresse.click();

  const vis = document.querySelector(".visionneuse");
  if (!vis) return;
  const img = vis.querySelector(".vis-figure img");
  const cartel = vis.querySelector(".vis-figure .cartel");
  const compteur = vis.querySelector(".vis-compteur");
  const ouvrables = () => oeuvres.filter((o) => !o.hidden && o.hasAttribute("data-ouvrable"));
  let courant = 0;
  let origine = null;

  const afficher = (o, animer) => {
    const source = o.querySelector("img");
    const liste = ouvrables();
    const remplir = () => {
      img.src = source.currentSrc || source.src;
      img.alt = source.alt;
      cartel.innerHTML = o.querySelector(".cartel").innerHTML;
      compteur.textContent = `${o.dataset.numero} / ${String(oeuvres.length).padStart(3, "0")}`;
      img.classList.remove("change");
    };
    if (animer && !mouvementReduit) {
      img.classList.add("change");
      setTimeout(remplir, 250);
    } else remplir();
    courant = liste.indexOf(o);
  };
  const ouvrir = (o) => {
    origine = document.activeElement;
    afficher(o, false);
    vis.hidden = false;
    document.body.classList.add("vis-active");
    requestAnimationFrame(() => vis.classList.add("ouverte"));
    vis.querySelector(".vis-fermer").focus();
  };
  const fermer = () => {
    vis.classList.remove("ouverte");
    document.body.classList.remove("vis-active");
    setTimeout(() => (vis.hidden = true), mouvementReduit ? 0 : 500);
    if (origine) origine.focus();
  };
  const deplacer = (pas) => {
    const liste = ouvrables();
    if (liste.length < 2) return;
    afficher(liste[(courant + pas + liste.length) % liste.length], true);
  };

  oeuvres.forEach((o) => {
    if (!o.hasAttribute("data-ouvrable")) return;
    o.addEventListener("click", () => ouvrir(o));
    o.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        ouvrir(o);
      }
    });
  });
  vis.querySelector(".vis-fermer").addEventListener("click", fermer);
  vis.querySelector(".vis-prec").addEventListener("click", () => deplacer(-1));
  vis.querySelector(".vis-suiv").addEventListener("click", () => deplacer(1));
  document.addEventListener("keydown", (e) => {
    if (vis.hidden) return;
    if (e.key === "Escape") fermer();
    if (e.key === "ArrowLeft") deplacer(-1);
    if (e.key === "ArrowRight") deplacer(1);
    if (e.key === "Tab") {
      // garder le focus dans la vue en grand
      const focusables = [...vis.querySelectorAll("button")];
      const i = focusables.indexOf(document.activeElement);
      if (e.shiftKey && i <= 0) {
        e.preventDefault();
        focusables.at(-1).focus();
      } else if (!e.shiftKey && i === focusables.length - 1) {
        e.preventDefault();
        focusables[0].focus();
      }
    }
  });
}

// Formulaire de devis : envoi sans quitter la page
function formulaire() {
  const form = document.querySelector(".formulaire");
  if (!form) return;
  const etat = form.querySelector(".etat");
  const bouton = form.querySelector("button[type=submit]");
  const d = form.dataset;
  const afficher = (texte, classe, avecEmail) => {
    etat.className = "etat mono " + classe;
    etat.textContent = texte + (avecEmail ? " " : "");
    if (avecEmail) {
      const lien = document.createElement("a");
      lien.href = "mailto:" + d.email;
      lien.textContent = d.email;
      etat.append(lien, ".");
    }
  };
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (d.actif !== "oui") return afficher(d.pasActif, "ko", true);
    bouton.disabled = true;
    afficher(d.envoi, "", false);
    try {
      const reponse = await fetch(form.action, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(Object.fromEntries(new FormData(form))),
      });
      if (!reponse.ok) throw new Error(reponse.status);
      form.reset();
      afficher(d.merci, "ok", false);
    } catch {
      afficher(d.erreur, "ko", true);
    } finally {
      bouton.disabled = false;
    }
  });
}

// Bouton « Copier » à côté de l'e-mail
function copier() {
  document.querySelectorAll("[data-copier]").forEach((bouton) => {
    const texte = bouton.textContent;
    bouton.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(bouton.dataset.copier);
        bouton.textContent = bouton.dataset.copie;
        setTimeout(() => (bouton.textContent = texte), 1800);
      } catch {
        /* presse-papiers refusé : l'e-mail reste sélectionnable */
      }
    });
  });
}

// Curseur de précision : point instantané, anneau en inertie, étirement selon la vitesse.
// Désactivé sur écran tactile et si le mouvement réduit est demandé.
function curseur() {
  const precis = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const racine = document.querySelector(".curseur");
  if (!precis || mouvementReduit || !racine) return;

  const point = racine.querySelector(".curseur-point");
  const anneau = racine.querySelector(".curseur-anneau");
  const label = racine.querySelector(".curseur-label");
  const coords = racine.querySelector(".curseur-coords");
  const voir = document.documentElement.lang === "fr" ? "Voir" : "View";

  const souris = { x: innerWidth / 2, y: innerHeight / 2 };
  const pos = { x: souris.x, y: souris.y };
  let aimant = null; // élément attiré vers le curseur
  let vu = false;

  document.documentElement.classList.add("curseur-actif");
  racine.classList.add("cache");

  addEventListener("pointermove", (e) => {
    souris.x = e.clientX;
    souris.y = e.clientY;
    if (!vu) {
      vu = true;
      pos.x = souris.x;
      pos.y = souris.y;
      racine.classList.remove("cache");
    }
  }, { passive: true });
  document.addEventListener("pointerleave", () => racine.classList.add("cache"));
  document.addEventListener("pointerenter", () => racine.classList.remove("cache"));
  addEventListener("pointerdown", () => racine.classList.add("presse"));
  addEventListener("pointerup", () => racine.classList.remove("presse"));

  const relacher = () => {
    if (aimant) aimant.style.translate = "";
    aimant = null;
  };

  document.addEventListener("pointerover", (e) => {
    const cible = e.target;
    const oeuvre = cible.closest(".oeuvre[data-ouvrable]");
    const lien = cible.closest("a, button, select, label.champ, .filtre");
    const texte = cible.closest("p, h1, h2, h3, li, input, textarea, figcaption");
    racine.classList.toggle("oeuvre", !!oeuvre);
    racine.classList.toggle("lien", !oeuvre && !!lien);
    racine.classList.toggle("texte", !oeuvre && !lien && !!texte);
    if (oeuvre) label.textContent = `${oeuvre.dataset.numero} / ${voir}`;
    const nouvelAimant = !oeuvre && lien && lien.matches("a, button") ? lien : null;
    if (nouvelAimant !== aimant) {
      relacher();
      aimant = nouvelAimant;
    }
  });

  let derniereCoord = "";
  const boucle = () => {
    const dx = souris.x - pos.x;
    const dy = souris.y - pos.y;
    pos.x += dx * 0.14;
    pos.y += dy * 0.14;

    // étirement plafonné dans la direction du mouvement
    // (pas d'étirement quand l'anneau porte un label, pour qu'il reste lisible)
    const libre = !racine.classList.contains("oeuvre");
    const vitesse = libre ? Math.min(Math.hypot(dx, dy) / 140, 0.28) : 0;
    const angle = vitesse ? Math.atan2(dy, dx) * (180 / Math.PI) : 0;
    point.style.transform = `translate3d(${souris.x}px, ${souris.y}px, 0)`;
    anneau.style.transform = `translate3d(${pos.x}px, ${pos.y}px, 0) rotate(${angle}deg) scale(${1 + vitesse}, ${1 - vitesse * 0.6})`;
    coords.style.transform = `translate3d(${pos.x + (libre ? 26 : 56)}px, ${pos.y + (libre ? 18 : 24)}px, 0)`;

    const texteCoords = `X ${String(Math.round(souris.x)).padStart(4, "0")} / Y ${String(Math.round(souris.y)).padStart(4, "0")}`;
    if (texteCoords !== derniereCoord) coords.textContent = derniereCoord = texteCoords;

    // effet magnétique : l'élément survolé glisse de 4 px au plus vers le curseur
    if (aimant) {
      const r = aimant.getBoundingClientRect();
      const mx = Math.max(-4, Math.min(4, (souris.x - (r.left + r.width / 2)) * 0.12));
      const my = Math.max(-4, Math.min(4, (souris.y - (r.top + r.height / 2)) * 0.12));
      aimant.style.translate = `${mx}px ${my}px`;
    }
    requestAnimationFrame(boucle);
  };
  requestAnimationFrame(boucle);
}
