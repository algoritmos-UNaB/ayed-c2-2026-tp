"""Genera docs/*.html para GitHub Pages a partir de los markdown del TP."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = "assets/style.css"

NAV = [
    ("index.html", "Inicio"),
    ("consigna.html", "Consigna"),
    ("cronograma.html", "Cronograma"),
    ("rubrica.html", "Rúbrica"),
    ("entregar.html", "Cómo entregar"),
    ("datasets.html", "Datasets"),
]


def md_to_html(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )


def layout(title: str, body: str, current: str, extra_class: str = "doc") -> str:
    links = []
    for href, label in NAV:
        current_attr = ' aria-current="page"' if href == current else ""
        links.append(f'<a href="{href}"{current_attr}>{label}</a>')
    nav = "\n        ".join(links)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — AyED C2 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{ASSETS}">
</head>
<body>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="index.html">
        <small>00184 · UNaB · C2 2026</small>
        <strong>TP integrador</strong>
      </a>
      <nav>
        {nav}
      </nav>
    </div>
  </header>
  <main class="{extra_class}">
    {body}
  </main>
  <footer class="site-footer">
    <div class="wrap">Algoritmos y Estructuras de Datos · C2 2026. El código se corrige por tag de GitHub; esta página es la consigna para leer.</div>
  </footer>
</body>
</html>
"""


INDEX_BODY = """
<div class="wrap">
  <section class="hero">
    <div>
      <p class="kicker">Un solo trabajo, todo el cuatrimestre</p>
      <h1>Tres temas.<br>Las mismas estructuras.</h1>
      <p class="lede">Reemplazamos las prácticas sueltas por un TP que crece entrega a entrega: Pokédex, recetario o biblioteca musical. Consola, Python, grupos de 2 o 3.</p>
      <div class="meta-pills">
        <span class="pill">6 entregas · domingo 23:59</span>
        <span class="pill">CLI · stdlib</span>
        <span class="pill">GitHub obligatorio</span>
        <span class="pill">IA permitida si se declara</span>
      </div>
      <div class="actions">
        <a class="btn btn-primary" href="consigna.html">Leer la consigna</a>
        <a class="btn btn-ghost" href="entregar.html">Clonar el esqueleto</a>
      </div>
    </div>
    <aside class="deadline">
      <span>Próximo cierre</span>
      <strong>Entrega 1</strong>
      <p>Domingo 30 de agosto de 2026, 23:59 (Argentina). Repo, tema, CSV y listar el catálogo.</p>
      <a href="rubrica.html">Ver checklist de E1</a>
    </aside>
  </section>

  <section class="themes">
    <article class="theme poke">
      <span class="kicker">Tema A</span>
      <h2>Pokédex</h2>
      <p>Catálogo, equipo de 6, cadenas de evolución (recursión), historial en pila y cola de turnos.</p>
    </article>
    <article class="theme cook">
      <span class="kicker">Tema B</span>
      <h2>Recetario</h2>
      <p>Recetas con sub-recetas, menú de la semana, historial de lo cocinado y cola de preparación.</p>
    </article>
    <article class="theme music">
      <span class="kicker">Tema C</span>
      <h2>Biblioteca musical</h2>
      <p>Canciones, playlists, covers y vivos (recursión), historial de reproducción y cola “up next”.</p>
    </article>
  </section>

  <section class="grid-2">
    <div class="panel">
      <h2>Seis entregas</h2>
      <ol class="entregas">
        <li><span class="tag">E1</span><span>Repo, dataset y listar</span><span>30 ago</span></li>
        <li><span class="tag">E2</span><span>Módulos y recursión</span><span>13 sep</span></li>
        <li><span class="tag">E3</span><span>Lista, pila, cola, excepciones</span><span>4 oct</span></li>
        <li><span class="tag">E4</span><span>Búsqueda, orden, complejidad</span><span>1 nov</span></li>
        <li><span class="tag">E5</span><span>CSV + binario</span><span>15 nov</span></li>
        <li><span class="tag">E6</span><span>Cierre y defensa oral</span><span>22 nov</span></li>
      </ol>
    </div>
    <div class="panel">
      <h2>Cómo se nota</h2>
      <div class="bars" aria-hidden="true"><span></span><span></span><span></span></div>
      <p class="legend">Parcial 1 · 25% &nbsp; Parcial 2 · 25% &nbsp; TP integrador · 40%</p>
      <p>El TP se aprueba con 24/40 y con defensa oral de todo el grupo. Cada parcial, con 60%.</p>
      <p><a href="cronograma.html">Cronograma completo</a> · <a href="rubrica.html">Rúbrica</a></p>
    </div>
  </section>
</div>
"""


