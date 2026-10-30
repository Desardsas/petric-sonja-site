"""Génère les pages HTML du site dans chaque langue.

Tout le contenu est dans ce fichier : coordonnées, PRESTATIONS, REALISATIONS, PARCOURS et TEXTES.
Après une modification : python3 generer.py (nécessite Pillow : pip install pillow), puis commit des fichiers
.html et des images générées dans images/_gen/.
Le français est à la racine du site, chaque autre langue dans son dossier (en/, ...).
"""
from html import escape
from pathlib import Path

RACINE = Path(__file__).parent
LANGUES = ["fr", "en"]  # la première est la langue par défaut, à la racine
EMAIL = "sonjapetric92@gmail.com"
TELEPHONE = ""  # par exemple "+33 6 12 34 56 78" ; vide = non affiché
INSTAGRAM = "https://www.instagram.com/psonjap/"
PHOTO_ACCUEIL = "sonja-petric-portrait.jpg"  # dans images/ ; None = cadre d'attente
# Service qui transforme chaque demande de devis en e-mail pour Sonja.
# "web3forms" : CLE_FORMULAIRE = la clé reçue sur https://web3forms.com (gratuit, sans compte)
# "formspree" : CLE_FORMULAIRE = l'identifiant du formulaire créé sur https://formspree.io
SERVICE_FORMULAIRE = "web3forms"
CLE_FORMULAIRE = "53f87200-2afb-415d-aa77-5d1bc108841a"  # vide = formulaire pas encore activé, le site propose alors l'e-mail

# Les services, dans l'ordre d'affichage. L'identifiant sert aussi de catégorie aux réalisations.
PRESTATIONS = [
    {
        "id": "peinture",
        "image": "illustrations/peinture-toile-console.jpg",
        "titre": {"fr": "Peinture", "en": "Painting"},
        "resume": {"fr": "Des toiles contemporaines aux lignes épurées, et des œuvres sur commande pensées pour votre intérieur.", "en": "Contemporary canvases with clean lines, and commissioned works designed for your interior."},
        "points": {
            "fr": ["Œuvres originales", "Toiles sur commande, au format et aux couleurs de votre pièce", "Grands formats pour particuliers, hôtels et bureaux"],
            "en": ["Original works", "Commissioned canvases, sized and coloured for your room", "Large formats for homes, hotels and offices"],
        },
    },
    {
        "id": "restauration",
        "image": "restauration-avant-apres.jpg",
        "entier": True,  # image montrée en entier (avant / après), sans recadrage
        "titre": {"fr": "Restauration de peinture", "en": "Painting restoration"},
        "resume": {"fr": "Formée à l'École supérieure d'art d'Avignon, elle redonne vie aux tableaux abîmés par le temps, dans le respect de l'œuvre.", "en": "Trained at the École supérieure d'art d'Avignon, she brings time-worn paintings back to life while respecting the original work."},
        "points": {
            "fr": ["Nettoyage et allègement des vernis", "Consolidation et retouches", "Conseils de conservation"],
            "en": ["Cleaning and varnish reduction", "Consolidation and retouching", "Conservation advice"],
        },
    },
    {
        "id": "enduits",
        "image": "enduit-salon.jpg",
        "titre": {"fr": "Enduits décoratifs sur mesure", "en": "Bespoke decorative plaster"},
        "resume": {"fr": "Des murs uniques, créés sur mesure : matières minérales, textures subtiles et teintes choisies avec vous.", "en": "Unique walls, made to measure: mineral materials, subtle textures and colours chosen with you."},
        "points": {
            "fr": ["Enduits à la chaux, effets béton et matières minérales", "Teintes et textures créées pour chaque projet", "Salons, chambres, salles de bains, commerces"],
            "en": ["Lime plasters, concrete effects and mineral finishes", "Colours and textures created for each project", "Living rooms, bedrooms, bathrooms, shops"],
        },
    },
    {
        "id": "home-staging",
        "image": "illustrations/home-staging-salon.jpg",
        "titre": {"fr": "Home staging", "en": "Home staging"},
        "resume": {"fr": "Valoriser un bien pour le vendre ou le louer plus vite, avec un regard d'artiste et des moyens maîtrisés.", "en": "Enhancing a property so it sells or rents faster, with an artist's eye and a controlled budget."},
        "points": {
            "fr": ["Conseil couleurs et agencement", "Rafraîchissement des murs avant les photos", "Mise en scène pour la vente ou la location"],
            "en": ["Colour and layout advice", "Wall refresh before the photo shoot", "Staging for sale or rental"],
        },
    },
]

