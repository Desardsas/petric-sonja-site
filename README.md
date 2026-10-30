# Petric Sonja — site vitrine

Site statique en HTML, CSS et un peu de JavaScript, sans framework ni étape de compilation. Il se déploie tel quel sur Vercel (ou tout autre hébergeur).

## Site privé (au besoin)

Pour remettre un mot de passe avant chaque page, restaurer `middleware.js` depuis l'historique git (`git checkout <commit>~1 -- middleware.js`, voir le commit « Site public ») et définir `SITE_PASSWORD` dans Vercel.

## Design

Direction « brutalisme méditerranéen » : palette claire « Chaux & Terre » (chaux, pierre, béton, encre, terre cuite en seul accent, olive en aplat rare) avec une variante sombre « Nuit d'été » qui suit le réglage du système ou le bouton Clair / Sombre de l'en-tête. Radius 0, filets de 1 px, aucune ombre, grille de 12 colonnes, grain de chaux derrière le contenu (jamais sur les photos).

Polices hébergées dans `fonts/` (licence SIL OFL), latin étendu chargé seulement si besoin (č, ć, š, ž) : Cormorant Garamond pour les titres, Inter Tight pour le texte courant et le nom, IBM Plex Mono pour les données, la navigation, les cartels et les boutons. Les couleurs, polices, tailles et durées sont des variables en haut de `css/style.css`.

Les révélations au défilement, la vue en grand, le formulaire et le thème sont dans `js/main.js`, sans bibliothèque. Les mouvements durent 150 à 250 ms ; quand le visiteur demande moins d'animations, tout s'affiche sans mouvement.

`generer.py` crée pour chaque image des versions AVIF et WebP en 640, 1024 et 1600 px dans `images/_gen/` (il faut Pillow : `pip install pillow`).

L'audit et la note d'intention de la refonte sont dans `docs/`.

## Pages et langues

Cinq pages en français à la racine (`index`, `prestations`, `realisations`, `a-propos`, `contact`) et leur version anglaise dans `en/`. Un lien FR / EN en haut de chaque page mène à la même page dans l'autre langue. L'ancienne adresse `/galerie` redirige vers `/realisations` (`vercel.json`).

Ces fichiers HTML sont **générés** par `generer.py` : on ne les modifie pas à la main. Coordonnées, prestations, réalisations, parcours et tous les textes sont en haut de `generer.py`. Après une modification :

```sh
python3 generer.py
```

puis commit des fichiers `.html` mis à jour. Les textes entre crochets `[...]` sont à remplacer par le vrai contenu.

## Pages légales, référencement

`confidentialite` est générée dans chaque langue et liée depuis le pied de page et le formulaire. `mentions-legales` n'est générée qu'une fois `SIRET` rempli en haut de `generer.py` (avec `STATUT` et `ADRESSE`), car le SIRET y est obligatoire. Leurs textes sont dans `LEGAL`.

`generer.py` écrit aussi `sitemap.xml` et `robots.txt`, ajoute à chaque page un lien canonique, les `hreflang` absolus (avec `x-default`) et l'image de partage, et place les données structurées (JSON-LD) sur l'accueil. L'adresse publique est `SITE`.

## Ajouter une réalisation

1. Déposer la photo dans `images/realisations/` (JPEG, 1600 px de large maximum, nom sans espace, par exemple `salon-tadelakt.jpg`).
2. Dans `generer.py`, ajouter une entrée à `REALISATIONS` avec `"image": "salon-tadelakt.jpg"`, la prestation concernée (un `id` de `PRESTATIONS`), son titre et ses détails dans chaque langue. Les trois premières apparaissent sur l'accueil.
3. Lancer `python3 generer.py`.

Un lien vers `/realisations#enduits` ouvre la page déjà filtrée sur une prestation.

## Formulaire de devis

Le formulaire de la page Contact envoie chaque demande par e-mail grâce à [Web3Forms](https://web3forms.com) (gratuit jusqu'à 250 demandes par mois). Le visiteur reste sur la page et voit un message de confirmation ; un champ invisible bloque les robots.

Pour l'activer : sur web3forms.com, saisir l'adresse e-mail qui doit recevoir les demandes, récupérer la clé (Access Key) reçue par e-mail, la mettre dans `CLE_FORMULAIRE` en haut de `generer.py`, puis lancer `python3 generer.py`. Cette clé est publique par conception : elle peut figurer dans le code. Tant qu'elle est vide, le formulaire affiche l'adresse e-mail à la place. Pour passer à Formspree, mettre `SERVICE_FORMULAIRE = "formspree"` et l'identifiant du formulaire dans `CLE_FORMULAIRE`.

## Voir le site en local

```sh
npx serve .   # puis ouvrir l'adresse affichée (gère les adresses sans .html, comme Vercel)
```

## Mise en ligne sur Vercel

1. Sur vercel.com, *Add New → Project*, importer ce dépôt GitHub. Framework : *Other*, sans commande de build ni dossier de sortie.
2. Chaque push sur `main` met le site à jour automatiquement.
3. Domaine : *Settings → Domains*, ajouter le domaine, puis chez le registraire créer les enregistrements DNS indiqués par Vercel (en général un `A` vers `76.76.21.21` pour le domaine nu et un `CNAME` vers `cname.vercel-dns.com` pour `www`). Le certificat HTTPS est automatique.
