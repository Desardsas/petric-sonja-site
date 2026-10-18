"""Génère les pages HTML du site dans chaque langue.

Tout le contenu est dans ce fichier : coordonnées, PRESTATIONS, REALISATIONS, PARCOURS et TEXTES.
Après une modification : python3 generer.py, puis commit des fichiers .html.
Le français est à la racine du site, chaque autre langue dans son dossier (en/, ...).
"""
from html import escape
from pathlib import Path

RACINE = Path(__file__).parent
LANGUES = ["fr", "en"]  # la première est la langue par défaut, à la racine
EMAIL = "contact@exemple.fr"
TELEPHONE = ""  # par exemple "+33 6 12 34 56 78" ; vide = non affiché
INSTAGRAM = "https://www.instagram.com/"
FORMSPREE_ID = "VOTRE_ID"

# Les services, dans l'ordre d'affichage. L'identifiant sert aussi de catégorie aux réalisations.
PRESTATIONS = [
    {
        "id": "peinture",
        "titre": {"fr": "Peinture", "en": "Painting"},
        "resume": {"fr": "[Une phrase : tableaux, toiles sur commande, fresques…]", "en": "[One sentence: paintings, commissioned canvases, murals…]"},
        "points": {
            "fr": ["[Exemple de ce qu'elle propose]", "[Exemple]", "[Exemple]"],
            "en": ["[Example of what she offers]", "[Example]", "[Example]"],
        },
    },
    {
        "id": "restauration",
        "titre": {"fr": "Restauration de peinture", "en": "Painting restoration"},
        "resume": {"fr": "[Une phrase : quels types de peintures elle restaure et comment.]", "en": "[One sentence: which paintings she restores and how.]"},
        "points": {
            "fr": ["[Exemple]", "[Exemple]", "[Exemple]"],
            "en": ["[Example]", "[Example]", "[Example]"],
        },
    },
    {
        "id": "enduits",
        "titre": {"fr": "Enduits décoratifs sur mesure", "en": "Bespoke decorative plaster"},
        "resume": {"fr": "[Une phrase : finitions, matières, pièces concernées.]", "en": "[One sentence: finishes, materials, rooms.]"},
        "points": {
            "fr": ["[Exemple : tadelakt, chaux, béton ciré…]", "[Exemple]", "[Exemple]"],
            "en": ["[Example: tadelakt, lime, polished concrete…]", "[Example]", "[Example]"],
        },
    },
    {
        "id": "home-staging",
        "titre": {"fr": "Home staging", "en": "Home staging"},
        "resume": {"fr": "[Une phrase : valoriser un bien pour la vente ou la location.]", "en": "[One sentence: enhancing a property for sale or rent.]"},
        "points": {
            "fr": ["[Exemple]", "[Exemple]", "[Exemple]"],
            "en": ["[Example]", "[Example]", "[Example]"],
        },
    },
]

