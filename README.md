# Sonja Petric — site vitrine

Site statique en HTML, CSS et un peu de JavaScript, sans framework ni étape de compilation. Il se déploie tel quel sur Vercel (ou tout autre hébergeur).

## Pages et langues

Cinq pages en français à la racine (`index`, `prestations`, `realisations`, `a-propos`, `contact`) et leur version anglaise dans `en/`. Un lien FR / EN en haut de chaque page mène à la même page dans l'autre langue. L'ancienne adresse `/galerie` redirige vers `/realisations` (`vercel.json`).

Ces fichiers HTML sont **générés** par `generer.py` : on ne les modifie pas à la main. Coordonnées, prestations, réalisations, parcours et tous les textes sont en haut de `generer.py`. Après une modification :

```sh
python3 generer.py
```

puis commit des fichiers `.html` mis à jour. Les textes entre crochets `[...]` sont à remplacer par le vrai contenu.

## Ajouter une réalisation

1. Déposer la photo dans `images/realisations/` (JPEG, 1600 px de large maximum, nom sans espace, par exemple `salon-tadelakt.jpg`).
2. Dans `generer.py`, ajouter une entrée à `REALISATIONS` avec `"image": "salon-tadelakt.jpg"`, la prestation concernée (un `id` de `PRESTATIONS`), son titre et ses détails dans chaque langue. Les trois premières apparaissent sur l'accueil.
3. Lancer `python3 generer.py`.

Un lien vers `/realisations#enduits` ouvre la page déjà filtrée sur une prestation.

## Formulaire de contact

Le formulaire passe par [Formspree](https://formspree.io) (gratuit jusqu'à 50 messages par mois) : créer un formulaire, puis remplacer `VOTRE_ID` dans `generer.py` (`FORMSPREE_ID`) par son identifiant. Les messages arrivent par e-mail.

## Voir le site en local

```sh
npx serve .   # puis ouvrir l'adresse affichée (gère les adresses sans .html, comme Vercel)
```

## Mise en ligne sur Vercel

1. Sur vercel.com, *Add New → Project*, importer ce dépôt GitHub. Framework : *Other*, sans commande de build ni dossier de sortie.
2. Chaque push sur `main` met le site à jour automatiquement.
3. Domaine : *Settings → Domains*, ajouter le domaine, puis chez le registraire créer les enregistrements DNS indiqués par Vercel (en général un `A` vers `76.76.21.21` pour le domaine nu et un `CNAME` vers `cname.vercel-dns.com` pour `www`). Le certificat HTTPS est automatique.