DATASETS_BODY = """
<h1>Datasets</h1>
<p>Elegí un tema. Los CSV van en UTF-8, con encabezado. No hardcodees las filas en el código: leé los archivos.</p>
<table>
  <thead><tr><th>Tema</th><th>Archivos</th><th>Recursión</th></tr></thead>
  <tbody>
    <tr>
      <td>Pokédex</td>
      <td><a href="data/pokedex.csv">pokedex.csv</a>, <a href="data/evoluciones.csv">evoluciones.csv</a></td>
      <td><code>origen_id</code> → <code>destino_id</code></td>
    </tr>
    <tr>
      <td>Recetario</td>
      <td><a href="data/recetas.csv">recetas.csv</a>, <a href="data/ingredientes.csv">ingredientes.csv</a>, <a href="data/subrecetas.csv">subrecetas.csv</a></td>
      <td>una receta usa sub-recetas</td>
    </tr>
    <tr>
      <td>Biblioteca musical</td>
      <td><a href="data/canciones.csv">canciones.csv</a>, <a href="data/versiones.csv">versiones.csv</a></td>
      <td>cover, live o remix de otra canción</td>
    </tr>
  </tbody>
</table>
<p>Están también dentro del esqueleto, en <code>tp-integrador/esqueleto/data/</code>.</p>
"""


def strip_teacher_notes(text: str) -> str:
    return re.split(r"\n## Notas de corrección", text, maxsplit=1)[0]


def write(name: str, title: str, body: str, extra_class: str = "doc") -> None:
    (DOCS / name).write_text(layout(title, body, name, extra_class), encoding="utf-8")


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    data_src = ROOT / "tp-integrador" / "esqueleto" / "data"
    data_dst = DOCS / "data"
    if data_dst.exists():
        shutil.rmtree(data_dst)
    shutil.copytree(data_src, data_dst)

    write("index.html", "TP integrador", INDEX_BODY, extra_class="")
    write("consigna.html", "Consigna", md_to_html((ROOT / "tp-integrador" / "consigna.md").read_text(encoding="utf-8")))
    write("cronograma.html", "Cronograma", md_to_html((ROOT / "cronograma.md").read_text(encoding="utf-8")))
    write(
        "rubrica.html",
        "Rúbrica",
        md_to_html(strip_teacher_notes((ROOT / "tp-integrador" / "rubrica.md").read_text(encoding="utf-8"))),
    )
    git_md = (ROOT / "tp-integrador" / "esqueleto" / "GIT.md").read_text(encoding="utf-8")
    readme_md = (ROOT / "tp-integrador" / "esqueleto" / "README.md").read_text(encoding="utf-8")
    intro = """# Cómo entregar

El esqueleto vive en este mismo repositorio: carpeta `tp-integrador/esqueleto`.

```text
git clone https://github.com/algoritmos-UNaB/ayed-c2-2026-tp.git
```

Sitio de la consigna: https://algoritmos-unab.github.io/ayed-c2-2026-tp/

Cloná el repo de la cátedra, copiá esa carpeta a un repo **nuevo** del grupo y trabajá ahí. No hagan fork eterno sobre el repo de la consigna: si no, se mezclan tags.

"""
    write("entregar.html", "Cómo entregar", md_to_html(intro + "\n\n" + readme_md + "\n\n" + git_md))
    write("datasets.html", "Datasets", DATASETS_BODY)
    print(f"OK -> {DOCS}")


if __name__ == "__main__":
    main()
