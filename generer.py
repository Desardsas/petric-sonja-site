"""Génère les pages HTML du site dans chaque langue.

Tout le contenu est dans ce fichier : coordonnées, PRESTATIONS, REALISATIONS, PARCOURS, FAQ et TEXTES.
Après une modification : python3 generer.py (nécessite Pillow : pip install pillow), puis commit des fichiers
.html et des images générées dans images/_gen/.
Le français est à la racine du site, chaque autre langue dans son dossier (en/, ...), avec ses propres
adresses (SLUGS).
"""
from html import escape
from pathlib import Path

RACINE = Path(__file__).parent
LANGUES = ["fr", "en"]  # la première est la langue par défaut, à la racine
EMAIL = "sonjapetric92@gmail.com"
TELEPHONE = "+33 6 09 49 18 75"  # vide = non affiché
WHATSAPP = "33609491875"  # numéro au format international sans + ni espace, pour https://wa.me/ ; vide = non affiché
SITE = "https://www.petricsonja.art"  # adresse publique, pour les liens canoniques, hreflang, JSON-LD et le plan du site
# Mentions légales : la page n'est générée que lorsque SIRET est rempli (mention obligatoire).
STATUT = {"fr": "Entrepreneuse individuelle (micro-entreprise)", "en": "Sole trader (micro-entreprise)"}  # à confirmer
SIRET = ""
ADRESSE = ""  # vide = « Cannes, sur rendez-vous »
INSTAGRAM = "https://www.instagram.com/psonjap/"
PHOTO_ACCUEIL = "sonja-petric-portrait.jpg"  # dans images/ ; None = cadre d'attente
# Service qui transforme chaque demande de devis en e-mail pour Sonja.
# "web3forms" : CLE_FORMULAIRE = la clé reçue sur https://web3forms.com (gratuit, sans compte)
# "formspree" : CLE_FORMULAIRE = l'identifiant du formulaire créé sur https://formspree.io
SERVICE_FORMULAIRE = "web3forms"
CLE_FORMULAIRE = "53f87200-2afb-415d-aa77-5d1bc108841a"  # vide = formulaire pas encore activé, le site propose alors l'e-mail

NBSP = " "
SUR_DEVIS = {"fr": "Sur devis, après une première visite.", "en": "On quotation, after a first visit."}

# Les quatre prestations, dans l'ordre d'affichage. "livrable" résume ce que le client reçoit (accueil),
# "points" détaille les livrables (page Prestations). Aucune durée ni aucun prix : tout est sur devis.
PRESTATIONS = [
    {
        "id": "couleurs-matieres",
        "image": "enduit-salon.jpg",
        "alt": {"fr": "Salon aux murs en enduit décoratif ocre clair, éclairé par deux appliques", "en": "Living room with pale ochre decorative plaster walls lit by two wall lights"},
        "titre": {"fr": "Conseil couleurs & matières", "en": "Colour & materials"},
        "resume": {"fr": "Choisir les teintes, les enduits et les finitions d'un lieu d'après sa lumière, son usage et ce qui est déjà là : sols, bois, pierre, mobilier.",
                   "en": "Choosing the colours, plasters and finishes of a place according to its light, its use and what is already there: floors, wood, stone, furniture."},
        "livrable": {"fr": "Palette référencée, échantillons testés sur vos murs", "en": "Referenced palette, samples tested on your walls"},
        "points": {
            "fr": ["Lecture de la lumière, pièce par pièce, à plusieurs heures du jour", "Palette référencée : marque, référence et finition de chaque teinte", "Échantillons peints ou enduits, testés sur place avant toute décision", "Enduits à la chaux, effets béton et matières minérales", "Réalisation des enduits décoratifs, ou suivi de l'artisan de votre choix"],
            "en": ["Reading the light, room by room, at several times of day", "Referenced palette: brand, reference and finish for each colour", "Painted or plastered samples, tested on site before any decision", "Lime plasters, concrete effects and mineral finishes", "Decorative plaster applied by Petric Sonja, or supervision of the craftsman of your choice"],
        },
    },
    {
        "id": "agencement",
        "image": "illustrations/peinture-diptyque-arches.jpg",
        "alt": {"fr": "Illustration : diptyque aux arches ocre, brun et terre cuite au-dessus d'une console en bois brut", "en": "Illustration: diptych of ochre, brown and terracotta arches above a raw wood console"},
        "illustration": True,
        "titre": {"fr": "Agencement & mise en scène", "en": "Layout & styling"},
        "resume": {"fr": "Réorganiser une pièce sans travaux de structure : circulation, place des meubles, éclairage, accrochage des œuvres et des objets.",
                   "en": "Reorganising a room without structural work: circulation, furniture placement, lighting, hanging artworks and objects."},
        "livrable": {"fr": "Plan d'agencement et planche d'ambiance", "en": "Layout plan and mood board"},
        "points": {
            "fr": ["Plan d'agencement de chaque pièce", "Planche d'ambiance : couleurs, matières, mobilier, luminaires", "Plan d'accrochage des œuvres : hauteurs, espacements, éclairage", "Ce qui reste, ce qui change, ce qui part : une liste claire", "Mise en place sur place, si vous le souhaitez"],
            "en": ["Layout plan for each room", "Mood board: colours, materials, furniture, lighting", "Hanging plan for artworks: heights, spacing, lighting", "What stays, what changes, what goes: a clear list", "Installation on site, if you wish"],
        },
    },
    {
        "id": "home-staging",
        "image": "illustrations/home-staging-salon.jpg",
        "alt": {"fr": "Illustration : salon haussmannien clair mis en scène, canapé lin, table basse en travertin, tableau terre cuite", "en": "Illustration: bright Haussmann-style living room staged with a linen sofa, travertine coffee table and terracotta painting"},
        "illustration": True,
        "titre": {"fr": "Home staging", "en": "Home staging"},
        "resume": {"fr": "Préparer un bien à la vente ou à la location pour qu'il se lise bien en photo et en visite : retirer, réordonner, corriger la couleur et la lumière.",
                   "en": "Preparing a property for sale or rental so it reads clearly in photographs and viewings: removing, rearranging, correcting colour and light."},
        "livrable": {"fr": "Liste d'actions par pièce, photos avant / après", "en": "Room-by-room action list, before / after photos"},
        "points": {
            "fr": ["Visite et liste d'actions par pièce, par ordre de priorité", "Désencombrement et réorganisation", "Rafraîchissement des murs avant les photos", "Mise en scène le jour des photos", "Photos avant / après remises au propriétaire ou à l'agence"],
            "en": ["Visit and room-by-room action list, in order of priority", "Decluttering and rearranging", "Wall refresh before the photo shoot", "Styling on the day of the shoot", "Before / after photos for the owner or the agency"],
        },
    },
    {
        "id": "sourcing",
        "image": "illustrations/peinture-toile-console.jpg",
        "alt": {"fr": "Illustration : grande toile abstraite terre cuite et ocre accrochée au-dessus d'un banc en bois, mur à la chaux", "en": "Illustration: large terracotta and ochre abstract canvas hung above a wooden bench, lime-washed wall"},
        "illustration": True,
        "titre": {"fr": "Sourcing déco & œuvres", "en": "Decor & art sourcing"},
        "resume": {"fr": "Trouver les meubles, luminaires, textiles, objets et œuvres qui manquent, chez des artisans, des galeries et des marchands, dans le budget fixé ensemble.",
                   "en": "Finding the missing furniture, lighting, textiles, objects and artworks from craftspeople, galleries and dealers, within the budget agreed together."},
        "livrable": {"fr": "Sélection argumentée, dans votre budget", "en": "A reasoned selection, within your budget"},
        "points": {
            "fr": ["Sélection de pièces avec photos, dimensions et prix", "Œuvres et pièces anciennes : état de conservation vérifié avant achat", "Commande, réception et installation", "Accrochage et éclairage des œuvres"],
            "en": ["Selection of pieces with photos, dimensions and prices", "Artworks and antiques: condition checked before purchase", "Ordering, delivery and installation", "Hanging and lighting of artworks"],
        },
    },
]

# La conservation-restauration a sa propre page ; elle sert aussi de catégorie aux projets.
CONSERVATION = {"id": "conservation", "titre": {"fr": "Conservation-restauration", "en": "Conservation"}}

