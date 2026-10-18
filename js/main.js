// Menu mobile, filtres et visionneuse de la galerie.
document.addEventListener("DOMContentLoaded", () => {
  const bouton = document.querySelector(".menu-bouton");
  const nav = document.querySelector(".nav");
  if (bouton && nav) {
    bouton.addEventListener("click", () => {
      const ouvert = nav.classList.toggle("ouvert");
      bouton.setAttribute("aria-expanded", ouvert);
    });
  }

  const annee = document.getElementById("annee");
  if (annee) annee.textContent = new Date().getFullYear();

  // Filtres par prestation (attribut data-categorie sur chaque réalisation)
  const oeuvres = [...document.querySelectorAll(".galerie .oeuvre")];
  document.querySelectorAll(".filtres button").forEach((filtre) => {
    filtre.addEventListener("click", () => {
      document.querySelectorAll(".filtres button").forEach((b) => b.setAttribute("aria-pressed", b === filtre));
      const cat = filtre.dataset.filtre;
      oeuvres.forEach((o) => { o.hidden = cat !== "tout" && o.dataset.categorie !== cat; });
    });
  });

  // Filtre choisi par l'adresse, par exemple /realisations#enduits
  const depuisAdresse = document.querySelector(`.filtres button[data-filtre="${location.hash.slice(1)}"]`);
  if (depuisAdresse) depuisAdresse.click();

  // Visionneuse plein écran
  const vis = document.querySelector(".visionneuse");
  if (!vis || !oeuvres.length) return;
  const visImg = vis.querySelector("img");
  const visTexte = vis.querySelector("figcaption");
  let courant = 0;

  const visibles = () => oeuvres.filter((o) => !o.hidden && o.querySelector("img"));
  const afficher = (o) => {
    const img = o.querySelector("img");
    visImg.src = img.dataset.grande || img.src;
    visImg.alt = img.alt;
    visTexte.textContent = o.querySelector("figcaption").textContent.replace(/\s+/g, " ").trim();
  };
  const ouvrir = (o) => { courant = visibles().indexOf(o); afficher(o); vis.classList.add("ouverte"); };
  const fermer = () => vis.classList.remove("ouverte");
  const deplacer = (pas) => {
    const liste = visibles();
    courant = (courant + pas + liste.length) % liste.length;
    afficher(liste[courant]);
  };

  oeuvres.forEach((o) => o.addEventListener("click", () => { if (o.querySelector("img")) ouvrir(o); }));
  vis.querySelector(".fermer").addEventListener("click", fermer);
  vis.querySelector(".prec").addEventListener("click", () => deplacer(-1));
  vis.querySelector(".suiv").addEventListener("click", () => deplacer(1));
  vis.addEventListener("click", (e) => { if (e.target === vis) fermer(); });
  document.addEventListener("keydown", (e) => {
    if (!vis.classList.contains("ouverte")) return;
    if (e.key === "Escape") fermer();
    if (e.key === "ArrowLeft") deplacer(-1);
    if (e.key === "ArrowRight") deplacer(1);
  });
});
