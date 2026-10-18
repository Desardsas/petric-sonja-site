# Refonte design du site de Sonja Petric : audit et note d'intention

À valider avant de coder.

## Contexte retenu (rempli à partir du projet)

- **Site** : vitrine de Sonja Petric, artiste peintre à Cannes. Peinture, restauration de tableaux, enduits décoratifs sur mesure, home staging, sur toute la Côte d'Azur.
- **Stack** : HTML, CSS et JavaScript statiques, sans framework. Les pages sont générées par `generer.py` et hébergées sur Vercel (projet `petric-sonja-site`, domaine petricsonja.art).
- **Pages** : Accueil, Prestations, Réalisations, À propos, Contact, en français et en anglais (`/en`).
- **À ne pas changer** : les textes, les 5 pages et leur contenu, le bilinguisme FR / EN, le formulaire de devis (Web3Forms, anti-spam, message de confirmation), la protection par mot de passe tant que le site n'est pas public, l'e-mail et l'Instagram. Rien ne touche au projet Desard Yachting.

## 1. Audit du design actuel

**Ce qui fonctionne**
- La structure est claire : le chemin « arriver → voir les réalisations → demander un devis » se fait en deux clics.
- La galerie a déjà une vue en grand avec les flèches du clavier et Échap.
- Le site est léger : aucune bibliothèque, un seul fichier CSS et un seul fichier JS.
- Le portrait noir et blanc et l'avant / après de restauration sont des images fortes, faites pour un fond sombre.

**Ce qui fait « template » ou bon marché**
- Le fond crème, le titre en serif classique (Cormorant) et l'accent terre de Sienne donnent un aspect « blog déco » générique.
- Les boutons de filtre en pilule (coins très arrondis) et les cartes de prestations qui se soulèvent au survol sont des codes de startup.
- L'en-tête translucide flouté (backdrop-blur) relève du glassmorphism.
- Les cadres d'attente en dégradé beige sont décoratifs.
- La mise en page est symétrique et prévisible : image à droite, texte à gauche, grille de 3 cartes identiques.
- L'icône ☰ sert de menu sur mobile.

**Ce qui contredit la direction artistique**
- Les images sont recadrées de force au format 4/5 dans la galerie, ce qui coupe les œuvres (sauf l'avant / après).
- Il n'y a ni numérotation ni cartel : le titre et les détails sont en texte courant.
- Il n'y a pas de style de focus clavier dédié ni de gestion de `prefers-reduced-motion`.
- Les images sont en JPEG seul, sans tailles adaptées (`srcset`), et les polices ne sont pas préchargées.

## 2. Note d'intention

**Palette** : les tokens du brief à l'identique (`--bg` #0E0E0E, `--bg-elevated` #161616, `--surface` #1E1E1E, `--line` #2A2A2A, `--text` #E6E4E0, `--text-muted` #8C8A86, `--text-faint` #4E4D4A), avec un grain SVG à 4 % sur tout le site.
- Contrastes mesurés : `--text` sur `--bg` 15,2 : 1 et `--text-muted` sur `--bg` 5,6 : 1, conformes AA. `--text-faint` n'atteint que 2,3 : 1 : il est réservé aux éléments décoratifs (numéros de section, coordonnées), jamais à une information utile.
- Accent : à choisir (question en carte).

**Typographie** : Inter Tight pour les titres et le texte, JetBrains Mono pour les cartels, les numéros et la navigation. Les deux sont gratuites et hébergées sur le site (sous-ensemble latin, `font-display: swap`, préchargées), sans appel à Google Fonts. Les titres sont très grands, avec un interlignage de 0,95 et un approche de −0,03 em. L'échelle est fluide avec `clamp()`.

**Grille** : 12 colonnes, marges latérales de 6 vw, filets de 1 px pour structurer chaque section comme une planche de catalogue. Les sections sont numérotées en mono (001 Prestations, 002 Réalisations…). La mise en page est asymétrique : le portrait d'accueil est décalé sur les colonnes 7 à 12, le nom est composé très grand sur les colonnes 1 à 8, et les réalisations alternent les largeurs.

**Œuvres** : aucune image recadrée, chacune est affichée dans ses proportions réelles. Un cartel en mono accompagne chaque image (numéro, titre, prestation, détails). La vue en grand se fait sur fond `--bg`, avec un compteur « 002 / 006 », les flèches, Échap et un fondu entre les images. Les images sont servies en AVIF et WebP en plusieurs tailles, chargées progressivement avec un fondu depuis leur couleur dominante.

**Curseur** : un point de 6 px et un anneau de 32 px en inertie (facteur 0,14), en `mix-blend-mode: difference`, avec un léger étirement selon la vitesse.
- Sur un lien, l'anneau grossit et attire l'élément de 4 px au plus. Sur une œuvre, il affiche « 002 / VOIR ». Sur du texte, il devient une barre fine. Au clic, il se contracte.
- Tout tourne dans une seule boucle `requestAnimationFrame`, et seuls `transform` et `opacity` sont animés.
- Le curseur est désactivé sur écran tactile et avec `prefers-reduced-motion`.
- Les coordonnées X/Y sont une option (question en carte).
- Je déconseille le décalage RGB en WebGL : pour un site de restauratrice, déformer l'œuvre envoie le mauvais message, et cela ajoute du poids pour peu d'effet.

**Mouvement** : courbe `cubic-bezier(0.16, 1, 0.3, 1)`, de 500 à 900 ms.
- Les titres sont révélés par un masque au défilement, une seule fois (IntersectionObserver).
- Au survol, les images montent à l'échelle 1,02 et un soulignement de 1 px se dessine sous les liens.
- Les transitions entre pages utilisent un fondu natif du navigateur (View Transitions), sans bibliothèque.
- Pas de Lenis ni de GSAP : le défilement natif reste le plus accessible, et tout tient en environ 6 Ko de JavaScript.

**Navigation** : le menu typographique est en mono, avec la page courante indiquée en numéro (« 03 Réalisations ») et le sélecteur FR / EN conservé. Sur mobile, le mot « MENU » ouvre un panneau plein écran sombre. Le pied de page est brut : un filet, l'e-mail, l'Instagram, Cannes et l'année, en mono.

**Accessibilité et performance** : focus visible partout (contour de 1 px `--text`, décalé de 3 px), navigation complète au clavier, textes alternatifs, et respect total de `prefers-reduced-motion`. Objectif : 60 fps et aucune bibliothèque externe.

**Points à signaler**
- Les filtres de la page Réalisations passent de pilules à des onglets texte soulignés. C'est un changement de style uniquement : la fonction ne change pas.
- Le formulaire de devis passe en champs à filet bas, sans cadres. Les champs et l'envoi ne changent pas.
- Un site très sombre et « galerie » convient aux tableaux. Pour les enduits et le home staging, les photos d'intérieurs chaleureux ressortiront fortement sur le noir, ce qui est un atout.