# Chaque projet : fichier image dans images/realisations/ (ou "dossier/fichier" depuis images/),
# prestation (un "id" de PRESTATIONS ou "conservation"), titre, lieu anonymisé (ville ou secteur, jamais
# d'adresse) et année. Une valeur vide s'affiche « — ».
# "illustration": True = image d'ambiance (générée par IA), pas un projet de Sonja : elle ne va jamais
# au registre des projets, seulement dans la planche d'illustrations, avec la mention « Illustration ».
# Une réalisation sans image ("image": None) n'est pas affichée.
REALISATIONS = [
    {"image": "enduit-salon.jpg", "alt": {"fr": "Salon aux murs en enduit décoratif ocre clair, éclairé par deux appliques, canapé d'angle en tissu blanc cassé", "en": "Living room with pale ochre decorative plaster walls lit by two wall lights, off-white corner sofa"}, "prestation": "couleurs-matieres", "titre": {"fr": "Mur de salon en enduit décoratif", "en": "Living room wall in decorative plaster"}, "lieu": {"fr": "", "en": ""}, "annee": "", "details": {"fr": "", "en": ""}},
    {"image": "restauration-avant-apres.jpg", "alt": {"fr": "Tableau ancien avant et après restauration : un cheval blanc bâté et deux chiens dans un paysage de montagne, vernis jauni en haut, couleurs retrouvées en bas", "en": "Old painting before and after restoration: a white pack horse and two dogs in a mountain landscape, yellowed varnish above, recovered colours below"}, "entier": True, "prestation": "conservation", "titre": {"fr": "Tableau ancien, avant / après", "en": "Old painting, before / after"}, "lieu": {"fr": "", "en": ""}, "annee": "", "details": {"fr": "", "en": ""}},
    {"image": "illustrations/peinture-formes-terre-cuite.jpg", "alt": {"fr": "Illustration : toile abstraite aux grandes formes arrondies terre cuite, rose poudré et blanc cassé", "en": "Illustration: abstract canvas with large rounded shapes in terracotta, dusty pink and off-white"}, "illustration": True, "prestation": "sourcing", "titre": {"fr": "Formes en terre cuite", "en": "Terracotta shapes"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/enduit-tadelakt-salle-de-bain.jpg", "alt": {"fr": "Illustration : salle de bains entièrement en tadelakt terre cuite, vasque maçonnée, robinetterie laiton, niche en arc", "en": "Illustration: bathroom finished entirely in terracotta tadelakt, built-in basin, brass taps, arched niche"}, "illustration": True, "prestation": "couleurs-matieres", "titre": {"fr": "Salle de bains en tadelakt", "en": "Tadelakt bathroom"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/peinture-diptyque-arches.jpg", "alt": {"fr": "Illustration : diptyque aux arches ocre, brun et terre cuite au-dessus d'une console en bois brut", "en": "Illustration: diptych of ochre, brown and terracotta arches above a raw wood console"}, "illustration": True, "prestation": "agencement", "titre": {"fr": "Diptyque aux arches", "en": "Arches diptych"}, "details": {"fr": "", "en": ""}},
    {"image": "illustrations/enduit-chaux-olivier.jpg", "alt": {"fr": "Illustration : mur à la chaux sable en lumière rasante, ombre d'une branche d'olivier, jarre en terre cuite", "en": "Illustration: sand-coloured lime wall in raking light, shadow of an olive branch, terracotta jar"}, "illustration": True, "prestation": "couleurs-matieres", "titre": {"fr": "Mur à la chaux", "en": "Lime plaster wall"}, "details": {"fr": "", "en": ""}},
]

ILLUSTRATIONS_DANS_REALISATIONS = True  # True = montrer la planche d'illustrations IA sur la page Projets

PARCOURS = [
    # "annee" vide = non affichée. Ajouter ici les autres formations, expériences ou expositions.
    {"annee": "", "fr": "DNSEP (Diplôme national supérieur d'expression plastique, grade Master) mention Conservation-restauration des biens culturels, École supérieure d'art d'Avignon", "en": "DNSEP (French national higher diploma in visual arts, Master's level), Conservation-restoration of cultural property, École supérieure d'art d'Avignon"},
]

# Accueil : à qui s'adresse le travail. "page" = lien vers une page du site.
POUR_QUI = [
    {"titre": {"fr": "Particuliers", "en": "Private clients"},
     "texte": {"fr": "Une maison ou un appartement à repenser sans forcément tout refaire : couleurs, matières, agencement, œuvres.", "en": "A house or flat to rethink without necessarily redoing everything: colours, materials, layout, artworks."},
     "page": "prestations"},
    {"titre": {"fr": "Agents immobiliers", "en": "Estate agents"},
     "texte": {"fr": "Un bien préparé avant les photos et les visites, qui se lit mieux en ligne comme sur place.", "en": "A property prepared before the photos and viewings, easier to read online and in person."},
     "page": "professionnels"},
    {"titre": {"fr": "Locations saisonnières, conciergeries", "en": "Holiday rentals, concierges"},
     "texte": {"fr": "Des logements cohérents d'une saison à l'autre, simples à entretenir et à photographier.", "en": "Homes that stay consistent from one season to the next, easy to maintain and to photograph."},
     "page": "professionnels"},
    {"titre": {"fr": "Lieux professionnels", "en": "Businesses"},
     "texte": {"fr": "Boutiques, hôtels, restaurants, bureaux : une ambiance tenue, du mur à l'accrochage.", "en": "Shops, hotels, restaurants, offices: a consistent atmosphere, from the walls to the artworks."},
     "page": "professionnels"},
]

METHODE = [
    {"fr": ("Visite et écoute", "Je viens sur place. Vous me dites ce que vous attendez, ce que vous gardez, votre calendrier et votre budget."),
     "en": ("Visit and listening", "I come to the place. You tell me what you expect, what you are keeping, your timing and your budget.")},
    {"fr": ("Lecture du lieu", "La lumière à plusieurs heures, les volumes, les matériaux en place, la circulation : je regarde le lieu avant de proposer."),
     "en": ("Reading the place", "The light at different times, the volumes, the existing materials, the circulation: I look at the place before proposing anything.")},
    {"fr": ("Proposition", "Palette référencée, planche d'ambiance et plan d'agencement, avec un devis détaillé."),
     "en": ("Proposal", "Referenced palette, mood board and layout plan, with a detailed quotation.")},
    {"fr": ("Échantillons", "Les teintes et les matières sont testées sur vos murs et regardées à plusieurs heures du jour avant toute décision."),
     "en": ("Samples", "Colours and materials are tested on your walls and looked at several times of day before any decision.")},
    {"fr": ("Mise en œuvre et suivi", "Je réalise ou je suis les travaux, je mets en place le mobilier et les œuvres, puis je photographie le résultat."),
     "en": ("Implementation and follow-up", "I carry out or supervise the work, put the furniture and artworks in place, then photograph the result.")},
]

# Questions fréquentes (page Prestations, avec données structurées FAQPage). "page" = lien facultatif.
FAQ = [
    {"q": {"fr": "Faites-vous des plans ou des travaux de structure ?", "en": "Do you draw building plans or carry out structural work?"},
     "r": {"fr": "Non. Je travaille la couleur, la matière, l'agencement du mobilier, la lumière et les œuvres, sans toucher aux murs porteurs ni aux réseaux. Pour des travaux de structure, il faut un maître d'œuvre ou un architecte ; je peux travailler à ses côtés.",
           "en": "No. I work on colour, materials, furniture layout, light and artworks, without touching load-bearing walls or services. Structural work needs a project manager or an architect; I can work alongside them."}},
    {"q": {"fr": "Comment se passe la première visite ?", "en": "How does the first visit work?"},
     "r": {"fr": "Je viens voir le lieu, je vous écoute, et je regarde la lumière, les volumes et ce qui est déjà en place. Je vous envoie ensuite une proposition et un devis.",
           "en": "I come to see the place, listen to you, and look at the light, the volumes and what is already there. I then send you a proposal and a quotation."}},
    {"q": {"fr": "Combien coûte une prestation ?", "en": "How much does it cost?"},
     "r": {"fr": "Chaque projet est sur devis, établi après la première visite, selon la surface, le nombre de pièces et ce qu'il y a à faire.",
           "en": "Every project is quoted individually after the first visit, depending on the size, the number of rooms and what needs doing."}},
    {"q": {"fr": "Où intervenez-vous ?", "en": "Where do you work?"},
     "r": {"fr": "À Cannes, sur toute la Côte d'Azur (Antibes, Nice, Grasse, Saint-Tropez et alentours) et à Monaco.",
           "en": "In Cannes, across the French Riviera (Antibes, Nice, Grasse, Saint-Tropez and the surrounding area) and in Monaco."}},
    {"q": {"fr": "Travaillez-vous avec les agents immobiliers et les conciergeries ?", "en": "Do you work with estate agents and concierge services?"},
     "r": {"fr": "Oui. Je prépare les biens avant les photos et les visites, et je remets des photos avant / après à chaque projet.",
           "en": "Yes. I prepare properties before the photos and viewings, and provide before / after photos for every project."},
     "page": "professionnels"},
    {"q": {"fr": "Restaurez-vous aussi des tableaux et des objets ?", "en": "Do you also restore paintings and objects?"},
     "r": {"fr": "Oui, c'est ma formation : je suis diplômée en conservation-restauration des biens culturels. Chaque œuvre est d'abord examinée, puis fait l'objet d'un constat d'état et d'un devis.",
           "en": "Yes, it is my training: I hold a degree in the conservation-restoration of cultural property. Each work is examined first, then receives a condition report and a quotation."},
     "page": "conservation-restauration"},
]

# Page Professionnels : un bloc par type de client, puis les engagements.
PROFESSIONNELS = [
    {"id": "agents", "titre": {"fr": "Agents immobiliers", "en": "Estate agents"},
     "texte": {"fr": "Préparer un bien avant les photos et les visites : retirer, réordonner, corriger la couleur et la lumière, pour qu'il se lise du premier coup.",
               "en": "Preparing a property before the photos and viewings: removing, rearranging, correcting colour and light, so it reads at first glance."},
     "points": {"fr": ["Visite et liste d'actions par pièce, par ordre de priorité", "Home staging avant la séance photo", "Photos avant / après pour l'agence et le vendeur"],
                "en": ["Visit and room-by-room action list, in order of priority", "Home staging before the photo shoot", "Before / after photos for the agency and the seller"]}},
    {"id": "locations", "titre": {"fr": "Locations saisonnières, conciergeries", "en": "Holiday rentals, concierges"},
     "texte": {"fr": "Des logements cohérents, solides et simples à entretenir, qui se lisent bien sur les plateformes de réservation.",
               "en": "Homes that are consistent, durable and easy to maintain, and that read well on booking platforms."},
     "points": {"fr": ["Couleurs et matières choisies pour durer", "Agencement et mise en scène de chaque logement", "Sourcing du mobilier, du linge et des objets", "Rafraîchissement entre deux saisons"],
                "en": ["Colours and materials chosen to last", "Layout and styling of each home", "Sourcing of furniture, linen and objects", "Refresh between seasons"]}},
    {"id": "lieux", "titre": {"fr": "Boutiques, hôtels, restaurants, bureaux", "en": "Shops, hotels, restaurants, offices"},
     "texte": {"fr": "Une ambiance tenue dans le temps, du mur à l'accrochage, en accord avec ce que vous vendez ou servez.",
               "en": "An atmosphere that holds over time, from the walls to the artworks, in keeping with what you sell or serve."},
     "points": {"fr": ["Conseil couleurs & matières pour l'ensemble du lieu", "Agencement et accrochage d'œuvres", "Sourcing d'œuvres et d'objets", "Interventions possibles hors des heures d'ouverture, à convenir"],
                "en": ["Colour & materials advice for the whole space", "Layout and art hanging", "Sourcing of artworks and objects", "Work outside opening hours possible, by arrangement"]}},
]
ENGAGEMENTS = {
    "fr": [f"Réponse sous 48{NBSP}h", "Photos avant / après remises à chaque projet", "Discrétion : aucune adresse ni aucun propriétaire publiés", "Partenariat possible pour des projets réguliers, sur devis"],
    "en": ["Reply within 48 hours", "Before / after photos provided for every project", "Discretion: no address or owner ever published", "Partnership possible for regular projects, on quotation"],
}

# Page Conservation-restauration
PRINCIPES = {
    "fr": [("Intervention minimale", "Ne traiter que ce qui doit l'être."), ("Réversibilité", "Des matériaux que l'on peut retirer plus tard sans abîmer l'œuvre."), ("Compatibilité", "Des matériaux stables, choisis pour l'œuvre et ses matériaux d'origine."), ("Documentation", "Photographies avant, pendant et après, et un rapport écrit."), ("Respect de l'œuvre", "Son histoire et ses traces d'usage font partie d'elle.")],
    "en": [("Minimal intervention", "Treat only what needs treating."), ("Reversibility", "Materials that can be removed later without harming the work."), ("Compatibility", "Stable materials, chosen for the work and its original materials."), ("Documentation", "Photographs before, during and after, and a written report."), ("Respect for the work", "Its history and signs of use are part of it.")],
}
SERVICES_CONSERVATION = {
    "fr": [("Constat d'état", "Examen de l'œuvre et rapport écrit avec photographies : état, altérations, traitement proposé."), ("Devis", "Établi après examen, avec le détail du traitement proposé."), ("Traitement en atelier", "Nettoyage, allègement de vernis, consolidation, réintégration, selon le constat."), ("Conservation préventive", "Conseils d'accrochage, d'éclairage, d'humidité et de manipulation, chez vous.")],
    "en": [("Condition report", "Examination of the work and a written report with photographs: condition, damage, proposed treatment."), ("Quotation", "Prepared after examination, detailing the proposed treatment."), ("Studio treatment", "Cleaning, varnish reduction, consolidation, retouching, as the report requires."), ("Preventive conservation", "Advice on hanging, lighting, humidity and handling, in your home.")],
}

TEXTES = {
    "fr": {
        "descriptions": {
            "index": "Petric Sonja, direction artistique d'intérieur à Cannes : couleur, matière, agencement et home staging pour maisons, biens à vendre et lieux d'accueil, jusqu'à Monaco.",
            "projets": "Projets de Petric Sonja à Cannes et sur la Côte d'Azur : registre des réalisations, enduits décoratifs et restauration de tableaux.",
            "prestations": "Conseil couleurs et matières, agencement, home staging et sourcing d'œuvres à Cannes, sur la Côte d'Azur et à Monaco. Sur devis.",
            "professionnels": "Home staging et mise en scène pour agents immobiliers, conciergeries, locations saisonnières, boutiques et hôtels, de Cannes à Monaco.",
            "conservation-restauration": "Conservation-restauration d'œuvres pour collectionneurs particuliers par Petric Sonja, diplômée DNSEP (École supérieure d'art d'Avignon). Cannes.",
            "a-propos": "Petric Sonja, diplômée en conservation-restauration des biens culturels (DNSEP, Avignon), porte un regard de restauratrice sur les intérieurs.",
            "contact": "Parlez de votre projet à Petric Sonja : formulaire, e-mail, téléphone ou WhatsApp. Basée à Cannes, sur la Côte d'Azur et à Monaco.",
            "confidentialite": "Comment Petric Sonja traite les informations envoyées par le formulaire de contact du site petricsonja.art.",
            "mentions-legales": "Mentions légales du site petricsonja.art : éditrice, hébergeur, propriété intellectuelle et crédits.",
        },
        "nav": {"index": "Accueil", "projets": "Projets", "prestations": "Prestations", "professionnels": "Professionnels", "conservation-restauration": "Conservation-restauration", "a-propos": "À propos", "contact": "Contact"},
        "titres": {
            "index": "Petric Sonja · Direction artistique d'intérieur à Cannes",
            "projets": "Projets · Petric Sonja",
            "prestations": "Prestations · Petric Sonja",
            "professionnels": "Professionnels · Petric Sonja",
            "conservation-restauration": "Conservation-restauration · Petric Sonja",
            "a-propos": "À propos · Petric Sonja",
            "contact": "Contact et devis · Petric Sonja",
            "confidentialite": "Confidentialité · Petric Sonja",
            "mentions-legales": "Mentions légales · Petric Sonja",
        },
        "menu": "Menu",
        "droits": "Tous droits réservés.",
        "meta_lieu": "Cannes · Côte d'Azur · Monaco",
        "metier": "Direction artistique d'intérieur",
        "manifeste": ["Regarder un lieu", "comme une œuvre."],
        "accroche": "Couleur, matière, lumière et agencement pour les maisons, les biens à vendre et les lieux d'accueil, de Cannes à Monaco.",
        "devis": "Parler de votre projet",
        "voir_projets": "Voir les projets",
        "photo_principale": "Portrait de Petric Sonja",
        "portrait_alt": "Portrait en noir et blanc de Petric Sonja, cheveux longs, pull à col roulé sombre",
        "prestations": "Prestations",
        "prestations_intro": "Quatre façons d'intervenir, seules ou ensemble. Chacune commence par une visite et se termine par un résultat que vous pouvez voir et garder.",
        "toutes_prestations": "Le détail des prestations →",
        "livrable": "Livrable",
        "livrables": "Ce que vous recevez",
        "pour_qui": "Pour qui",
        "methode": "Méthode",
        "faq": "Questions fréquentes",
        "projets": "Projets",
        "projets_intro": "Le registre des projets réels, avec leur lieu (ville ou secteur, jamais d'adresse) et leur année. Les images d'ambiance sont rangées à part, dans la planche d'illustrations.",
        "registre": "Registre",
        "col_num": "N°",
        "col_projet": "Projet",
        "col_lieu": "Lieu",
        "col_prestation": "Prestation",
        "col_annee": "Année",
        "tous_projets": "Tous les projets →",
        "planche": "Planche d'illustrations",
        "planche_texte": "Images d'ambiance générées par intelligence artificielle, pour montrer une direction : ce ne sont pas des projets de Petric Sonja.",
        "cta_titre": "Un projet en tête ?",
        "cta_texte": f"Décrivez votre lieu en quelques lignes : je vous réponds sous 48{NBSP}h pour convenir d'une première visite.",
        "vue_grand": "Projet en grand",
        "fermer": "Fermer",
        "precedente": "Précédente",
        "suivante": "Suivante",
        "a_propos": "À propos",
        "bio": "Petric Sonja est diplômée en conservation-restauration des biens culturels (DNSEP, grade Master, École supérieure d'art d'Avignon). Elle y a appris à regarder une œuvre avant d'y toucher : comprendre ses matériaux, son histoire, ce qui l'abîme et ce qui la tient.",
        "bio_demarche": "Elle porte ce regard sur les intérieurs. Avant de proposer une couleur ou de déplacer un meuble, elle observe la lumière, les matières déjà en place et la façon dont le lieu est vécu. Ses propositions sont sobres : changer ce qui doit l'être, garder ce qui tient.",
        "bio_peinture": "Elle peint aussi : des toiles contemporaines aux lignes épurées.",
        "parcours": "Parcours",
        "zone": "Basée à Cannes. Intervient sur toute la Côte d'Azur (Antibes, Nice, Grasse, Saint-Tropez et alentours) et à Monaco.",
        "diplome_ligne": "Diplômée en conservation-restauration des biens culturels (DNSEP, École supérieure d'art d'Avignon). Le même principe guide chaque intérieur : comprendre avant d'intervenir.",
        "voir_conservation": "La conservation-restauration →",
        "voir_professionnels": "Pour les professionnels →",
        "pro_titre": "Pour les professionnels",
        "pro_intro": "Agents immobiliers, conciergeries, propriétaires de locations saisonnières, boutiques, hôtels et restaurants : je prépare et je mets en scène vos lieux, de Cannes à Monaco.",
        "engagements": "Engagements",
        "cons_titre": "Conservation-restauration",
        "cons_intro": "Conservatrice-restauratrice diplômée (DNSEP, École supérieure d'art d'Avignon), j'interviens pour les collectionneurs particuliers sur les œuvres qui comptent pour eux.",
        "principes": "Principes",
        "interventions": "Interventions",
        "champ_titre": "Quelles œuvres ?",
        "champ": "Peintures, art contemporain, sculptures et objets, œuvres sur papier : chaque demande est examinée, et je vous dis franchement si elle relève de mes compétences ou d'un autre spécialiste.",
        "contact": "Contact",
        "ecrivez": "Parlons de votre projet",
        "contact_intro": f"Décrivez votre lieu et votre projet. Je vous réponds sous 48{NBSP}h.",
        "email": "E-mail",
        "telephone": "Téléphone",
        "nom": "Nom",
        "type_projet": "Type de demande",
        "profil": "Vous êtes",
        "bien": "Type de bien (villa, appartement, boutique…)",
        "surface": "Surface approximative, en m² (facultatif)",
        "echeance": "Échéance (vente, location, saison, ouverture…)",
        "facultatif": "facultatif",
        "photos_titre": "Vous avez des photos ?",
        "photos_texte": "Envoyez-les après votre demande par WhatsApp ou par e-mail. Pour une pièce : une vue d'ensemble prise depuis l'entrée, en lumière du jour et sans flash, puis un détail des murs et du sol. Pour une œuvre : de face et en entier, puis un détail des zones abîmées.",
        "consentement": "J'accepte que ces informations servent à répondre à ma demande.",
        "votre_projet": "Votre projet",
        "message": "Votre projet en quelques lignes",
        "envoyer": "Envoyer la demande",
        "telephone_facultatif": "Téléphone (facultatif)",
        "ville": "Ville du projet",
        "envoi": "Envoi en cours…",
        "merci": f"Votre demande est bien arrivée. Je vous réponds sous 48{NBSP}h.",
        "erreur": "L'envoi n'a pas abouti. Vous pouvez m'écrire directement à",
        "pas_actif": "Le formulaire sera bientôt actif. En attendant, écrivez-moi à",
        "sujet": "Nouvelle demande de devis depuis petricsonja.art",
        "copier": "Copier",
        "copie": "Copié",
        "image_a_venir": "Image à venir",
        "illustration": "Illustration",
        "echap": "Échap",
        "lieu": "Cannes, Côte d'Azur",
        "fermer_menu": "Fermer",
        "aller_contenu": "Aller au contenu",
        "atelier_libelle": "Atelier",
        "confidentialite": "Confidentialité",
        "mentions_legales": "Mentions légales",
        "og_locale": "fr_FR",
        "theme_sombre": "Sombre",
        "theme_clair": "Clair",
        "exemple": "Exemple — ne pas publier",
        "etude_contexte": "Le lieu",
        "etude_demande": "La demande",
        "etude_intervention": "L'intervention",
        "etude_materiaux": "Matières et teintes",
        "etude_fiche": "Fiche",
    },
    "en": {
        "descriptions": {
            "index": "Petric Sonja, interior art direction in Cannes: colour, materials, layout and home staging for homes, properties for sale and hospitality spaces, as far as Monaco.",
            "projets": "Projects by Petric Sonja in Cannes and on the French Riviera: project register, decorative plaster and painting restoration.",
            "prestations": "Colour and materials advice, layout, home staging and art sourcing in Cannes, on the French Riviera and in Monaco. On quotation.",
            "professionnels": "Home staging and styling for estate agents, concierge services, holiday rentals, shops and hotels, from Cannes to Monaco.",
            "conservation-restauration": "Conservation of artworks for private collectors by Petric Sonja, DNSEP graduate in conservation-restoration (École supérieure d'art d'Avignon). Cannes.",
            "a-propos": "Petric Sonja, trained in the conservation-restoration of cultural property (DNSEP, Avignon), brings a conservator's eye to interiors.",
            "contact": "Tell Petric Sonja about your project: form, email, phone or WhatsApp. Based in Cannes, working across the French Riviera and Monaco.",
            "confidentialite": "How Petric Sonja handles the information sent through the contact form on petricsonja.art.",
            "mentions-legales": "Legal notice for petricsonja.art: publisher, host, intellectual property and credits.",
        },
        "nav": {"index": "Home", "projets": "Projects", "prestations": "Services", "professionnels": "Professionals", "conservation-restauration": "Conservation", "a-propos": "About", "contact": "Contact"},
        "titres": {
            "index": "Petric Sonja · Interior art direction in Cannes",
            "projets": "Projects · Petric Sonja",
            "prestations": "Services · Petric Sonja",
            "professionnels": "Professionals · Petric Sonja",
            "conservation-restauration": "Conservation · Petric Sonja",
            "a-propos": "About · Petric Sonja",
            "contact": "Contact and quotes · Petric Sonja",
            "confidentialite": "Privacy · Petric Sonja",
            "mentions-legales": "Legal notice · Petric Sonja",
        },
        "menu": "Menu",
        "droits": "All rights reserved.",
        "meta_lieu": "Cannes · French Riviera · Monaco",
        "metier": "Interior art direction",
        "manifeste": ["Look at a room", "as you would a painting."],
        "accroche": "Colour, materials, light and layout for homes, properties for sale and hospitality spaces, from Cannes to Monaco.",
        "devis": "Discuss your project",
        "voir_projets": "See the projects",
        "photo_principale": "Portrait of Petric Sonja",
        "portrait_alt": "Black and white portrait of Petric Sonja, long hair, dark roll-neck jumper",
        "prestations": "Services",
        "prestations_intro": "Four ways of working, alone or together. Each one starts with a visit and ends with a result you can see and keep.",
        "toutes_prestations": "Services in detail →",
        "livrable": "Deliverable",
        "livrables": "What you receive",
        "pour_qui": "Who it is for",
        "methode": "Method",
        "faq": "Frequently asked questions",
        "projets": "Projects",
        "projets_intro": "The register of real projects, with their location (town or area, never an address) and year. Mood images are kept apart, in the illustration plate.",
        "registre": "Register",
        "col_num": "No.",
        "col_projet": "Project",
        "col_lieu": "Location",
        "col_prestation": "Service",
        "col_annee": "Year",
        "tous_projets": "All projects →",
        "planche": "Illustration plate",
        "planche_texte": "AI-generated mood images, used to show a direction: they are not projects by Petric Sonja.",
        "cta_titre": "Have a project in mind?",
        "cta_texte": "Describe your place in a few lines: I will reply within 48 hours to arrange a first visit.",
        "vue_grand": "Enlarged project",
        "fermer": "Close",
        "precedente": "Previous",
        "suivante": "Next",
        "a_propos": "About",
        "bio": "Petric Sonja holds a degree in the conservation-restoration of cultural property (DNSEP, Master's level, École supérieure d'art d'Avignon). There she learned to look at a work before touching it: to understand its materials, its history, what damages it and what holds it together.",
        "bio_demarche": "She brings the same eye to interiors. Before suggesting a colour or moving a piece of furniture, she observes the light, the materials already in place and the way the space is lived in. Her proposals are restrained: change what needs changing, keep what holds.",
        "bio_peinture": "She also paints: contemporary canvases with clean lines.",
        "parcours": "Background",
        "zone": "Based in Cannes. Works across the French Riviera (Antibes, Nice, Grasse, Saint-Tropez and the surrounding area) and in Monaco.",
        "diplome_ligne": "Trained in the conservation-restoration of cultural property (DNSEP, École supérieure d'art d'Avignon). The same principle guides every interior: understand before intervening.",
        "voir_conservation": "Conservation →",
        "voir_professionnels": "For professionals →",
        "pro_titre": "For professionals",
        "pro_intro": "Estate agents, concierge services, holiday rental owners, shops, hotels and restaurants: I prepare and style your spaces, from Cannes to Monaco.",
        "engagements": "Commitments",
        "cons_titre": "Conservation",
        "cons_intro": "A qualified conservator-restorer (DNSEP, École supérieure d'art d'Avignon), I work for private collectors on the works that matter to them.",
        "principes": "Principles",
        "interventions": "Services",
        "champ_titre": "Which works?",
        "champ": "Paintings, contemporary art, sculptures and objects, works on paper: every request is examined, and I will tell you plainly whether it is within my expertise or calls for another specialist.",
        "contact": "Contact",
        "ecrivez": "Let's talk about your project",
        "contact_intro": "Describe your place and your project. I reply within 48 hours.",
        "email": "Email",
        "telephone": "Phone",
        "nom": "Name",
        "type_projet": "Type of request",
        "profil": "You are",
        "bien": "Type of property (villa, flat, shop…)",
        "surface": "Approximate size, in m² (optional)",
        "echeance": "Timing (sale, rental, season, opening…)",
        "facultatif": "optional",
        "photos_titre": "Do you have photos?",
        "photos_texte": "Send them after your request by WhatsApp or email. For a room: one wide shot from the doorway in daylight, without flash, then a detail of the walls and floor. For an artwork: straight on and in full, then a detail of the damaged areas.",
        "consentement": "I agree that this information is used to reply to my request.",
        "votre_projet": "Your project",
        "message": "Your project in a few lines",
        "envoyer": "Send request",
        "telephone_facultatif": "Phone (optional)",
        "ville": "Project location",
        "envoi": "Sending…",
        "merci": "Your request has arrived. I will reply within 48 hours.",
        "erreur": "The request could not be sent. You can email me directly at",
        "pas_actif": "The form will be active soon. In the meantime, email me at",
        "sujet": "New quote request from petricsonja.art",
        "copier": "Copy",
        "copie": "Copied",
        "image_a_venir": "Image to come",
        "illustration": "Illustration",
        "echap": "Esc",
        "lieu": "Cannes, French Riviera",
        "fermer_menu": "Close",
        "aller_contenu": "Skip to content",
        "atelier_libelle": "Studio",
        "confidentialite": "Privacy",
        "mentions_legales": "Legal notice",
        "og_locale": "en_GB",
        "theme_sombre": "Dark",
        "theme_clair": "Light",
        "exemple": "Example — do not publish",
        "etude_contexte": "The place",
        "etude_demande": "The brief",
        "etude_intervention": "The work",
        "etude_materiaux": "Materials and colours",
        "etude_fiche": "Facts",
    },
}


# Formulaire de projet : types de demande et profils proposés
DEMANDES = {
    "fr": ["Couleurs & matières", "Agencement & mise en scène", "Home staging", "Sourcing déco & œuvres", "Conservation-restauration d'une œuvre", "Autre"],
    "en": ["Colour & materials", "Layout & styling", "Home staging", "Decor & art sourcing", "Artwork conservation", "Other"],
}
PROFILS = {
    "fr": ["Particulier", "Agent immobilier", "Location saisonnière, conciergerie", "Lieu professionnel (boutique, hôtel, restaurant, bureau)", "Collectionneur"],
    "en": ["Private client", "Estate agent", "Holiday rental, concierge", "Business (shop, hotel, restaurant, office)", "Collector"],
}

# Pages du menu, dans l'ordre. L'accueil est le logo.
NAV = ["projets", "prestations", "a-propos", "contact"]
PAGES = ["index", "projets", "prestations", "professionnels", "conservation-restauration", "a-propos", "contact"]
# Pages hors menu, liées depuis le pied de page. Les mentions légales attendent le SIRET.
PAGES_LEGALES = ["confidentialite"] + (["mentions-legales"] if SIRET else [])
# Adresse de chaque page dans chaque langue (sans .html). Une page absente garde son nom interne.
SLUGS = {
    "fr": {},
    "en": {"projets": "projects", "prestations": "services", "professionnels": "professionals", "conservation-restauration": "conservation",
           "a-propos": "about", "confidentialite": "privacy", "mentions-legales": "legal"},
}

LEGAL = {
    "fr": {
        "confidentialite": f"""## Responsable du traitement
Petric Sonja, Cannes. Contact : {EMAIL}.

## Informations collectées
Le formulaire de contact recueille votre nom, votre e-mail, votre téléphone (facultatif), le type de demande, votre profil, le type de bien, la ville, la surface et l'échéance du projet, votre message et votre accord. Rien d'autre n'est collecté.

## Pourquoi
Uniquement pour répondre à votre demande et, si vous le souhaitez, établir un devis. Base légale : les mesures précontractuelles prises à votre demande (article 6.1.b du RGPD).

## Qui les reçoit
Petric Sonja seule. Le message est acheminé par e-mail par le service Web3Forms. Le site est hébergé par Vercel. Vos informations ne sont ni vendues ni cédées.

## Combien de temps
Au plus 3 ans après notre dernier échange, puis elles sont supprimées.

## Cookies
Ce site ne dépose aucun cookie et n'utilise aucun outil de mesure d'audience ni de publicité.

## Vos droits
Vous pouvez demander l'accès à vos informations, leur rectification, leur effacement, la limitation du traitement ou vous y opposer en écrivant à {EMAIL}. Vous pouvez aussi saisir la CNIL (www.cnil.fr).""",
        "mentions-legales": f"""## Éditrice
Petric Sonja, {STATUT["fr"]}. SIRET : {SIRET}. Adresse : {ADRESSE or "Cannes, sur rendez-vous"}. E-mail : {EMAIL}. Téléphone : {TELEPHONE}.

Directrice de la publication : Petric Sonja.

## Hébergeur
Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis. vercel.com.

## Propriété intellectuelle
Les textes et les photographies de ce site sont la propriété de Petric Sonja, sauf mention contraire. Toute reproduction sans accord écrit est interdite.

## Crédits
Les images marquées « Illustration » sont des images d'ambiance générées par intelligence artificielle : ce ne sont pas des réalisations de Petric Sonja.""",
    },
    "en": {
        "confidentialite": f"""## Data controller
Petric Sonja, Cannes. Contact: {EMAIL}.

## What is collected
The contact form collects your name, email, phone number (optional), the type of request, your profile, the type of property, the project location, size and timing, your message and your consent. Nothing else is collected.

## Why
Only to reply to your request and, if you wish, to prepare a quotation. Legal basis: pre-contractual steps taken at your request (Article 6(1)(b) GDPR).

## Who receives it
Petric Sonja alone. The message is delivered by email through the Web3Forms service. The site is hosted by Vercel. Your information is never sold or shared.

## How long
No more than 3 years after our last exchange, after which it is deleted.

## Cookies
This site sets no cookies and uses no analytics or advertising tools.

## Your rights
You may ask to access, correct or erase your information, restrict its use or object to it by writing to {EMAIL}. You may also contact the French data protection authority, the CNIL (www.cnil.fr).""",
        "mentions-legales": f"""## Publisher
Petric Sonja, {STATUT["en"]}. SIRET: {SIRET}. Address: {ADRESSE or "Cannes, by appointment"}. Email: {EMAIL}. Phone: {TELEPHONE}.

Publication director: Petric Sonja.

## Host
Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, United States. vercel.com.

## Intellectual property
The texts and photographs on this site belong to Petric Sonja unless stated otherwise. No reproduction without written consent.

## Credits
Images marked "Illustration" are AI-generated mood images: they are not projects by Petric Sonja.""",
    },
}
LARGEURS = [640, 1024, 1600]  # tailles générées pour chaque image (AVIF et WebP)


def slug(langue, page):
    return SLUGS.get(langue, {}).get(page, page)


def chemin(langue, page):
    """Adresse d'une page depuis la racine du site, sans .html (cleanUrls de Vercel)."""
    if langue == LANGUES[0]:
        return "/" if page == "index" else f"/{slug(langue, page)}"
    return f"/{langue}" if page == "index" else f"/{langue}/{slug(langue, page)}"


def fichier_image(nom):
    """Chemin depuis images/ : les noms simples sont dans images/realisations/."""
    return nom if "/" in nom else f"realisations/{nom}"


def projets_reels():
    return [r for r in REALISATIONS if r["image"] and not r.get("illustration")]


def illustrations():
    return [r for r in REALISATIONS if r["image"] and r.get("illustration")] if ILLUSTRATIONS_DANS_REALISATIONS else []


def num(n, chiffres=3):
    return str(n).zfill(chiffres)


def nom_prestation(id_, langue):
    if id_ == CONSERVATION["id"]:
        return CONSERVATION["titre"][langue]
    return next(p["titre"][langue] for p in PRESTATIONS if p["id"] == id_)


def lien_prestation(id_, langue):
    if id_ == CONSERVATION["id"]:
        return chemin(langue, "conservation-restauration")
    return f'{chemin(langue, "prestations")}#{id_}'


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


def oeuvre(r, n, t, langue, tailles):
    if r["image"]:
        visuel = picture(fichier_image(r["image"]), r.get("alt", r["titre"])[langue], tailles)
    else:
        visuel = attente(t)
    mention = t["illustration"] if r.get("illustration") else ""
    lieu = r.get("lieu", {}).get(langue, "")
    details = " · ".join(x for x in (mention or nom_prestation(r["prestation"], langue), lieu, r.get("annee", ""), r["details"][langue]) if x)
    ouvrable = ' data-ouvrable tabindex="0" role="button"' if r["image"] else ""
    return f'''<figure class="oeuvre" data-categorie="{r["prestation"]}" data-numero="{num(n)}"{ouvrable} data-reveal>
          <div class="oeuvre-image">{visuel}</div>
          <figcaption class="cartel mono"><span class="cartel-num">{num(n)}</span><span class="cartel-titre">{escape(r["titre"][langue])}</span><span class="cartel-details">{escape(details)}</span></figcaption>
        </figure>'''


def registre(t, langue):
    """Tableau des projets réels : N° | Projet | Lieu | Prestation | Année. Une case vide s'affiche « — »."""
    lignes = "\n".join(
        f'''          <tr>
            <td class="mono r-num">{num(n)}</td>
            <th scope="row" class="r-projet">{escape(r["titre"][langue])}</th>
            <td class="r-lieu"><span class="r-etiquette mono">{t["col_lieu"]}</span>{escape(r.get("lieu", {}).get(langue, "") or "—")}</td>
            <td class="r-prestation"><span class="r-etiquette mono">{t["col_prestation"]}</span><a class="lien" href="{lien_prestation(r["prestation"], langue)}">{nom_prestation(r["prestation"], langue)}</a></td>
            <td class="mono r-annee"><span class="r-etiquette">{t["col_annee"]}</span>{r.get("annee") or "—"}</td>
          </tr>''' for n, r in enumerate(projets_reels(), 1)
    )
    return f'''<table class="registre" data-reveal>
          <thead class="mono"><tr><th scope="col">{t["col_num"]}</th><th scope="col">{t["col_projet"]}</th><th scope="col">{t["col_lieu"]}</th><th scope="col">{t["col_prestation"]}</th><th scope="col">{t["col_annee"]}</th></tr></thead>
          <tbody>
{lignes}
          </tbody>
        </table>'''


def appel_devis(t, langue, numero):
    return f'''    <section class="section appel grille">
      <div class="col-entete">{entete_section(numero, t["contact"])}</div>
      <div class="col-principale">
        {titre_masque("h2", t["cta_titre"], "titre-xl")}
        <p class="texte-large" data-reveal>{t["cta_texte"]}</p>
        <p data-reveal><a class="lien-fort accent" href="{chemin(langue, "contact")}">{t["devis"]} <span aria-hidden="true">→</span></a></p>
      </div>
    </section>'''


def liste_numerotee(elements, classe):
    """Liste de paires (titre, texte) numérotées : méthode, principes, interventions."""
    return f'<ol class="{classe}">\n' + "\n".join(
        f'          <li data-reveal><span class="mono num">{num(n, 2)}</span><h3 class="titre-s">{titre}</h3><p>{texte}</p></li>'
        for n, (titre, texte) in enumerate(elements, 1)
    ) + "\n        </ol>"


def corps_index(t, langue):
    lignes = "\n".join(
        f'''        <li class="ligne-prestation" data-reveal>
          <a href="{chemin(langue, "prestations")}#{p["id"]}">
            <span class="mono num">{num(n, 2)}</span>
            <span class="lp-titre">{p["titre"][langue]}</span>
            <span class="lp-resume"><span class="mono">{t["livrable"]}</span> {p["livrable"][langue]}</span>
            <span class="mono lp-fleche" aria-hidden="true">→</span>
          </a>
        </li>''' for n, p in enumerate(PRESTATIONS, 1)
    )
    pour_qui = "\n".join(
        f'''          <li data-reveal><h3 class="titre-s">{p["titre"][langue]}</h3><p>{p["texte"][langue]}</p><a class="lien mono" href="{chemin(langue, p["page"])}">{t["nav"][p["page"]]} →</a></li>'''
        for p in POUR_QUI
    )
    reels = projets_reels()
    recentes = "\n".join(oeuvre(r, n, t, langue, "(max-width: 760px) 100vw, 50vw") for n, r in enumerate(reels[:3], 1))
    portrait = picture(PHOTO_ACCUEIL, t["portrait_alt"], "(max-width: 760px) 100vw, 40vw", prioritaire=True) if PHOTO_ACCUEIL else attente(t)
    manifeste = "".join(f'<span class="ligne"><span>{x}</span></span>' for x in t["manifeste"])
    return f'''    <section class="hero grille">
      <p class="hero-meta mono" data-reveal><span>{num(1)}</span><span>{t["meta_lieu"]}</span></p>
      <h1 class="hero-titre" data-reveal="masque"><span class="hero-qui mono">Petric Sonja — {t["metier"]}</span><span class="hero-manifeste">{manifeste}</span></h1>
      <div class="hero-texte">
        <p class="texte-large" data-reveal>{t["accroche"]}</p>
        <p class="actions" data-reveal><a class="lien-fort accent" href="{chemin(langue, "contact")}">{t["devis"]} <span aria-hidden="true">→</span></a><a class="lien-fort" href="{chemin(langue, "projets")}">{t["voir_projets"]} <span aria-hidden="true">→</span></a></p>
      </div>
      <figure class="hero-portrait" data-reveal>
        <div class="hero-image">{portrait}</div>
        <figcaption class="cartel mono"><span class="cartel-titre">Petric Sonja</span><span class="cartel-details">{t["photo_principale"]}</span></figcaption>
      </figure>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(2, t["prestations"])}<p class="mono" data-reveal><a class="lien" href="{chemin(langue, "prestations")}">{t["toutes_prestations"]}</a></p></div>
      <div class="col-large">
        <ul class="liste-prestations">
{lignes}
        </ul>
      </div>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(3, t["pour_qui"])}</div>
      <div class="col-large">
        <ul class="pour-qui">
{pour_qui}
        </ul>
      </div>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(4, t["methode"])}</div>
      <div class="col-large">
        {liste_numerotee([m[langue] for m in METHODE], "etapes")}
      </div>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(5, t["projets"])}<p class="mono" data-reveal><a class="lien" href="{chemin(langue, "projets")}">{t["tous_projets"]}</a></p></div>
      <div class="col-large">
        {registre(t, langue)}
      </div>
      <div class="col-large galerie galerie-accueil">
        {recentes}
      </div>
    </section>

    <section class="section grille">
      <div class="col-principale diplome">
        <p class="texte-large" data-reveal>{t["diplome_ligne"]}</p>
        <p class="mono" data-reveal><a class="lien" href="{chemin(langue, "conservation-restauration")}">{t["voir_conservation"]}</a></p>
      </div>
    </section>

{appel_devis(t, langue, 6)}'''


def figure_prestation(p, t, langue):
    if not p.get("image"):
        return attente(t)
    visuel = picture(fichier_image(p["image"]), p["alt"][langue], "(max-width: 760px) 100vw, 45vw")
    legende = f'<figcaption class="cartel mono"><span class="cartel-titre">{t["illustration"]}</span></figcaption>' if p.get("illustration") else ""
    return visuel + legende


def corps_prestations(t, langue):
    blocs = []
    for n, p in enumerate(PRESTATIONS, 1):
        points = "\n".join(f"            <li>{x}</li>" for x in p["points"][langue])
        blocs.append(f'''      <article class="prestation grille{" inverse" if n % 2 == 0 else ""}" id="{p["id"]}">
        <p class="mono num prestation-num" data-reveal>{num(n, 2)} / {num(len(PRESTATIONS), 2)}</p>
        <div class="prestation-texte">
          {titre_masque("h2", p["titre"][langue], "titre-l")}
          <p class="texte-large" data-reveal>{p["resume"][langue]}</p>
          <p class="mono faible-texte" data-reveal>{t["livrables"]}</p>
          <ul class="liste-mono mono" data-reveal>
{points}
          </ul>
          <p class="mono sur-devis" data-reveal>{SUR_DEVIS[langue]}</p>
        </div>
        <figure class="prestation-image" data-reveal>{figure_prestation(p, t, langue)}</figure>
      </article>''')
    faq = "\n".join(
        f'''          <details class="question" data-reveal>
            <summary><span class="titre-s">{q["q"][langue]}</span><span class="mono plus" aria-hidden="true">+</span></summary>
            <div class="reponse"><p>{q["r"][langue]}</p>{f'<p class="mono"><a class="lien" href="{chemin(langue, q["page"])}">{t["nav"][q["page"]]} →</a></p>' if q.get("page") else ""}</div>
          </details>''' for q in FAQ
    )
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["prestations"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["prestations"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["prestations_intro"]}</p>
      </div>
    </section>
{chr(10).join(blocs)}

    <section class="section grille">
      <div class="col-entete">{entete_section(2, t["faq"])}</div>
      <div class="col-large faq">
{faq}
      </div>
    </section>

{appel_devis(t, langue, 3)}'''


def corps_projets(t, langue):
    reels = projets_reels()
    items = "\n        ".join(oeuvre(r, n, t, langue, "(max-width: 760px) 100vw, 50vw") for n, r in enumerate(reels, 1))
    planche = ""
    if illustrations():
        dessins = "\n        ".join(oeuvre(r, n, t, langue, "(max-width: 760px) 100vw, 50vw") for n, r in enumerate(illustrations(), len(reels) + 1))
        planche = f'''
    <section class="section grille planche">
      <div class="col-entete">{entete_section(2, t["planche"])}</div>
      <div class="col-large"><p data-reveal class="faible-texte">{t["planche_texte"]}</p></div>
      <div class="galerie galerie-complete">
        {dessins}
      </div>
    </section>'''
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["registre"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["projets"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["projets_intro"]}</p>
      </div>
    </section>
    <section class="section-galerie grille">
      <div class="col-large">
        {registre(t, langue)}
      </div>
      <div class="galerie galerie-complete">
        {items}
      </div>
    </section>{planche}

{appel_devis(t, langue, 3)}'''


def corps_professionnels(t, langue):
    blocs = "\n".join(
        f'''      <article class="pro grille" id="{p["id"]}">
        <p class="mono num prestation-num" data-reveal>{num(n, 2)} / {num(len(PROFESSIONNELS), 2)}</p>
        <div class="pro-texte">
          {titre_masque("h2", p["titre"][langue], "titre-l")}
          <p class="texte-large" data-reveal>{p["texte"][langue]}</p>
        </div>
        <ul class="liste-mono mono pro-points" data-reveal>
{chr(10).join(f"          <li>{x}</li>" for x in p["points"][langue])}
        </ul>
      </article>''' for n, p in enumerate(PROFESSIONNELS, 1)
    )
    engagements = "\n".join(f"          <li data-reveal>{x}</li>" for x in ENGAGEMENTS[langue])
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["nav"]["professionnels"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["pro_titre"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["pro_intro"]}</p>
      </div>
    </section>
{blocs}

    <section class="section grille">
      <div class="col-entete">{entete_section(2, t["engagements"])}</div>
      <div class="col-large">
        <ul class="engagements">
{engagements}
        </ul>
        <p class="mono sur-devis" data-reveal>{SUR_DEVIS[langue]}</p>
      </div>
    </section>

{appel_devis(t, langue, 3)}'''


def corps_conservation(t, langue):
    exemple = next((r for r in REALISATIONS if r["prestation"] == CONSERVATION["id"] and r["image"]), None)
    figure = ""
    if exemple:
        figure = f'''
    <section class="section grille">
      <figure class="col-large conservation-image" data-reveal>{picture(fichier_image(exemple["image"]), exemple["alt"][langue], "(max-width: 760px) 100vw, 70vw")}<figcaption class="cartel mono"><span class="cartel-titre">{escape(exemple["titre"][langue])}</span></figcaption></figure>
    </section>'''
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["cons_titre"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["cons_titre"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["cons_intro"]}</p>
      </div>
    </section>{figure}

    <section class="section grille">
      <div class="col-entete">{entete_section(2, t["principes"])}</div>
      <div class="col-large">
        {liste_numerotee(PRINCIPES[langue], "etapes")}
      </div>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(3, t["interventions"])}</div>
      <div class="col-large">
        {liste_numerotee(SERVICES_CONSERVATION[langue], "etapes")}
        <p class="mono sur-devis" data-reveal>{SUR_DEVIS[langue]}</p>
      </div>
    </section>

    <section class="section grille">
      <div class="col-entete">{entete_section(4, t["champ_titre"])}</div>
      <div class="col-principale">
        <p class="texte-large" data-reveal>{t["champ"]}</p>
      </div>
    </section>

{appel_devis(t, langue, 5)}'''


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
        f'          <li data-reveal><span class="mono annee">{e["annee"] or "—"}</span><span>{e[langue]}</span></li>' for e in PARCOURS if "[" not in e[langue]
    )
    portrait = picture(PHOTO_ACCUEIL, t["portrait_alt"], "(max-width: 760px) 100vw, 35vw") if PHOTO_ACCUEIL else attente(t)
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["a_propos"])}</div>
      <div class="col-large">
        {titre_masque("h1", "Petric Sonja", "titre-xxl nom")}
        <p class="mono intro faible-texte" data-reveal>{t["metier"]}</p>
      </div>
    </section>
    <section class="section apropos grille">
      <figure class="apropos-portrait" data-reveal>{portrait}<figcaption class="cartel mono"><span class="cartel-titre">Petric Sonja</span><span class="cartel-details">{t["lieu"]}</span></figcaption></figure>
      <div class="apropos-texte">
        <p class="texte-large" data-reveal>{t["bio"]}</p>
        <p data-reveal>{t["bio_demarche"]}</p>
        <p data-reveal>{t["bio_peinture"]}</p>
        <p class="mono faible-texte" data-reveal>{t["zone"]}</p>
        <p class="mono liens-suite" data-reveal><a class="lien" href="{chemin(langue, "conservation-restauration")}">{t["voir_conservation"]}</a><a class="lien" href="{chemin(langue, "professionnels")}">{t["voir_professionnels"]}</a></p>
        <h2 class="mono index-section" data-reveal><span>—</span><span>{t["parcours"]}</span></h2>
        <ul class="parcours">
{lignes}
        </ul>
      </div>
    </section>

