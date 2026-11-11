#!/usr/bin/env python3
"""Squelette de génération Higgsfield (à compléter avec la doc API : cloud.higgsfield.ai).
Lit la clé dans .env. Vérifie le prix avant de lancer (ne pas gaspiller de crédits)."""
import os, sys, pathlib

def load_env():
    p = pathlib.Path(__file__).resolve().parent.parent / ".env"
    if p.exists():
        for l in p.read_text().splitlines():
            if "=" in l and not l.startswith("#"):
                k, v = l.split("=", 1); os.environ.setdefault(k.strip(), v.strip())

def main():
    load_env()
    if not os.environ.get("HIGGSFIELD_API_KEY"):
        sys.exit("Clé manquante : copie .env.example en .env et remplis-la.")
    print("TODO : appeler l'API (image Nano Banana 2 puis vidéo Seedance 2.5) pour plans/<n>.md")

if __name__ == "__main__":
    main()
