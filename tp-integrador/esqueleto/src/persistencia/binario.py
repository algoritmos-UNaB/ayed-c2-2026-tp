"""Registros de longitud fija con struct.

Layout sugerido (documentar el definitivo en docs/INFORME.md):

Header:
  magia     4s   b'AYED'
  tema      1s   b'P' | b'R' | b'M'
  cantidad  I    unsigned int

El registro depende del tema. Ejemplo Pokédex:
  id          I
  nombre     20s
  tipo1      12s
  tipo2      12s
  hp          H
  ataque      H
  defensa     H
  velocidad   H
  generacion  H
"""


def guardar_binario(ruta, items):
    raise NotImplementedError


def cargar_binario(ruta):
    raise NotImplementedError


def actualizar_registro(ruta, posicion, item):
    """Pisa un registro por posición (acceso directo). posicion es 0-based."""
    raise NotImplementedError
