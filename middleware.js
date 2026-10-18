// Site privé tant qu'il n'est pas prêt : Vercel exécute ce fichier avant chaque page
// et demande un mot de passe (fenêtre de connexion du navigateur, nom d'utilisateur libre).
// Le mot de passe est la variable SITE_PASSWORD du projet Vercel ; sans elle, personne n'entre.
// Pour ouvrir le site au public : supprimer ce fichier.

export const config = { matcher: "/:path*" };

export default function middleware(request) {
  const motDePasse = process.env.SITE_PASSWORD;
  const entete = request.headers.get("authorization") || "";
  if (motDePasse && entete.startsWith("Basic ")) {
    const [, saisi] = atob(entete.slice(6)).split(/:(.*)/s);
    if (saisi === motDePasse) return;
  }
  return new Response("Site en préparation. / Site under construction.", {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="Sonja Petric", charset="UTF-8"',
      "Content-Type": "text/plain; charset=utf-8",
      "X-Robots-Tag": "noindex",
    },
  });
}
