# Rúbrica del TP integrador — C2 2026

Comisión grande: cada entrega se corrige con **checklist**. Escala por ítem:

| Letra | Significado | Fracción de ese ítem |
| --- | --- | --- |
| C | Cumple | 1.00 |
| P | Parcial (está, pero frágil / incompleto / mal encapsulado) | 0.50 |
| N | No cumple o no corre | 0.00 |
| NA | No aplica todavía | se ignora |

**Puntaje de la entrega** = (suma de C/P/N ponderados) × peso de la entrega × (1 − 0.25 si llegó el lunes o el martes).

Si el CLI **no arranca** con el dataset de la cátedra: esa entrega vale **0** (salvo E1, donde alcanza un error claro y un README que explique cómo debería correr).

Regresión: si algo que ya había sido C en una entrega previa deja de andar, ese ítem de la entrega actual se marca N aunque el tema nuevo esté bien.

---

## Entrega 1 — 5 % — repo y catálogo vivo

| # | Ítem | Peso interno |
| --- | --- | --- |
| 1.1 | Mail del grupo enviado a Ambrossio **y** Bianco; repo GitHub accesible, tag `entrega-1`, README con integrantes, mails, tema y cómo ejecutar | 20 % |
| 1.2 | Dataset de la cátedra se carga (CSV) sin hardcodear las filas en el `.py` | 20 % |
| 1.3 | CLI lista el catálogo (aunque sea con `list` de Python) | 20 % |
| 1.4 | Funciones con responsabilidad clara (no un único bloque lineal en `main`) | 15 % |
| 1.5 | Informe arrancado: por qué eligieron el tema; qué objetos son mutables e inmutables en su modelo | 15 % |
| 1.6 | `docs/DECLARACION_IA.md` presente (aunque diga “no usamos”) | 10 % |

---

## Entrega 2 — 7 % — módulos, recursión, objetos

| # | Ítem | Peso interno |
| --- | --- | --- |
| 2.1 | Código partido en módulos; clases del dominio aunque todavía usen `list`; `main` no concentra la lógica | 20 % |
| 2.2 | Recursión del dominio correcta, con caso base, sobre el dataset (no un factorial de juguete) | 35 % |
| 2.3 | Traza de un ejemplo en el informe | 15 % |
| 2.4 | Protocolo de pruebas con al menos 8 casos escritos (entrada, esperado, aún no hace falta ejecutarlos todos) | 20 % |
| 2.5 | Declaración de IA actualizada + el tag corre | 10 % |

---

## Entrega 3 — 12 % — TADs, lineales, excepciones

| # | Ítem | Peso interno |
| --- | --- | --- |
| 3.1 | `ListaEnlazada` propia con nodos (insertar, eliminar, buscar, tamaño). Un `list` interno cuenta como N | 20 % |
| 3.2 | Iterador funcionando; el listado del catálogo o de la colección lo usa | 10 % |
| 3.3 | `Pila` y `Cola` implementadas **sobre** la lista enlazada, usadas en el dominio (historial y cola) | 20 % |
| 3.4 | Colección principal (equipo / menú / playlist) sobre `ListaEnlazada`, con tope si aplica (equipo de 6) | 15 % |
| 3.5 | Encapsulamiento: atributos no se manosean desde el CLI; métodos con nombres claros | 10 % |
| 3.6 | Excepciones propias capturadas en el menú (sin `except:`) | 10 % |
| 3.7 | Protocolo de pruebas **ejecutado** (columna pasa / no pasa / comentarios) | 10 % |
| 3.8 | Tag corre; declaración de IA al día | 5 % |

---

## Entrega 4 — 9 % — búsqueda, orden, complejidad