{appel_devis(t, langue, 2)}'''


def corps_contact(t, langue):
    def options(liste):
        return "\n".join(f"              <option>{escape(x)}</option>" for x in liste)
    tel = f'\n          <li><span class="mono etiquette">{t["telephone"]}</span><a class="lien" href="tel:{TELEPHONE.replace(" ", "")}">{TELEPHONE}</a></li>' if TELEPHONE else ""
    whatsapp = f'        <li><span class="mono etiquette">WhatsApp</span><a class="lien" href="https://wa.me/{WHATSAPP}" rel="noopener">{TELEPHONE}</a></li>' if WHATSAPP else ""
    if SERVICE_FORMULAIRE == "formspree":
        adresse, caches = f"https://formspree.io/f/{CLE_FORMULAIRE}", f'        <input type="hidden" name="_subject" value="{t["sujet"]}">'
    else:
        adresse = "https://api.web3forms.com/submit"
        caches = (f'        <input type="hidden" name="access_key" value="{CLE_FORMULAIRE}">\n'
                  f'        <input type="hidden" name="subject" value="{t["sujet"]}">\n'
                  '        <input type="hidden" name="from_name" value="petricsonja.art">')
    return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["contact"])}</div>
      <div class="col-large">
        {titre_masque("h1", t["ecrivez"], "titre-xxl")}
        <p class="texte-large intro" data-reveal>{t["contact_intro"]}</p>
      </div>
    </section>
    <section class="section contact grille">
      <ul class="coordonnees" data-reveal>
        <li><span class="mono etiquette">{t["email"]}</span><a class="lien email" href="mailto:{EMAIL}">{EMAIL}</a> <button class="copier mono" type="button" data-copier="{EMAIL}" data-copie="{t["copie"]}">{t["copier"]}</button></li>{tel}
{whatsapp}
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
            <select name="demande">
{options(DEMANDES[langue])}
            </select>
          </label>
          <label class="champ"><span class="mono">{t["profil"]}</span>
            <select name="profil">
{options(PROFILS[langue])}
            </select>
          </label>
        </div>
        <div class="deux-colonnes">
          <label class="champ"><span class="mono">{t["bien"]}</span><input name="bien"></label>
          <label class="champ"><span class="mono">{t["ville"]}</span><input name="ville" autocomplete="address-level2"></label>
        </div>
        <div class="deux-colonnes">
          <label class="champ"><span class="mono">{t["surface"]}</span><input name="surface" inputmode="numeric"></label>
          <label class="champ"><span class="mono">{t["echeance"]}</span><input name="echeance"></label>
        </div>
        <label class="champ"><span class="mono">{t["message"]}</span><textarea name="message" rows="5" required></textarea></label>
        <div class="consignes">
          <p class="mono">{t["photos_titre"]}</p>
          <p>{t["photos_texte"]}</p>
        </div>
        <label class="case"><input type="checkbox" name="consentement" value="oui" required><span>{t["consentement"]} <a class="lien" href="{chemin(langue, "confidentialite")}">{t["confidentialite"]}</a></span></label>
        <div class="envoi"><button class="lien-fort accent" type="submit">{t["envoyer"]} <span aria-hidden="true">→</span></button><p class="etat mono" role="status" aria-live="polite"></p></div>
      </form>
    </section>'''


