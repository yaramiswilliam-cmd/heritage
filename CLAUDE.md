# Kodo Iwa — épisode d'animation 2D (Higgsfield)

Projet de William : épisode d'animation 2D, style doux "Ranking of Kings", boxe Muay Thai intense et dynamique.
Langue de travail : français, ton direct et informel. Claude agit comme réalisateur / storyboardeur (rigueur Wit Studio) et NE FAIT PAS GASPILLER DE CRÉDITS : il vérifie chaque image point par point AVANT de la valider.

## Direction artistique (validée)
Anime doux façon livre d'images, traits fins légèrement irréguliers brun foncé, couleurs pastel mates, aplats, décor gouache (sans contours, pas d'effet aquarelle), lumière chaude de fin d'après-midi venant de la gauche.

## Règles de continuité (à vérifier à chaque plan)
- Luca à GAUCHE, Kodo à DROITE quand les deux sont dans le cadre (règle des 180°).
- Gants : Luca ORANGE, Kodo ROUGES.
- UN seul ring par plan.
- Mèche étoile bleue de Kodo : centrée au-dessus du nez.
- Kodo sérieux et concentré ; Luca sourit en coin sans rire.
- Une seule action par plan.
- Coach : grand et massif, bonnet jaune moutarde, cigarette au coin de la bouche (même côté sur toutes les vues), henley crème, pantalon bleu marine ample, baskets rouges.

## Pipeline
1. Image clé : Nano Banana 2 (Higgsfield Image), références dans cet ordre : image 1 = gym, image 2 = fiche Kodo, image 3 = fiche Luca. 16:9.
2. Animation : Seedance 2.5 (image-vers-vidéo), 480p pour tester, 5 s, 16:9, son activé. UNE vidéo par plan (le multi-plan tue le mouvement). Ne garder que 1 à 2 s utiles.
3. Son : pas de musique, pas d'ambiance, pas de voix dans Seedance ; seulement bruits de corps/objets via une ligne "Sound:" et une ligne "Avoid:". Voix via ElevenLabs. Silence volontaire au plan 10.
4. Contrôle "anime" : `scripts/en2.sh` convertit en 12 fps ("en 2") pour juger le rendu.
5. Montage CapCut, upscale final (Video2X ou CapCut).

## Dépôt
- `scenario/` : histoire et découpage
- `refs/` : fiches personnages, décor, images clés validées
- `plans/` : un fichier par plan (prompt image, prompt vidéo, références, réglages, statut)
- `scripts/` : génération via API Higgsfield + conversion "en 2"
- Clé API dans `.env` (jamais commitée, jamais collée dans le chat).
