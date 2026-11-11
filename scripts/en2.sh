#!/usr/bin/env bash
# Convertit une vidéo en 12 fps (animation "en 2") pour juger le rendu anime.
# Usage : scripts/en2.sh entree.mp4 [sortie.mp4]
set -e
in="$1"; out="${2:-${in%.*}_en2.mp4}"
ffmpeg -y -i "$in" -vf "fps=12,fps=24" -c:v libx264 -crf 18 -preset veryfast -c:a copy "$out"
echo "ok -> $out"