def corps_legal(nom):
    def corps(t, langue):
        blocs = []
        for bloc in LEGAL[langue][nom].split("\n\n"):
            if bloc.startswith("## "):
                titre, _, reste = bloc[3:].partition("\n")
                blocs.append(f'        <h2 class="titre-m">{escape(titre)}</h2>')
                if reste:
                    blocs.append(f"        <p>{escape(reste)}</p>")
            else:
                blocs.append(f"        <p>{escape(bloc)}</p>")
        contenu = "\n".join(blocs)
        return f'''    <section class="entete-page grille">
      <div class="col-large">
        <h1 class="titre-xl">{t["titres"][nom].split(" · ")[0]}</h1>
      </div>
    </section>
    <section class="section grille">
      <div class="col-large texte-legal">
{contenu}
      </div>
    </section>'''
    return corps



# Gabarit « étude de projet » : une page par projet réel, quand ses détails sont connus.
# Pas encore publié : ETUDES est vide tant que Sonja n'a pas fourni les informations.
# python3 generer.py --exemple DOSSIER écrit un exemple marqué « Exemple — ne pas publier » dans DOSSIER.
ETUDES = []
EXEMPLE_ETUDE = {
    "realisation": REALISATIONS[0],
    "fiche": {"fr": [("Lieu", "[Exemple] Cannes"), ("Type", "Appartement"), ("Surface", "— m²"), ("Prestation", "Conseil couleurs & matières"), ("Année", "—")],
              "en": [("Location", "[Example] Cannes"), ("Type", "Flat"), ("Size", "— m²"), ("Service", "Colour & materials"), ("Year", "—")]},
    "contexte": {"fr": "[Exemple] Un salon orienté ouest, lumineux l'après-midi, sombre le matin.", "en": "[Example] A west-facing living room, bright in the afternoon, dark in the morning."},
    "demande": {"fr": "[Exemple] Donner de la profondeur au mur principal sans assombrir la pièce.", "en": "[Example] Give depth to the main wall without darkening the room."},
    "intervention": {"fr": "[Exemple] Trois échantillons testés sur place à 9 h, 14 h et 19 h, puis enduit à la chaux en deux passes.", "en": "[Example] Three samples tested on site at 9 am, 2 pm and 7 pm, then lime plaster in two coats."},
    "materiaux": {"fr": ["[Exemple] Enduit à la chaux, teinte ocre clair", "[Exemple] Finition cirée mate"], "en": ["[Example] Lime plaster, pale ochre", "[Example] Matt waxed finish"]},
}


