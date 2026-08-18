class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        raise NotImplementedError

    def esta_vacia(self):
        raise NotImplementedError

    def tamanio(self):
        raise NotImplementedError

    def insertar_al_inicio(self, dato):
        raise NotImplementedError

    def insertar_al_final(self, dato):
        raise NotImplementedError

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        raise NotImplementedError

    def buscar(self, dato):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
