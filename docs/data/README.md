# Datasets

Elegí **un** tema. Los CSV de los otros dos se pueden dejar en la carpeta; no hace falta borrarlos.

Codificación: UTF-8. Separador: coma. La primera fila es encabezado.

| Tema | Archivos | Relación recursiva |
| --- | --- | --- |
| Pokédex | `pokedex.csv`, `evoluciones.csv` | `origen_id` → `destino_id` (una fila por evolución; Eevee tiene varias) |
| Recetario | `recetas.csv`, `ingredientes.csv`, `subrecetas.csv` | `receta_id` usa `subreceta_id` |
| Biblioteca musical | `canciones.csv`, `versiones.csv` | `cancion_id` es versión de `version_de_id` (`cover`, `live`, `remix`) |

No hardcodees las filas en el código: leé los CSV.
