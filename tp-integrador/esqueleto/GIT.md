# Git mínimo para este TP

## Una sola vez

1. Crear un repo vacío en GitHub (nombre sugerido: `ayed-2026-pokedex`, `ayed-2026-recetario` o `ayed-2026-musica`). No uses el repo de la consigna de la cátedra.
2. Copiar esta carpeta `esqueleto` (no el de los otros grupos).
3. Subir:

```text
git init
git add .
git commit -m "E1: esqueleto y datos del tema"
git branch -M main
git remote add origin https://github.com/USUARIO/ayed-2026-TEMA.git
git push -u origin main
```

Invitar a los integrantes. El grupo se avisa **sí o sí** por mail a:

- diego.ambrossio@unab.edu.ar
- angel.bianco@unab.edu.ar

Asunto: `[AyED C2 2026] Grupo Apellido1-Apellido2`. Incluir nombres, mails, usuarios de GitHub, tema y URL del repo.

## Preentrega (opcional, domingo 30-ago)

Solo para probar que el repo se puede clonar. No suma nota.

```text
git tag preentrega
git push origin preentrega
```

Después mandan el mail con la URL. El código del catálogo no hace falta todavía.

## Cada entrega

```text
git add .
git status
git commit -m "E3: lista enlazada, pila y cola"
git tag entrega-3
git push
git push origin entrega-3
```

El mensaje de commit puede ser el que quieran; el **tag** tiene que ser exactamente `entrega-1` … `entrega-6`.

Si se equivocan antes del vencimiento:

```text
git tag -d entrega-3
git push origin :refs/tags/entrega-3
git tag entrega-3
git push origin entrega-3
```

Después del domingo 23:59 no retaguear en silencio: ese tag ya se está corrigiendo.

## Qué no subir

`__pycache__/`, `.venv/`, archivos `.bin` de prueba locales (el programa los tiene que **poder generar**). El `.gitignore` del esqueleto ya cubre lo habitual.