# Chaque réalisation : fichier image dans images/realisations/ (None tant qu'il n'y a pas de photo),
# prestation (un "id" de PRESTATIONS), titre et détails dans chaque langue.
# Les trois premières apparaissent sur l'accueil.
REALISATIONS = [
    {"image": None, "prestation": "peinture", "titre": {"fr": "[Titre]", "en": "[Title]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "prestation": "enduits", "titre": {"fr": "[Titre]", "en": "[Title]"}, "details": {"fr": "[Pièce, matière, ville]", "en": "[Room, material, town]"}},
    {"image": None, "prestation": "restauration", "titre": {"fr": "[Titre]", "en": "[Title]"}, "details": {"fr": "[Œuvre restaurée, année]", "en": "[Restored work, year]"}},
    {"image": None, "prestation": "home-staging", "titre": {"fr": "[Titre]", "en": "[Title]"}, "details": {"fr": "[Type de bien, ville]", "en": "[Property type, town]"}},
    {"image": None, "prestation": "peinture", "titre": {"fr": "[Titre]", "en": "[Title]"}, "details": {"fr": "[Technique, dimensions, année]", "en": "[Medium, size, year]"}},
    {"image": None, "prestation": "enduits", "titre": {"fr": "[Titre]", "en": "[Title]"}, "details": {"fr": "[Pièce, matière, ville]", "en": "[Room, material, town]"}},
]

PARCOURS = [
    {"annee": "[Année]", "fr": "[Formation, expérience ou exposition]", "en": "[Training, experience or exhibition]"},
    {"annee": "[Année]", "fr": "[Formation, expérience ou exposition]", "en": "[Training, experience or exhibition]"},
    {"annee": "[Année]", "fr": "[Formation, expérience ou exposition]", "en": "[Training, experience or exhibition]"},
]

TEXTES = {
    "fr": {
        "description": "Sonja Petric, Cannes : peinture, restauration de peinture, enduits décoratifs sur mesure et home staging sur toute la Côte d'Azur.",
        "nav": {"index": "Accueil", "prestations": "Prestations", "realisations": "Réalisations", "a-propos": "À propos", "contact": "Contact"},
        "titres": {
            "index": "Sonja Petric · Peinture, enduits décoratifs, home staging à Cannes",
            "prestations": "Prestations · Sonja Petric",
            "realisations": "Réalisations · Sonja Petric",
            "a-propos": "À propos · Sonja Petric",
            "contact": "Contact et devis · Sonja Petric",
        },
        "menu": "Menu",
        "droits": "Tous droits réservés.",
        "surtitre": "Peinture · Restauration · Enduits décoratifs · Home staging",
        "accroche": "[Une phrase qui la présente : ce qu'elle fait, pour qui, et ce qui rend son travail unique.]",
        "voir_prestations": "Mes prestations",
        "devis": "Demander un devis",
        "photo_principale": "Photo principale",
        "prestations": "Prestations",
        "prestations_intro": "[Une phrase d'introduction : sur mesure, à l'écoute, du conseil à la réalisation.]",
        "en_savoir_plus": "En savoir plus →",
        "realisations": "Réalisations",
        "realisations_recentes": "Réalisations récentes",
        "toutes_realisations": "Toutes les réalisations →",
        "photo": "Photo",
        "cta_titre": "Un projet en tête ?",
        "cta_texte": "Décrivez-le-moi en quelques lignes : je vous réponds avec une proposition et un devis.",
        "filtrer": "Filtrer par prestation",
        "tout": "Tout",
        "vue_grand": "Réalisation en grand",
        "fermer": "Fermer",
        "precedente": "Précédente",
        "suivante": "Suivante",
        "a_propos": "À propos",
        "portrait": "Portrait",
        "bio": "[Sa biographie : son parcours, sa formation, ce qui l'a menée à la peinture et à la décoration.]",
        "bio_demarche": "[Sa façon de travailler : écoute, matières, sur mesure.]",
        "parcours": "Parcours",
        "zone": "Atelier à Cannes. Intervient sur toute la Côte d'Azur : Cannes, Antibes, Nice, Grasse, Saint-Tropez et alentours.",
        "contact": "Contact",
        "ecrivez": "Parlons de votre projet",
        "contact_intro": "Pour un devis, une commande ou une simple question, écrivez-moi : je réponds rapidement.",
        "email": "E-mail",
        "telephone": "Téléphone",
        "nom": "Nom",
        "type_projet": "Prestation souhaitée",
        "autre": "Autre",
        "message": "Votre projet (lieu, surface, délai…)",
        "envoyer": "Envoyer la demande",
    },
    "en": {
        "description": "Sonja Petric, Cannes: painting, painting restoration, bespoke decorative plaster and home staging across the French Riviera.",
        "nav": {"index": "Home", "prestations": "Services", "realisations": "Projects", "a-propos": "About", "contact": "Contact"},
        "titres": {
            "index": "Sonja Petric · Painting, decorative plaster, home staging in Cannes",
            "prestations": "Services · Sonja Petric",
            "realisations": "Projects · Sonja Petric",
            "a-propos": "About · Sonja Petric",
            "contact": "Contact and quotes · Sonja Petric",
        },
        "menu": "Menu",
        "droits": "All rights reserved.",
        "surtitre": "Painting · Restoration · Decorative plaster · Home staging",
        "accroche": "[One sentence introducing her: what she does, for whom, and what makes her work unique.]",
        "voir_prestations": "My services",
        "devis": "Request a quote",
        "photo_principale": "Main photo",
        "prestations": "Services",
        "prestations_intro": "[One introductory sentence: bespoke, attentive, from advice to completion.]",
        "en_savoir_plus": "Learn more →",
        "realisations": "Projects",
        "realisations_recentes": "Recent projects",
        "toutes_realisations": "All projects →",
        "photo": "Photo",
        "cta_titre": "Have a project in mind?",
        "cta_texte": "Describe it in a few lines and I will reply with a proposal and a quote.",
        "filtrer": "Filter by service",
        "tout": "All",
        "vue_grand": "Enlarged project",
        "fermer": "Close",
        "precedente": "Previous",
        "suivante": "Next",
        "a_propos": "About",
        "portrait": "Portrait",
        "bio": "[Her biography: background, training, what led her to painting and decoration.]",
        "bio_demarche": "[How she works: listening, materials, bespoke.]",
        "parcours": "Background",
        "zone": "Studio in Cannes. Works across the French Riviera: Cannes, Antibes, Nice, Grasse, Saint-Tropez and the surrounding area.",
        "contact": "Contact",
        "ecrivez": "Let's talk about your project",
        "contact_intro": "For a quote, a commission or a simple question, write to me: I reply quickly.",
        "email": "Email",
        "telephone": "Phone",
        "nom": "Name",
        "type_projet": "Service",
        "autre": "Other",
        "message": "Your project (place, surface, timing…)",
        "envoyer": "Send request",
    },
}

PAGES = ["index", "prestations", "realisations", "a-propos", "contact"]


def chemin(langue, page):
    """Adresse d'une page depuis la racine du site, sans .html (cleanUrls de Vercel)."""
    if langue == LANGUES[0]:
        return "/" if page == "index" else f"/{page}"
    return f"/{langue}" if page == "index" else f"/{langue}/{page}"


def nom_prestation(id_, langue):
    return next(p["titre"][langue] for p in PRESTATIONS if p["id"] == id_)


def figure(r, t, langue):
    if r["image"]:
        visuel = f'<img src="/images/realisations/{r["image"]}" alt="{escape(r["titre"][langue])}" loading="lazy">'
    else:
        visuel = f'<div class="attente">{t["photo"]}</div>'
    return f'''        <figure class="oeuvre" data-categorie="{r["prestation"]}">
          <div class="cadre">{visuel}</div>
          <figcaption><div class="nom">{escape(r["titre"][langue])}</div><div class="details">{escape(nom_prestation(r["prestation"], langue))} · {escape(r["details"][langue])}</div></figcaption>
        </figure>'''


def appel_devis(t, langue):
    return f'''    <section class="section conteneur" style="text-align:center;max-width:720px">
      <h2>{t["cta_titre"]}</h2>
      <p style="color:var(--texte-doux)">{t["cta_texte"]}</p>
      <p><a class="bouton plein" href="{chemin(langue, "contact")}">{t["devis"]}</a></p>
    </section>'''


def corps_index(t, langue):
    cartes = "\n".join(
        f'''          <a class="carte" href="{chemin(langue, "prestations")}#{p["id"]}">
            <h3>{p["titre"][langue]}</h3>
            <p>{p["resume"][langue]}</p>
            <span class="lien">{t["en_savoir_plus"]}</span>
          </a>''' for p in PRESTATIONS
    )
    recentes = "\n".join(figure(r, t, langue) for r in REALISATIONS[:3])
    return f'''    <section class="conteneur hero">
      <div>
        <p class="surtitre">{t["surtitre"]}</p>
        <h1>Sonja Petric</h1>
        <p>{t["accroche"]}</p>
        <p style="margin-top:28px"><a class="bouton plein" href="{chemin(langue, "contact")}">{t["devis"]}</a> &nbsp; <a class="bouton" href="{chemin(langue, "prestations")}">{t["voir_prestations"]}</a></p>
      </div>
      <div class="hero-image"><div class="attente">{t["photo_principale"]}</div></div>
    </section>

    <section class="section" style="background:var(--surface)">
      <div class="conteneur">
        <div class="section-titre"><h2>{t["prestations"]}</h2></div>
        <div class="cartes">
{cartes}
        </div>
      </div>
    </section>

    <section class="section conteneur">
      <div class="section-titre">
        <h2>{t["realisations_recentes"]}</h2>
        <a href="{chemin(langue, "realisations")}">{t["toutes_realisations"]}</a>
      </div>
      <div class="galerie">
{recentes}
      </div>
    </section>

{appel_devis(t, langue)}'''


def corps_prestations(t, langue):
    blocs = "\n".join(
        f'''      <article class="prestation" id="{p["id"]}">
        <div class="prestation-image"><div class="attente">{t["photo"]}</div></div>
        <div>
          <h2>{p["titre"][langue]}</h2>
          <p>{p["resume"][langue]}</p>
          <ul>
{chr(10).join(f"            <li>{x}</li>" for x in p["points"][langue])}
          </ul>
          <p><a href="{chemin(langue, "realisations")}#{p["id"]}">{t["toutes_realisations"]}</a></p>
        </div>
      </article>''' for p in PRESTATIONS
    )
    return f'''    <section class="section conteneur">
      <p class="surtitre">{t["prestations"]}</p>
      <h1>{t["prestations"]}</h1>
      <p style="color:var(--texte-doux);max-width:40em">{t["prestations_intro"]}</p>
{blocs}
    </section>

{appel_devis(t, langue)}'''


def corps_realisations(t, langue):
    filtres = "\n".join(f'        <button data-filtre="{p["id"]}" aria-pressed="false">{p["titre"][langue]}</button>' for p in PRESTATIONS)
    items = "\n".join(figure(r, t, langue) for r in REALISATIONS)
    return f'''    <section class="section conteneur">
      <div class="section-titre"><h1>{t["realisations"]}</h1></div>
      <div class="filtres" role="group" aria-label="{t["filtrer"]}">
        <button data-filtre="tout" aria-pressed="true">{t["tout"]}</button>
{filtres}
      </div>
      <div class="galerie">
{items}
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
    lignes = "\n".join(f'          <li><span class="annee">{e["annee"]}</span><span>{e[langue]}</span></li>' for e in PARCOURS)
    return f'''    <section class="section conteneur apropos">
      <div class="portrait"><div class="attente">{t["portrait"]}</div></div>
      <div>
        <p class="surtitre">{t["a_propos"]}</p>
        <h1>Sonja Petric</h1>
        <p>{t["bio"]}</p>
        <p>{t["bio_demarche"]}</p>
        <p>{t["zone"]}</p>
        <h2 style="margin-top:40px;font-size:1.8rem">{t["parcours"]}</h2>
        <ul class="parcours">
{lignes}
        </ul>
      </div>
    </section>

{appel_devis(t, langue)}'''


def corps_contact(t, langue):
    options = "\n".join(f'            <option>{p["titre"][langue]}</option>' for p in PRESTATIONS)
    tel = f'<br>\n           {t["telephone"]} : <a href="tel:{TELEPHONE.replace(" ", "")}">{TELEPHONE}</a>' if TELEPHONE else ""
    return f'''    <section class="section conteneur contact">
      <div class="coordonnees">
        <p class="surtitre">{t["contact"]}</p>
        <h1>{t["ecrivez"]}</h1>
        <p>{t["contact_intro"]}</p>
        <p>{t["email"]} : <a href="mailto:{EMAIL}">{EMAIL}</a>{tel}<br>
           Instagram : <a href="{INSTAGRAM}" rel="noopener">@[compte]</a><br>
           {t["zone"]}</p>
      </div>
      <form class="formulaire" action="https://formspree.io/f/{FORMSPREE_ID}" method="POST">
        <label>{t["nom"]}<input name="nom" required autocomplete="name"></label>
        <label>{t["email"]}<input type="email" name="email" required autocomplete="email"></label>
        <label>{t["type_projet"]}
          <select name="prestation">
{options}
            <option>{t["autre"]}</option>
          </select>
        </label>
        <label>{t["message"]}<textarea name="message" required></textarea></label>
        <div><button class="bouton plein" type="submit">{t["envoyer"]}</button></div>
      </form>
    </section>'''


CORPS = {
    "index": corps_index,
    "prestations": corps_prestations,
    "realisations": corps_realisations,
    "a-propos": corps_a_propos,
    "contact": corps_contact,
}


def page(langue, nom):
    t = TEXTES[langue]
    nav = "\n".join(
        f'        <a href="{chemin(langue, p)}"{" aria-current=\"page\"" if p == nom else ""}>{t["nav"][p]}</a>' for p in PAGES
    )
    langues = " ".join(
        f'<a href="{chemin(l, nom)}" lang="{l}" hreflang="{l}"{" aria-current=\"true\"" if l == langue else ""}>{l.upper()}</a>' for l in LANGUES
    )
    alternates = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{chemin(l, nom)}">' for l in LANGUES)
    extra = visionneuse(t) if nom == "realisations" else ""
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
