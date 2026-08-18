# TP integrador — Algoritmos y Estructuras de Datos (C2 2026)

Este directorio es el pack docente y el punto de partida para el alumnado.

## Para publicar en el campus

1. `consigna.md` — enunciado, reglas, tres temas, entregas.
2. `rubrica.md` — checklists de corrección (comisión grande).
3. `esqueleto/` — repositorio base para clonar/fork.
4. El `cronograma.md` de la raíz del workspace (ya actualizado).

## Contenido del esqueleto

- `esqueleto/README.md` — cómo correr el CLI y cómo entregar.
- `esqueleto/GIT.md` — clone, commits, tag `entrega-N`.
- `esqueleto/docs/` — plantillas de informe, protocolo de pruebas y declaración de IA.
- `esqueleto/data/` — datasets de los tres temas.
- `esqueleto/src/` — módulos vacíos con firmas a completar.

## Clase 1 (19-ago)

Mañana arranca el cuatrimestre. En esa clase conviene, además del intro a Python:

1. Publicar consigna + esqueleto en el campus / GitHub de la cátedra.
2. Armar grupos de 2–3 y elegir tema (no se cambia después de E1).
3. Que cada grupo cree el repo, copie el esqueleto y haga el primer commit (hay `esqueleto/GIT.md`).
4. Avisar: entrega 1 vence **domingo 06-sep 23:59**.

## Decisiones de diseño (para el equipo docente)

- Un solo TP, tres pieles: Pokédex, recetario, biblioteca musical.
- Grupos de 2 o 3. CLI. Solo biblioteca estándar de Python.
- Seis entregas incrementales, domingo 23:59, tag en GitHub. E1 el 06-sep.
- Lista enlazada propia; pila y cola sobre esa lista.
- Persistencia: archivo de texto (CSV) + archivo binario (`struct`).
- IA permitida si se declara y se puede defender en el oral.
- Verificación: protocolo de pruebas manual (no se exige `pytest`).
- El TP reemplaza prácticas y 2do parcial. Defensas: 25 y 27-nov.
