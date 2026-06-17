import requests

# Lista de fuentes públicas que quieras usar
FUENTES = [
    "https://iptv-org.github.io/iptv/index.m3u",
]

playlist = "#EXTM3U\n\n"

for url in FUENTES:
    try:
        r = requests.get(url, timeout=30)
        if r.ok:
            texto = r.text

            # Eliminar el encabezado repetido
            texto = texto.replace("#EXTM3U", "")

            playlist += texto.strip() + "\n\n"

    except Exception:
        pass

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist)
