# Sonja Petric — site vitrine

Site statique en HTML, CSS et un peu de JavaScript, sans framework ni étape de compilation. Il se déploie tel quel sur Vercel (ou tout autre hébergeur).

## Pages

- `index.html` : accueil
- `galerie.html` : galerie des œuvres, avec filtres par catégorie et vue en grand
- `a-propos.html` : biographie, démarche, expositions
- `contact.html` : coordonnées et formulaire

Les textes entre crochets `[...]` sont à remplacer par le vrai contenu.

## Ajouter une œuvre

1. Déposer la photo dans `images/oeuvres/` (JPEG, 1600 px de large maximum, nom sans espace, par exemple `jardin-bleu.jpg`).
2. Dans `galerie.html`, copier un bloc `<figure class="oeuvre">` et remplacer `<div class="attente">…</div>` par :

```html
<img src="images/oeuvres/jardin-bleu.jpg" alt="Jardin bleu, huile sur toile" loading="lazy">
```

3. Mettre la catégorie dans `data-categorie` (`peinture`, `dessin`, `sculpture` ; les boutons de filtre sont en haut de la page).

## Formulaire de contact

Le formulaire passe par [Formspree](https://formspree.io) (gratuit jusqu'à 50 messages par mois) : créer un formulaire, puis remplacer `VOTRE_ID` dans `contact.html` par son identifiant. Les messages arrivent par e-mail.

## Voir le site en local

```sh
python3 -m http.server 8000   # puis ouvrir http://localhost:8000
```

## Mise en ligne sur Vercel

1. Sur vercel.com, *Add New → Project*, importer ce dépôt GitHub. Framework : *Other*, sans commande de build ni dossier de sortie.
2. Chaque push sur `main` met le site à jour automatiquement.
3. Domaine : *Settings → Domains*, ajouter le domaine, puis chez le registraire créer les enregistrements DNS indiqués par Vercel (en général un `A` vers `76.76.21.21` pour le domaine nu et un `CNAME` vers `cname.vercel-dns.com` pour `www`). Le certificat HTTPS est automatique.
