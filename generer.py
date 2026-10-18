"""Génère les pages HTML du site dans chaque langue.

Les textes sont dans TEXTES et les œuvres dans OEUVRES, plus bas.
Après une modification : python3 generer.py, puis commit des fichiers .html.
Le français est à la racine du site, chaque autre langue dans son dossier (en/, ...).
"""
from html import escape
from pathlib import Path

RACINE = Path(__file__).parent
LANGUES = ["fr", "en"]  # la première est la langue par défaut, à la racine
EMAIL = "contact@exemple.fr"
INSTAGRAM = "https://www.instagram.com/"
FORMSPREE_ID = "VOTRE_ID"

# Chaque œuvre : fichier image dans images/oeuvres/ (None tant qu'il n'y a pas de photo),
# catégorie (clé de CATEGORIES), titre et détails dans chaque langue.
OEUVRES = [
    {"image": None, "categorie": "peinture", "titre": {"fr": "[Titre 1]", "en": "[Title 1]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "categorie": "peinture", "titre": {"fr": "[Titre 2]", "en": "[Title 2]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "categorie": "dessin", "titre": {"fr": "[Titre 3]", "en": "[Title 3]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "categorie": "sculpture", "titre": {"fr": "[Titre 4]", "en": "[Title 4]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "categorie": "peinture", "titre": {"fr": "[Titre 5]", "en": "[Title 5]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "categorie": "dessin", "titre": {"fr": "[Titre 6]", "en": "[Title 6]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
]
CATEGORIES = {
    "peinture": {"fr": "Peinture", "en": "Painting"},
    "dessin": {"fr": "Dessin", "en": "Drawing"},
    "sculpture": {"fr": "Sculpture", "en": "Sculpture"},
}

EXPOSITIONS = [
    {"annee": "[Année]", "fr": "[Nom de l'exposition, lieu]", "en": "[Exhibition name, venue]"},
    {"annee": "[Année]", "fr": "[Nom de l'exposition, lieu]", "en": "[Exhibition name, venue]"},
    {"annee": "[Année]", "fr": "[Nom de l'exposition, lieu]", "en": "[Exhibition name, venue]"},
]

TEXTES = {
    "fr": {
        "nom_langue": "Français",
        "description": "Sonja Petric, création artistique : œuvres, démarche et contact.",
        "nav": {"index": "Accueil", "galerie": "Galerie", "a-propos": "À propos", "contact": "Contact"},
        "titres": {"index": "Sonja Petric · Création artistique", "galerie": "Galerie · Sonja Petric", "a-propos": "À propos · Sonja Petric", "contact": "Contact · Sonja Petric"},
        "menu": "Menu",
        "droits": "Tous droits réservés.",
        "surtitre": "Création artistique",
        "accroche": "[Une phrase qui présente sa démarche : ce qu'elle crée, avec quelles matières, ce qui l'inspire.]",
        "voir_oeuvres": "Voir les œuvres",
        "me_contacter": "Me contacter",
        "photo_principale": "Photo principale",
        "oeuvres_recentes": "Œuvres récentes",
        "toute_galerie": "Toute la galerie →",
        "oeuvre": "Œuvre",
        "demarche": "Démarche",
        "demarche_titre": "[Titre court sur sa démarche]",
        "demarche_texte": "[Deux ou trois phrases sur ce qui guide son travail.]",
        "en_savoir_plus": "En savoir plus",
        "galerie": "Galerie",
        "filtrer": "Filtrer par catégorie",
        "tout": "Tout",
        "vue_grand": "Œuvre en grand",
        "fermer": "Fermer",
        "precedente": "Œuvre précédente",
        "suivante": "Œuvre suivante",
        "a_propos": "À propos",
        "portrait": "Portrait",
        "bio": "[Sa biographie : son parcours, sa formation, son atelier, ce qui l'a menée à la création.]",
        "bio_demarche": "[Sa démarche artistique : thèmes, matières, techniques.]",
        "expositions": "Expositions",
        "contact": "Contact",
        "ecrivez": "Écrivez-moi",
        "contact_intro": "Pour une commande, une acquisition, une exposition ou simplement un échange.",
        "email": "E-mail",
        "atelier": "Atelier : [Ville]",
        "nom": "Nom",
        "message": "Message",
        "envoyer": "Envoyer",
    },
    "en": {
        "nom_langue": "English",
        "description": "Sonja Petric, artist: artworks, approach and contact.",
        "nav": {"index": "Home", "galerie": "Gallery", "a-propos": "About", "contact": "Contact"},
        "titres": {"index": "Sonja Petric · Artist", "galerie": "Gallery · Sonja Petric", "a-propos": "About · Sonja Petric", "contact": "Contact · Sonja Petric"},
        "menu": "Menu",
        "droits": "All rights reserved.",
        "surtitre": "Artist",
        "accroche": "[One sentence introducing her work: what she creates, with which materials, what inspires her.]",
        "voir_oeuvres": "See the works",
        "me_contacter": "Get in touch",
        "photo_principale": "Main photo",
        "oeuvres_recentes": "Recent works",
        "toute_galerie": "Full gallery →",
        "oeuvre": "Work",
        "demarche": "Approach",
        "demarche_titre": "[Short title about her approach]",
        "demarche_texte": "[Two or three sentences about what drives her work.]",
        "en_savoir_plus": "Learn more",
        "galerie": "Gallery",
        "filtrer": "Filter by category",
        "tout": "All",
        "vue_grand": "Enlarged artwork",
        "fermer": "Close",
        "precedente": "Previous work",
        "suivante": "Next work",
        "a_propos": "About",
        "portrait": "Portrait",
        "bio": "[Her biography: background, training, studio, what led her to create.]",
        "bio_demarche": "[Her artistic approach: themes, materials, techniques.]",
        "expositions": "Exhibitions",
        "contact": "Contact",
        "ecrivez": "Write to me",
        "contact_intro": "For a commission, a purchase, an exhibition or simply a conversation.",
        "email": "Email",
        "atelier": "Studio: [City]",
        "nom": "Name",
        "message": "Message",
        "envoyer": "Send",
    },
}

PAGES = ["index", "galerie", "a-propos", "contact"]


def chemin(langue, page):
    """Adresse d'une page depuis la racine du site, sans .html (cleanUrls de Vercel)."""
    if langue == LANGUES[0]:
        return "/" if page == "index" else f"/{page}"
    return f"/{langue}" if page == "index" else f"/{langue}/{page}"


def figure(o, n, t, langue):
    if o["image"]:
        visuel = f'<img src="/images/oeuvres/{o["image"]}" alt="{escape(o["titre"][langue])}" loading="lazy">'
    else:
        visuel = f'<div class="attente">{t["oeuvre"]} {n}</div>'
    return f'''        <figure class="oeuvre" data-categorie="{o["categorie"]}">
          <div class="cadre">{visuel}</div>
          <figcaption><div class="nom">{escape(o["titre"][langue])}</div><div class="details">{escape(o["details"][langue])}</div></figcaption>
        </figure>'''


def corps_index(t, langue):
    recentes = "\n".join(figure(o, n, t, langue) for n, o in enumerate(OEUVRES[:3], 1))
    return f'''    <section class="conteneur hero">
      <div>
        <p class="surtitre">{t["surtitre"]}</p>
        <h1>Sonja Petric</h1>
        <p>{t["accroche"]}</p>
        <p style="margin-top:28px"><a class="bouton plein" href="{chemin(langue, "galerie")}">{t["voir_oeuvres"]}</a> &nbsp; <a class="bouton" href="{chemin(langue, "contact")}">{t["me_contacter"]}</a></p>
      </div>
      <div class="hero-image"><div class="attente">{t["photo_principale"]}</div></div>
    </section>

    <section class="section" style="background:var(--surface)">
      <div class="conteneur">
        <div class="section-titre">
          <h2>{t["oeuvres_recentes"]}</h2>
          <a href="{chemin(langue, "galerie")}">{t["toute_galerie"]}</a>
        </div>
        <div class="galerie">
{recentes}
        </div>
      </div>
    </section>

    <section class="section conteneur" style="text-align:center;max-width:720px">
      <p class="surtitre">{t["demarche"]}</p>
      <h2>{t["demarche_titre"]}</h2>
      <p style="color:var(--texte-doux)">{t["demarche_texte"]}</p>
      <p><a class="bouton" href="{chemin(langue, "a-propos")}">{t["en_savoir_plus"]}</a></p>
    </section>'''


def corps_galerie(t, langue):
    filtres = "\n".join(f'        <button data-filtre="{c}" aria-pressed="false">{noms[langue]}</button>' for c, noms in CATEGORIES.items())
    oeuvres = "\n".join(figure(o, n, t, langue) for n, o in enumerate(OEUVRES, 1))
    return f'''    <section class="section conteneur">
      <div class="section-titre"><h1>{t["galerie"]}</h1></div>
      <div class="filtres" role="group" aria-label="{t["filtrer"]}">
        <button data-filtre="tout" aria-pressed="true">{t["tout"]}</button>
{filtres}
      </div>
      <div class="galerie">
{oeuvres}
      </div>
    </section>'''


def visionneuse(t):
    return f'''
  <div class="visionneuse" role="dialog" aria-modal="true" aria-label="{t["vue_grand"]}">
    <button class="fermer" aria-label="{t["fermer"]}">×</button>
    <button class="prec" aria-label="{t["precedente"]}">‹</button>
    <figure><img src="" alt=""><figcaption></figcaption></figure>
    <button class="suiv" aria-label="{t["suivante"]}">›</button>
  </div>
'''


def corps_a_propos(t, langue):
    expos = "\n".join(f'          <li><span class="annee">{e["annee"]}</span><span>{e[langue]}</span></li>' for e in EXPOSITIONS)
    return f'''    <section class="section conteneur apropos">
      <div class="portrait"><div class="attente">{t["portrait"]}</div></div>
      <div>
        <p class="surtitre">{t["a_propos"]}</p>
        <h1>Sonja Petric</h1>
        <p>{t["bio"]}</p>
        <p>{t["bio_demarche"]}</p>
        <h2 style="margin-top:40px;font-size:1.8rem">{t["expositions"]}</h2>
        <ul class="parcours">
{expos}
        </ul>
      </div>
    </section>'''


def corps_contact(t, langue):
    return f'''    <section class="section conteneur contact">
      <div class="coordonnees">
        <p class="surtitre">{t["contact"]}</p>
        <h1>{t["ecrivez"]}</h1>
        <p>{t["contact_intro"]}</p>
        <p>{t["email"]} : <a href="mailto:{EMAIL}">{EMAIL}</a><br>
           Instagram : <a href="{INSTAGRAM}" rel="noopener">@[compte]</a><br>
           {t["atelier"]}</p>
      </div>
      <form class="formulaire" action="https://formspree.io/f/{FORMSPREE_ID}" method="POST">
        <label>{t["nom"]}<input name="nom" required autocomplete="name"></label>
        <label>{t["email"]}<input type="email" name="email" required autocomplete="email"></label>
        <label>{t["message"]}<textarea name="message" required></textarea></label>
        <div><button class="bouton plein" type="submit">{t["envoyer"]}</button></div>
      </form>
    </section>'''


CORPS = {"index": corps_index, "galerie": corps_galerie, "a-propos": corps_a_propos, "contact": corps_contact}


def page(langue, nom):
    t = TEXTES[langue]
    nav = "\n".join(
        f'        <a href="{chemin(langue, p)}"{" aria-current=\"page\"" if p == nom else ""}>{t["nav"][p]}</a>' for p in PAGES
    )
    langues = " ".join(
        f'<a href="{chemin(l, nom)}" lang="{l}" hreflang="{l}"{" aria-current=\"true\"" if l == langue else ""}>{l.upper()}</a>' for l in LANGUES
    )
    alternates = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{chemin(l, nom)}">' for l in LANGUES)
    extra = visionneuse(t) if nom == "galerie" else ""
    return f'''<!doctype html>
<html lang="{langue}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t["titres"][nom]}</title>
  <meta name="description" content="{t["description"]}">
  <meta property="og:title" content="{t["titres"][nom]}">
  <meta property="og:description" content="{t["description"]}">
  <meta property="og:type" content="website">
{alternates}
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Inter:wght@400;500&display=swap">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <header class="entete">
    <div class="conteneur">
      <a class="logo" href="{chemin(langue, "index")}">Sonja Petric</a>
      <div class="entete-droite">
        <nav class="nav">
{nav}
        </nav>
        <div class="langues">{langues}</div>
        <button class="menu-bouton" aria-label="{t["menu"]}" aria-expanded="false">☰</button>
      </div>
    </div>
  </header>

  <main>
{CORPS[nom](t, langue)}
  </main>
{extra}
  <footer class="pied">
    <div class="conteneur">
      <span>© <span id="annee"></span> Sonja Petric. {t["droits"]}</span>
      <span><a href="{INSTAGRAM}" rel="noopener">Instagram</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>
'''


if __name__ == "__main__":
    for langue in LANGUES:
        dossier = RACINE if langue == LANGUES[0] else RACINE / langue
        dossier.mkdir(exist_ok=True)
        for nom in PAGES:
            (dossier / f"{nom}.html").write_text(page(langue, nom), encoding="utf-8")
            print(f"{dossier.relative_to(RACINE) / (nom + '.html')}")