# Chaque réalisation : fichier image dans images/realisations/ (ou "dossier/fichier" depuis images/),
# prestation (un "id" de PRESTATIONS), titre et détails dans chaque langue.
# "illustration": True = image d'ambiance (générée par IA), pas un chantier de Sonja : elle n'apparaît
# que si ILLUSTRATIONS_DANS_REALISATIONS vaut True, avec la mention « Illustration » sur son cartel.
# Une réalisation sans image ("image": None) n'est pas affichée.
# Les trois premières affichées apparaissent sur l'accueil.
REALISATIONS = [
    {"image": "enduit-salon.jpg", "prestation": "enduits", "titre": {"fr": "Mur de salon en enduit décoratif", "en": "Living room wall in decorative plaster"}, "details": {"fr": "", "en": ""}},
    {"image": "restauration-avant-apres.jpg", "entier": True, "prestation": "restauration", "titre": {"fr": "Tableau ancien, avant / après", "en": "Old painting, before / after"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/peinture-formes-terre-cuite.jpg", "illustration": True, "prestation": "peinture", "titre": {"fr": "Formes en terre cuite", "en": "Terracotta shapes"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/enduit-tadelakt-salle-de-bain.jpg", "illustration": True, "prestation": "enduits", "titre": {"fr": "Salle de bains en tadelakt", "en": "Tadelakt bathroom"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/peinture-diptyque-arches.jpg", "illustration": True, "prestation": "peinture", "titre": {"fr": "Diptyque aux arches", "en": "Arches diptych"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/enduit-chaux-olivier.jpg", "illustration": True, "prestation": "enduits", "titre": {"fr": "Mur à la chaux", "en": "Lime plaster wall"}, "details": {"fr": "", "en": ""}},
]

ILLUSTRATIONS_DANS_REALISATIONS = True  # True = montrer aussi les illustrations IA dans Réalisations et sur l'accueil

PARCOURS = [
    {"annee": "[Année]", "fr": "Formation à l'École supérieure d'art d'Avignon (ESAA)", "en": "Trained at the École supérieure d'art d'Avignon (ESAA)"},
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
        "accroche": "Artiste peintre à Cannes, je crée des toiles, des murs et des intérieurs contemporains, et je restaure les tableaux qui comptent pour vous.",
        "voir_prestations": "Mes prestations",
        "devis": "Demander un devis",
        "photo_principale": "Portrait de Sonja Petric",
        "prestations": "Prestations",
        "prestations_intro": "Chaque projet est unique : je vous écoute, je vous conseille, puis je réalise le travail moi-même, du premier croquis à la dernière touche.",
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
        "bio": "Formée à l'École supérieure d'art d'Avignon, Sonja Petric partage son travail entre la création et le savoir-faire : peinture, restauration de tableaux, enduits décoratifs et home staging.",
        "bio_demarche": "Son style est contemporain et épuré : des lignes simples, des matières justes et des couleurs choisies avec soin, pour des œuvres et des lieux qui vous ressemblent.",
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
        "telephone_facultatif": "Téléphone (facultatif)",
        "ville": "Ville du projet",
        "mention": "Vos informations servent uniquement à répondre à votre demande.",
        "envoi": "Envoi en cours…",
        "merci": "Merci, votre demande est bien envoyée. Je vous réponds au plus vite.",
        "erreur": "L'envoi n'a pas abouti. Vous pouvez m'écrire directement à",
        "pas_actif": "Le formulaire sera bientôt actif. En attendant, écrivez-moi à",
        "sujet": "Nouvelle demande de devis depuis petricsonja.art",
        "voir": "Voir",
        "copier": "Copier",
        "copie": "Copié",
        "image_a_venir": "Image à venir",
        "illustration": "Illustration",
        "echap": "Échap",
        "lieu": "Cannes, Côte d'Azur",
        "fermer_menu": "Fermer",
        "aller_contenu": "Aller au contenu",
        "atelier_libelle": "Atelier",
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
        "accroche": "A painter based in Cannes, I create contemporary canvases, walls and interiors, and restore the paintings that matter to you.",
        "voir_prestations": "My services",
        "devis": "Request a quote",
        "photo_principale": "Portrait of Sonja Petric",
        "prestations": "Services",
        "prestations_intro": "Every project is unique: I listen, I advise, then I carry out the work myself, from the first sketch to the final touch.",
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
        "bio": "Trained at the École supérieure d'art d'Avignon, Sonja Petric divides her work between creation and craft: painting, painting restoration, decorative plaster and home staging.",
        "bio_demarche": "Her style is contemporary and clean: simple lines, honest materials and carefully chosen colours, for works and spaces that feel like you.",
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
        "telephone_facultatif": "Phone (optional)",
        "ville": "Project location",
        "mention": "Your details are only used to reply to your request.",
        "envoi": "Sending…",
        "merci": "Thank you, your request has been sent. I will get back to you shortly.",
        "erreur": "The request could not be sent. You can email me directly at",
        "pas_actif": "The form will be active soon. In the meantime, email me at",
        "sujet": "New quote request from petricsonja.art",
        "voir": "View",
        "copier": "Copy",
        "copie": "Copied",
        "image_a_venir": "Image to come",
        "illustration": "Illustration",
        "echap": "Esc",
        "lieu": "Cannes, French Riviera",
        "fermer_menu": "Close",
        "aller_contenu": "Skip to content",
        "atelier_libelle": "Studio",
    },
}


PAGES = ["index", "prestations", "realisations", "a-propos", "contact"]
LARGEURS = [640, 1024, 1600]  # tailles générées pour chaque image (AVIF et WebP)


def chemin(langue, page):
    """Adresse d'une page depuis la racine du site, sans .html (cleanUrls de Vercel)."""
    if langue == LANGUES[0]:
        return "/" if page == "index" else f"/{page}"
    return f"/{langue}" if page == "index" else f"/{langue}/{page}"


def fichier_image(nom):
    """Chemin depuis images/ : les noms simples sont dans images/realisations/."""
    return nom if "/" in nom else f"realisations/{nom}"


def realisations_visibles():
    return [r for r in REALISATIONS if r["image"] and (ILLUSTRATIONS_DANS_REALISATIONS or not r.get("illustration"))]


def num(n, chiffres=3):
    return str(n).zfill(chiffres)


def nom_prestation(id_, langue):
    return next(p["titre"][langue] for p in PRESTATIONS if p["id"] == id_)


_IMAGES = {}


def image(fichier):
    """Prépare les variantes AVIF / WebP d'une image (dans images/_gen/) et renvoie ses infos.

    Les variantes ne sont recalculées que si elles n'existent pas encore. Nécessite Pillow.
    """
    if fichier in _IMAGES:
        return _IMAGES[fichier]
    from PIL import Image

    source = RACINE / "images" / fichier
    sortie = RACINE / "images" / "_gen"
    sortie.mkdir(exist_ok=True)
    with Image.open(source) as im:
        im = im.convert("RGB")
        largeur, hauteur = im.size
        couleur = "#%02x%02x%02x" % im.resize((1, 1), Image.LANCZOS).getpixel((0, 0))
        largeurs = [l for l in LARGEURS if l < largeur] + [largeur]
        base = Path(fichier).stem
        for l in largeurs:
            for fmt, options in (("avif", {"quality": 55}), ("webp", {"quality": 78})):
                cible = sortie / f"{base}-{l}.{fmt}"
                if not cible.exists():
                    im.resize((l, round(hauteur * l / largeur)), Image.LANCZOS).save(cible, **options)
    infos = {
        "src": f"/images/{fichier}",
        "largeur": largeur,
        "hauteur": hauteur,
        "couleur": couleur,
        "srcset": {fmt: ", ".join(f"/images/_gen/{base}-{l}.{fmt} {l}w" for l in largeurs) for fmt in ("avif", "webp")},
    }
    _IMAGES[fichier] = infos
    return infos


def picture(fichier, alt, tailles, prioritaire=False):
    i = image(fichier)
    chargement = 'fetchpriority="high"' if prioritaire else 'loading="lazy"'
    return (
        f'<picture class="fondu" style="background-color:{i["couleur"]}">'
        f'<source type="image/avif" srcset="{i["srcset"]["avif"]}" sizes="{tailles}">'
        f'<source type="image/webp" srcset="{i["srcset"]["webp"]}" sizes="{tailles}">'
        f'<img src="{i["src"]}" alt="{escape(alt)}" width="{i["largeur"]}" height="{i["hauteur"]}" {chargement} decoding="async">'
        "</picture>"
    )


def attente(t):
    return f'<div class="attente"><span>{t["image_a_venir"]}</span></div>'


def titre_masque(balise, texte, classe=""):
    """Titre révélé par un masque au défilement."""
    attr = f' class="{classe}"' if classe else ""
    return f'<{balise}{attr} data-reveal="masque"><span class="ligne"><span>{texte}</span></span></{balise}>'


def entete_section(numero, libelle):
    return f'<p class="index-section mono" data-reveal><span>{num(numero)}</span><span>{libelle}</span></p>'


def oeuvre(r, n, total, t, langue, tailles):
    if r["image"]:
        visuel = picture(fichier_image(r["image"]), r["titre"][langue], tailles)
    else:
        visuel = attente(t)
    mention = t["illustration"] if r.get("illustration") else ""
    details = " · ".join(x for x in (nom_prestation(r["prestation"], langue), r["details"][langue], mention) if x)
    ouvrable = ' data-ouvrable tabindex="0" role="button"' if r["image"] else ""
    return f'''<figure class="oeuvre" data-categorie="{r["prestation"]}" data-numero="{num(n)}"{ouvrable} data-reveal>
          <div class="oeuvre-image">{visuel}</div>
          <figcaption class="cartel mono"><span class="cartel-num">{num(n)}</span><span class="cartel-titre">{escape(r["titre"][langue])}</span><span class="cartel-details">{escape(details)}</span></figcaption>
        </figure>'''


def appel_devis(t, langue, numero):
    return f'''    <section class="section appel grille">
      <div class="col-entete">{entete_section(numero, t["contact"])}</div>
      <div class="col-principale">
        {titre_masque("h2", t["cta_titre"], "titre-xl")}
        <p class="texte-large" data-reveal>{t["cta_texte"]}</p>
        <p data-reveal><a class="lien-fort accent" href="{chemin(langue, "contact")}">{t["devis"]} <span aria-hidden="true">→</span></a></p>
      </div>
    </section>'''


def corps_index(t, langue):
    lignes = "\n".join(
        f'''        <li class="ligne-prestation" data-reveal>
          <a href="{chemin(langue, "prestations")}#{p["id"]}">
            <span class="mono num">{num(n, 2)}</span>
            <span class="lp-titre">{p["titre"][langue]}</span>
            <span class="lp-resume">{p["resume"][langue]}</span>
            <span class="mono lp-fleche" aria-hidden="true">→</span>
          </a>
        </li>''' for n, p in enumerate(PRESTATIONS, 1)
    )
    avec_image = list(enumerate(realisations_visibles(), 1))[:3]
    recentes = "\n".join(
        oeuvre(r, n, len(realisations_visibles()), t, langue, "(max-width: 760px) 100vw, 50vw") for n, r in avec_image
    )
    portrait = picture(PHOTO_ACCUEIL, t["photo_principale"], "(max-width: 760px) 100vw, 40vw", prioritaire=True) if PHOTO_ACCUEIL else attente(t)
    return f'''    <section class="hero grille">
      <p class="hero-meta mono" data-reveal><span>{num(1)}</span><span>{t["lieu"]}</span></p>
      <h1 class="hero-nom" data-reveal="masque"><span class="ligne"><span>Sonja</span></span><span class="ligne"><span>Petric</span></span></h1>
      <div class="hero-texte">
        <p class="mono surtitre" data-reveal>{t["surtitre"]}</p>
        <p class="texte-large" data-reveal>{t["accroche"]}</p>
        <p class="actions" data-reveal><a class="lien-fort accent" href="{chemin(langue, "contact")}">{t["devis"]} <span aria-hidden="true">→</span></a><a class="lien-fort" href="{chemin(langue, "realisations")}">{t["realisations"]} <span aria-hidden="true">→</span></a></p>
      </div>
      <figure class="hero-portrait" data-reveal>
        <div class="hero-image">{portrait}</div>
        <figcaption class="cartel mono"><span class="cartel-titre">Sonja Petric</span><span class="cartel-details">{t["photo_principale"]}</span></figcaption>
      </figure>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(2, t["prestations"])}</div>
      <div class="col-large">
        <ul class="liste-prestations">
{lignes}
        </ul>
      </div>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(3, t["realisations_recentes"])}<p class="mono" data-reveal><a class="lien" href="{chemin(langue, "realisations")}">{t["toutes_realisations"]}</a></p></div>
      <div class="col-large galerie galerie-accueil">
        {recentes}
      </div>
    </section>

{appel_devis(t, langue, 4)}'''


def corps_prestations(t, langue):
    blocs = []
    for n, p in enumerate(PRESTATIONS, 1):
        visuel = picture(fichier_image(p["image"]), p["titre"][langue], "(max-width: 760px) 100vw, 45vw") if p.get("image") else attente(t)
        points = "\n".join(f"            <li>{x}</li>" for x in p["points"][langue])
        blocs.append(f'''      <article class="prestation grille{" inverse" if n % 2 == 0 else ""}" id="{p["id"]}">
        <p class="mono num prestation-num" data-reveal>{num(n, 2)} / {num(len(PRESTATIONS), 2)}</p>
        <div class="prestation-texte">
          {titre_masque("h2", p["titre"][langue], "titre-l")}
          <p class="texte-large" data-reveal>{p["resume"][langue]}</p>
          <ul class="liste-mono mono" data-reveal>
{points}
          </ul>
          <p class="mono" data-reveal><a class="lien" href="{chemin(langue, "realisations")}#{p["id"]}">{t["toutes_realisations"]}</a></p>
        </div>
        <figure class="prestation-image" data-reveal>{visuel}</figure>
      </article>''')
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(2, t["prestations"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["prestations"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["prestations_intro"]}</p>
      </div>
    </section>
{chr(10).join(blocs)}

{appel_devis(t, langue, 4)}'''


def corps_realisations(t, langue):
    visibles = realisations_visibles()
    total = len(visibles)
    filtres = "\n".join(
        f'        <button class="filtre" data-filtre="{p["id"]}" aria-pressed="false">{p["titre"][langue]} <span class="compte">{sum(r["prestation"] == p["id"] for r in visibles)}</span></button>'
        for p in PRESTATIONS
    )
    items = "\n        ".join(oeuvre(r, n, total, t, langue, "(max-width: 760px) 100vw, 50vw") for n, r in enumerate(visibles, 1))
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(3, t["realisations"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["realisations"], "titre-xxl")}
      </div>
    </section>
    <section class="section-galerie grille">
      <div class="filtres mono" role="group" aria-label="{t["filtrer"]}">
        <button class="filtre" data-filtre="tout" aria-pressed="true">{t["tout"]} <span class="compte">{total}</span></button>
{filtres}
      </div>
      <div class="galerie galerie-complete">
        {items}
      </div>
    </section>'''


def visionneuse(t):
    return f'''
  <div class="visionneuse" role="dialog" aria-modal="true" aria-label="{t["vue_grand"]}" hidden>
    <div class="vis-barre mono">
      <span class="vis-compteur" aria-live="polite"></span>
      <button class="vis-fermer lien" type="button">{t["fermer"]} <span class="faible">[{t["echap"]}]</span></button>
    </div>
    <figure class="vis-figure"><img src="" alt=""><figcaption class="cartel mono"></figcaption></figure>
    <div class="vis-nav mono">
      <button class="vis-prec lien" type="button">← {t["precedente"]}</button>
      <button class="vis-suiv lien" type="button">{t["suivante"]} →</button>
    </div>
  </div>
'''


def corps_a_propos(t, langue):
    lignes = "\n".join(
        f'          <li data-reveal><span class="mono annee">{e["annee"]}</span><span>{e[langue]}</span></li>' for e in PARCOURS
    )
    portrait = picture(PHOTO_ACCUEIL, t["photo_principale"], "(max-width: 760px) 100vw, 35vw") if PHOTO_ACCUEIL else attente(t)
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(4, t["a_propos"])}</div>
      <div class="col-large">
        {titre_masque("h1", "Sonja Petric", "titre-xxl nom")}
      </div>
    </section>
    <section class="section apropos grille">
      <figure class="apropos-portrait" data-reveal>{portrait}<figcaption class="cartel mono"><span class="cartel-titre">Sonja Petric</span><span class="cartel-details">{t["lieu"]}</span></figcaption></figure>
      <div class="apropos-texte">
        <p class="texte-large" data-reveal>{t["bio"]}</p>
        <p data-reveal>{t["bio_demarche"]}</p>
        <p class="mono faible-texte" data-reveal>{t["zone"]}</p>
        <h2 class="mono index-section" data-reveal><span>—</span><span>{t["parcours"]}</span></h2>
        <ul class="parcours">
{lignes}
        </ul>
      </div>
    </section>

{appel_devis(t, langue, 5)}'''


def corps_contact(t, langue):
    options = "\n".join(f'              <option>{p["titre"][langue]}</option>' for p in PRESTATIONS)
    tel = f'\n          <li><span class="mono etiquette">{t["telephone"]}</span><a class="lien" href="tel:{TELEPHONE.replace(" ", "")}">{TELEPHONE}</a></li>' if TELEPHONE else ""
    if SERVICE_FORMULAIRE == "formspree":
        adresse, caches = f"https://formspree.io/f/{CLE_FORMULAIRE}", f'        <input type="hidden" name="_subject" value="{t["sujet"]}">'
    else:
        adresse = "https://api.web3forms.com/submit"
        caches = (f'        <input type="hidden" name="access_key" value="{CLE_FORMULAIRE}">\n'
                  f'        <input type="hidden" name="subject" value="{t["sujet"]}">\n'
                  '        <input type="hidden" name="from_name" value="petricsonja.art">')
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(5, t["contact"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["ecrivez"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["contact_intro"]}</p>
      </div>
    </section>
    <section class="section contact grille">
      <ul class="coordonnees" data-reveal>
        <li><span class="mono etiquette">{t["email"]}</span><a class="lien email" href="mailto:{EMAIL}">{EMAIL}</a> <button class="copier mono" type="button" data-copier="{EMAIL}" data-copie="{t["copie"]}">{t["copier"]}</button></li>{tel}
        <li><span class="mono etiquette">Instagram</span><a class="lien" href="{INSTAGRAM}" rel="noopener">@psonjap</a></li>
        <li><span class="mono etiquette">{t["atelier_libelle"]}</span><span>{t["zone"]}</span></li>
      </ul>
      <form class="formulaire" action="{adresse}" method="POST" data-actif="{"oui" if CLE_FORMULAIRE else "non"}"
            data-envoi="{t["envoi"]}" data-merci="{t["merci"]}" data-erreur="{t["erreur"]}" data-pas-actif="{t["pas_actif"]}" data-email="{EMAIL}" data-reveal>
{caches}
        <input type="checkbox" name="botcheck" class="piege" tabindex="-1" autocomplete="off" aria-hidden="true">
        <label class="champ"><span class="mono">{t["nom"]}</span><input name="nom" required autocomplete="name"></label>
        <div class="deux-colonnes">
          <label class="champ"><span class="mono">{t["email"]}</span><input type="email" name="email" required autocomplete="email"></label>
          <label class="champ"><span class="mono">{t["telephone_facultatif"]}</span><input type="tel" name="telephone" autocomplete="tel"></label>
        </div>
        <div class="deux-colonnes">
          <label class="champ"><span class="mono">{t["type_projet"]}</span>
            <select name="prestation">
{options}
              <option>{t["autre"]}</option>
            </select>
          </label>
          <label class="champ"><span class="mono">{t["ville"]}</span><input name="ville" autocomplete="address-level2"></label>
        </div>
        <label class="champ"><span class="mono">{t["message"]}</span><textarea name="message" rows="5" required></textarea></label>
        <p class="mono mention">{t["mention"]}</p>
        <div class="envoi"><button class="lien-fort accent" type="submit">{t["envoyer"]} <span aria-hidden="true">→</span></button><p class="etat mono" role="status" aria-live="polite"></p></div>
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
    index_page = PAGES.index(nom) + 1
    nav = "\n".join(
        f'          <li><a class="lien-nav" href="{chemin(langue, p)}"{" aria-current=\"page\"" if p == nom else ""}><span class="num">{num(i, 2)}</span>{t["nav"][p]}</a></li>'
        for i, p in enumerate(PAGES, 1)
    )
    langues = "".join(
        f'<a class="lien-nav" href="{chemin(l, nom)}" lang="{l}" hreflang="{l}"{" aria-current=\"true\"" if l == langue else ""}>{l.upper()}</a>' for l in LANGUES
    )
    alternates = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{chemin(l, nom)}">' for l in LANGUES)
    extra = visionneuse(t) if nom in ("realisations", "index") else ""
    return f'''<!doctype html>
<html lang="{langue}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t["titres"][nom]}</title>
  <meta name="description" content="{t["description"]}">
  <meta name="theme-color" content="#3A3029">
  <meta name="color-scheme" content="dark">
  <meta property="og:title" content="{t["titres"][nom]}">
  <meta property="og:description" content="{t["description"]}">
  <meta property="og:type" content="website">
{alternates}
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/fonts/inter-tight.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/cormorant-garamond.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/css/style.css">
  <script>document.documentElement.classList.add("js")</script>
</head>
<body>
  <a class="evitement mono" href="#contenu">{t["aller_contenu"]}</a>
  <header class="entete">
    <a class="logo" href="{chemin(langue, "index")}"><img class="logo-sp" src="/images/logo-sp.svg" alt="" width="18" height="38">Sonja Petric</a>
    <p class="indicateur mono" aria-hidden="true"><span class="num">{num(index_page, 2)}</span> / {num(len(PAGES), 2)} — {t["nav"][nom]}</p>
    <nav class="nav mono" id="menu" aria-label="Menu">
      <ul>
{nav}
      </ul>
      <div class="langues">{langues}</div>
    </nav>
    <button class="menu-bouton mono" type="button" aria-expanded="false" aria-controls="menu" data-ouvrir="{t["menu"]}" data-fermer="{t["fermer_menu"]}">{t["menu"]}</button>
  </header>

  <main id="contenu">
{CORPS[nom](t, langue)}
  </main>
{extra}
  <footer class="pied mono grille">
    <span>© <span id="annee"></span> Sonja Petric</span>
    <span>{t["lieu"]}</span>
    <a class="lien" href="mailto:{EMAIL}">{EMAIL}</a>
    <a class="lien" href="{INSTAGRAM}" rel="noopener">Instagram</a>
  </footer>
  <div class="curseur" aria-hidden="true"><div class="curseur-anneau"><span class="curseur-label"></span></div><div class="curseur-point"></div><div class="curseur-coords"></div></div>
  <script src="/js/main.js" defer></script>
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