def corps_etude(etude, exemple=False):
    def corps(t, langue):
        r = etude["realisation"]
        fiche = "\n".join(f'          <div><dt class="mono">{k}</dt><dd>{escape(v)}</dd></div>' for k, v in etude["fiche"][langue])
        materiaux = "\n".join(f"            <li>{escape(x)}</li>" for x in etude["materiaux"][langue])
        bandeau = f'<p class="bandeau-exemple mono">{t["exemple"]}</p>' if exemple else ""
        return f'''    <section class="entete-page grille">
      <div class="col-entete">{entete_section(1, t["projets"])}</div>
      <div class="col-large">
        {bandeau}
        {titre_masque("h1", escape(r["titre"][langue]), "titre-xl")}
        <dl class="fiche">
{fiche}
        </dl>
      </div>
    </section>
    <section class="section grille">
      <figure class="col-large" data-reveal>{picture(fichier_image(r["image"]), r["alt"][langue], "(max-width: 760px) 100vw, 70vw")}</figure>
    </section>
    <section class="section grille etude">
      <div class="col-entete">{entete_section(2, t["etude_contexte"])}</div>
      <div class="col-principale"><p class="texte-large">{escape(etude["contexte"][langue])}</p></div>
      <div class="col-entete">{entete_section(3, t["etude_demande"])}</div>
      <div class="col-principale"><p class="texte-large">{escape(etude["demande"][langue])}</p></div>
      <div class="col-entete">{entete_section(4, t["etude_intervention"])}</div>
      <div class="col-principale"><p class="texte-large">{escape(etude["intervention"][langue])}</p></div>
      <div class="col-entete">{entete_section(5, t["etude_materiaux"])}</div>
      <div class="col-principale"><ul class="liste-mono mono">
{materiaux}
          </ul></div>
    </section>

{appel_devis(t, langue, 6)}'''
    return corps


