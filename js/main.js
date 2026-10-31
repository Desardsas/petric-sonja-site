// Petric Sonja : menu, révélations, images, galerie, vue en grand, formulaire, thème clair / sombre et curseur pinceau.
// Aucune bibliothèque.

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
  theme();
  pinceau();
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

// Clair / sombre : le choix du visiteur est gardé dans ce navigateur (sinon, réglage du système)
function theme() {
  const bouton = document.querySelector(".theme-bouton");
  if (!bouton) return;
  const racine = document.documentElement;
  const actuel = () => racine.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "sombre" : "clair");
  const afficher = () => {
    const sombre = actuel() === "sombre";
    bouton.textContent = sombre ? bouton.dataset.clair : bouton.dataset.sombre;
    bouton.setAttribute("aria-pressed", sombre);
  };
  bouton.addEventListener("click", () => {
    racine.dataset.theme = actuel() === "sombre" ? "clair" : "sombre";
    try { localStorage.setItem("theme", racine.dataset.theme); } catch (e) {}
    afficher();
  });
  afficher();
}

// Curseur pinceau : le pointeur devient un pinceau (CSS) et laisse une courte traînée de peinture qui sèche en un instant.
// Souris uniquement (rien sur écran tactile). Si le mouvement réduit est demandé : pinceau sans traînée.
// Le canvas ne se redessine que pendant le geste ; au repos, aucune boucle ne tourne.
function pinceau() {
  if (!matchMedia("(hover: hover) and (pointer: fine)").matches) return;
  document.documentElement.classList.add("pinceau");
  if (mouvementReduit) return;

  const toile = document.createElement("canvas");
  toile.className = "trainee";
  toile.setAttribute("aria-hidden", "true");
  document.body.appendChild(toile);
  const ctx = toile.getContext("2d");

  const VIE = 520;       // durée de séchage d'une touche (ms)
  const LARGEUR = 10;     // largeur maximale du trait (px)
  const points = [];     // { x, y, t, l } : position, instant, largeur
  let couleur = "#A34A26";
  let enCours = false;
  let ratio = 1;

  const dimensionner = () => {
    ratio = Math.min(devicePixelRatio || 1, 2);
    toile.width = innerWidth * ratio;
    toile.height = innerHeight * ratio;
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  };
  dimensionner();
  addEventListener("resize", dimensionner, { passive: true });

  addEventListener("pointermove", (e) => {
    if (e.pointerType !== "mouse") return;
    const t = performance.now();
    const dernier = points[points.length - 1];
    if (!dernier || t - dernier.t > VIE) {
      // nouveau geste : on reprend la couleur d'accent du thème en cours
      couleur = getComputedStyle(document.documentElement).getPropertyValue("--accent").trim() || couleur;
      points.length = 0;
    } else if (Math.hypot(e.clientX - dernier.x, e.clientY - dernier.y) < 2) return;
    // plus le geste est rapide, plus le trait s'affine, comme un vrai pinceau
    const vitesse = dernier ? Math.hypot(e.clientX - dernier.x, e.clientY - dernier.y) / Math.max(t - dernier.t, 1) : 0;
    const l = LARGEUR * Math.max(0.45, 1 - vitesse * 0.15);
    points.push({ x: e.clientX, y: e.clientY, t, l: dernier ? dernier.l * 0.6 + l * 0.4 : l * 0.5 });
    if (points.length > 64) points.shift();
    if (!enCours) { enCours = true; requestAnimationFrame(dessiner); }
  }, { passive: true });

  function dessiner(maintenant) {
    ctx.clearRect(0, 0, innerWidth, innerHeight);
    while (points.length && maintenant - points[0].t > VIE) points.shift();
    if (!points.length) { enCours = false; return; }

    ctx.strokeStyle = couleur;
    const n = points.length;
    for (let i = 1; i < n; i++) {
      const a = points[i - 1];
      const b = points[i];
      const frais = 1 - (maintenant - b.t) / VIE;   // 1 = peinture fraîche, 0 = sèche
      const effile = Math.min(1, i / 6);            // la queue de la touche s'effile
      const largeur = b.l * effile * (0.55 + 0.45 * frais);
      // trait principal
      ctx.globalAlpha = 0.42 * frais;
      ctx.lineWidth = largeur;
      ctx.lineCap = "butt";
      ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      // deux poils plus secs sur les bords, pour la texture du pinceau
      const dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy) || 1;
      const nx = (-dy / d) * largeur * 0.45, ny = (dx / d) * largeur * 0.45;
      ctx.globalAlpha = 0.3 * frais;
      ctx.lineWidth = Math.max(0.6, largeur * 0.16);
      ctx.lineCap = "round";
      ctx.beginPath();
      ctx.moveTo(a.x + nx, a.y + ny); ctx.lineTo(b.x + nx, b.y + ny);
      ctx.moveTo(a.x - nx, a.y - ny); ctx.lineTo(b.x - nx, b.y - ny);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
    requestAnimationFrame(dessiner);
  }
}