| # | Ítem | Peso interno |
| --- | --- | --- |
| 4.1 | Búsqueda lineal propia, usada desde el CLI | 15 % |
| 4.2 | Búsqueda binaria propia sobre colección ordenada; el CLI no la ofrece si no está ordenada (o reordena y avisa) | 20 % |
| 4.3 | Dos algoritmos de ordenamiento **propios** (no `sorted`). Criterios distintos o un criterio + estable vs. no) | 25 % |
| 4.4 | Tabla de complejidad de las operaciones del sistema | 20 % |
| 4.5 | Medición con `time.perf_counter` (dataset original y una versión agrandada, o al menos dos tamaños) | 15 % |
| 4.6 | Tag corre; no rompieron E2/E3 | 5 % |

Usar `sorted` / `list.sort` para cumplir 4.2–4.3 = N en esos ítems.

---

## Entrega 5 — 9 % — archivos texto y binario

| # | Ítem | Peso interno |
| --- | --- | --- |
| 5.1 | Guardar y cargar el catálogo en CSV (secuencial). Tras cerrar y abrir el programa, los datos siguen | 25 % |
| 5.2 | Archivo binario con `struct`, registros de longitud fija, header documentado | 25 % |
| 5.3 | Actualizar **un** registro por posición (seek / índice), sin reescribir todo el archivo a mano en un único `write` | 20 % |
| 5.4 | Alta / baja / modificación persistente desde el CLI | 15 % |
| 5.5 | Excepción de archivo inválido (binario corto, magia incorrecta, CSV roto) | 10 % |
| 5.6 | Tag corre; informe con el layout del registro | 5 % |

---

## Entrega 6 — 8 % — cierre del producto

| # | Ítem | Peso interno |
| --- | --- | --- |
| 6.1 | Las 10 operaciones del menú (consigna §3.1) funcionan sobre el dataset de la cátedra | 40 % |
| 6.2 | Informe completo (modelo, TADs, recursión, complejidad, persistencia, reparto de trabajo) | 20 % |
| 6.3 | Protocolo de pruebas de regresión ejecutado (mínimo 15 casos, cubriendo pila, cola, archivos, recursión, búsquedas) | 20 % |
| 6.4 | README de producto (cómo ejecutar, limitaciones, tema) | 10 % |
| 6.5 | Declaración de IA final coherente con el repo | 10 % |

---

## Defensa oral — 25 % — reemplaza el 2do parcial

15 minutos. 25 y 27 de noviembre de 2026. Los puntos se reparten entre integrantes; si uno no habla o no puede defender, **esa persona** tiene 0 en el oral (el resto conserva su oral).

| # | Qué se mira | Peso |
| --- | --- | --- |
| O1 | Explicar un TAD con invariante (pila, cola o lista) y mostrarlo en el código | 25 % |
| O2 | Traza de la recursión sobre un ítem real del dataset | 20 % |
| O3 | Persistencia: layout del binario y un `seek` / actualización por posición | 20 % |
| O4 | Complejidad de una operación del sistema (por qué esa cota, qué midieron) | 15 % |
| O5 | Responder un “¿y si…?” (equipo lleno, cola vacía, archivo truncado, catálogo no ordenado) | 20 % |

C / P / N también acá. Lectura de código en voz alta sin saber qué hace = N. Aprueba con 15 / 25.

---

## Notas de corrección (para la cátedra)

- Tiempo objetivo: E1/E2 ~10 min/grupo; E3 ~20 min; E4/E5 ~15 min; E6 repo ~15 min.
- Oral: 15 min + 3 min de cambio. ~8 grupos por clase. Miércoles 25-nov + viernes 27-nov cubren ~16 grupos; si hay más, arrancar el viernes 20-nov (semana 14) o usar un rato del 02-dic.
- Clonar el tag, correr, picar el checklist, un comentario de 3 líneas en el campus. No reescribir el TP.
- Tres docentes: partir grupos por inicial del apellido o por tema (Pokédex / recetario / música) y rotar en E4 para no fosilizar criterios.
- No hay 2do parcial ni recuperatorio de 2do parcial. Oral de recuperatorio en semana 16 solo con falta justificada.
