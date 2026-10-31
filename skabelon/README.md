# Skabelon til Gusbogen-opslag

Grafikken laves som HTML og gemmes som PNG med Chrome/Playwright.

- `eksempel-instagram.html` – 1080×1350 (Instagram, 4:5)
- `eksempel-tiktok.html` – 1080×1920 (TikTok, 9:16)
- `icon.png` – app-ikonet, vist nederst med navnet "Gusbogen"
- `render.py` – laver `olieskolen-feed.png` og `olieskolen-tiktok.png` fra `feed.html` og `tiktok.html`

Kør i denne mappe:

```
npm i @fontsource/fraunces @fontsource/inter
python3 render.py
```

## Faste regler for ALLE opslag

- App-logoet (`icon.png`) og navnet "Gusbogen" skal altid være med, nederst ved "Link i bio".
- Kaspers navn må aldrig stå på opslagene, hverken i grafik eller tekst.
- Ingen kategori-label øverst.
- Teksten starter med "Reklame |" og har #reklame.

Stil: skovgrøn #1F3A2E, creme #F4EDE1, saunatræ #C98A4B, glød #E8A15C. Skrift: Fraunces (overskrifter) og Inter (brødtekst). Ingen emojis i grafikken. Ingen kategori-label øverst. Logo og navn nederst sammen med "Link i bio".

Færdige billeder lægges i `opslag/<år>-uge-<nr>/` og bruges i Metricool via
`https://raw.githubusercontent.com/greenpure61/gusbogen_markedsforings_billeder/main/<sti>`.