def json_ld(langue, nom):
    """Données structurées : l'activité et la personne sur l'accueil, les questions sur Prestations."""
    import json
    if nom == "prestations":
        donnees = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q["q"][langue], "acceptedAnswer": {"@type": "Answer", "text": q["r"][langue]}} for q in FAQ],
        }
        return '  <script type="application/ld+json">' + json.dumps(donnees, ensure_ascii=False) + "</script>\n"
    if nom != "index":
        return ""
    contact = {"email": EMAIL}
    if TELEPHONE:
        contact["telephone"] = TELEPHONE.replace(" ", "")
    donnees = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ProfessionalService",
                "@id": f"{SITE}/#studio",
                "name": "Petric Sonja",
                "description": TEXTES[langue]["descriptions"]["index"],
                "url": SITE + chemin(langue, "index"),
                **contact,
                "image": f"{SITE}/images/{PHOTO_ACCUEIL}",
                "address": {"@type": "PostalAddress", "addressLocality": "Cannes", "addressRegion": "Provence-Alpes-Côte d'Azur", "addressCountry": "FR"},
                "areaServed": [{"@type": "AdministrativeArea", "name": "Côte d'Azur"}, {"@type": "Country", "name": "Monaco"}],
                "availableLanguage": ["fr", "en"],
                "priceRange": "Sur devis" if langue == "fr" else "On quotation",
                "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": p["titre"][langue], "description": p["resume"][langue]}} for p in PRESTATIONS],
                "sameAs": [INSTAGRAM],
                "founder": {"@id": f"{SITE}/#personne"},
            },
            {
                "@type": "Person",
                "@id": f"{SITE}/#personne",
                "name": "Petric Sonja",
                "givenName": "Sonja",
                "familyName": "Petric",
                "jobTitle": "Directrice artistique d'intérieur" if langue == "fr" else "Interior art director",
                "knowsAbout": ["couleur", "matières", "agencement", "home staging", "accrochage d'œuvres", "conservation-restauration"],
                "alumniOf": {"@type": "CollegeOrUniversity", "name": "École supérieure d'art d'Avignon"},
                "hasCredential": {"@type": "EducationalOccupationalCredential", "name": "DNSEP mention Conservation-restauration des biens culturels", "educationalLevel": "Master"},
                "sameAs": [INSTAGRAM],
            },
        ],
    }
    return '  <script type="application/ld+json">' + json.dumps(donnees, ensure_ascii=False) + "</script>\n"


CORPS = {
    "index": corps_index,
    "projets": corps_projets,
    "prestations": corps_prestations,
    "professionnels": corps_professionnels,
    "conservation-restauration": corps_conservation,
    "a-propos": corps_a_propos,
    "contact": corps_contact,
    "confidentialite": corps_legal("confidentialite"),
    "mentions-legales": corps_legal("mentions-legales"),
}


def page(langue, nom, corps=None, titre=None, robots=""):
    t = TEXTES[langue]
    titre = titre or t["titres"][nom]
    index_page = NAV.index(nom) + 1 if nom in NAV else None
    description = t["descriptions"][nom]
    url = SITE + chemin(langue, nom)
    nav = "\n".join(
        f'          <li><a class="lien-nav" href="{chemin(langue, p)}"{" aria-current=\"page\"" if p == nom else ""}><span class="num">{num(i, 2)}</span>{t["nav"][p]}</a></li>'
        for i, p in enumerate(NAV, 1)
    )
    langues = "".join(
        f'<a class="lien-nav" href="{chemin(l, nom)}" lang="{l}" hreflang="{l}"{" aria-current=\"true\"" if l == langue else ""}>{l.upper()}</a>' for l in LANGUES
    )
    alternates = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{SITE}{chemin(l, nom)}">' for l in LANGUES)
    alternates += f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{chemin(LANGUES[0], nom)}">'
    ld = "" if corps else json_ld(langue, nom)
    extra = visionneuse(t) if nom in ("projets", "index") and not corps else ""
    pied_pages = ["professionnels", "conservation-restauration"] + PAGES_LEGALES
    indicateur = f'<span class="num">{num(index_page, 2)}</span> / {num(len(NAV), 2)} — {t["nav"][nom]}' if index_page else titre.split(" · ")[0]
    return f'''<!doctype html>
<html lang="{langue}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titre}</title>
  <meta name="description" content="{description}">
{robots}  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#EFEAE2" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#1A1714" media="(prefers-color-scheme: dark)">
  <meta name="color-scheme" content="light dark">
  <meta property="og:title" content="{titre}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{t["og_locale"]}">
  <meta property="og:image" content="{SITE}/images/{PHOTO_ACCUEIL}">
  <meta name="twitter:card" content="summary_large_image">
{alternates}
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/fonts/inter-tight.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/css/style.css">
{ld}  <script>document.documentElement.classList.add("js");try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
  <a class="evitement mono" href="#contenu">{t["aller_contenu"]}</a>
  <header class="entete">
    <a class="logo" href="{chemin(langue, "index")}"{" aria-current=\"page\"" if nom == "index" else ""}><img class="logo-sp" src="/images/logo-sp.svg" alt="" width="18" height="38"><span class="logo-texte">Petric Sonja</span></a>
    <p class="indicateur mono" aria-hidden="true">{indicateur}</p>
    <nav class="nav mono" id="menu" aria-label="Menu">
      <ul>
{nav}
      </ul>
      <div class="langues">{langues}<button class="theme-bouton mono" type="button" aria-pressed="false" data-sombre="{t["theme_sombre"]}" data-clair="{t["theme_clair"]}">{t["theme_sombre"]}</button></div>
    </nav>
    <a class="cta-entete mono" href="{chemin(langue, "contact")}"{" aria-current=\"page\"" if nom == "contact" else ""}>{t["votre_projet"]} <span aria-hidden="true">→</span></a>
    <button class="menu-bouton mono" type="button" aria-expanded="false" aria-controls="menu" data-ouvrir="{t["menu"]}" data-fermer="{t["fermer_menu"]}">{t["menu"]}</button>
  </header>

  <main id="contenu">
{(corps or CORPS[nom])(t, langue)}
  </main>
{extra}
  <footer class="pied mono grille">
    <span>© <span id="annee"></span> Petric Sonja</span>
    <span>{t["lieu"]}</span>
    <a class="lien" href="mailto:{EMAIL}">{EMAIL}</a>
    {f'<a class="lien" href="tel:{TELEPHONE.replace(" ", "")}">{TELEPHONE}</a>' if TELEPHONE else ""}
    {f'<a class="lien" href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp</a>' if WHATSAPP else ""}
    <a class="lien" href="{INSTAGRAM}" rel="noopener">Instagram</a>
    {"".join(f'<a class="lien" href="{chemin(langue, p)}">{t["mentions_legales"] if p == "mentions-legales" else t["confidentialite"] if p == "confidentialite" else t["nav"][p]}</a>' for p in pied_pages)}
  </footer>
  <script src="/js/main.js" defer></script>
</body>
</html>
'''


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--exemple":
        dossier = Path(sys.argv[2])
        dossier.mkdir(parents=True, exist_ok=True)
        for langue in LANGUES:
            html = page(langue, "projets", corps=corps_etude(EXEMPLE_ETUDE, exemple=True), titre=f"{TEXTES[langue]['exemple']} · Petric Sonja",
                        robots='  <meta name="robots" content="noindex">\n')
            (dossier / f"etude-exemple-{langue}.html").write_text(html, encoding="utf-8")
        print(f"exemple écrit dans {dossier}")
        sys.exit()
    for langue in LANGUES:
        dossier = RACINE if langue == LANGUES[0] else RACINE / langue
        dossier.mkdir(exist_ok=True)
        for nom in PAGES + PAGES_LEGALES:
            (dossier / f"{slug(langue, nom)}.html").write_text(page(langue, nom), encoding="utf-8")
            print(f"{dossier.relative_to(RACINE) / (slug(langue, nom) + '.html')}")
    urls = []
    for nom in PAGES + PAGES_LEGALES:
        liens = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{chemin(l, nom)}"/>' for l in LANGUES)
        urls += [f"  <url>\n    <loc>{SITE}{chemin(l, nom)}</loc>{liens}\n  </url>" for l in LANGUES]
    (RACINE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (RACINE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("sitemap.xml, robots.txt")
