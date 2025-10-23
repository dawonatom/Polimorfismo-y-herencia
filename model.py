# model.py

# --- Clase Base (Superclase) ---
class Animal:
    def __init__(self, especie, edad, **kwargs):
        """
        Añadimos **kwargs para capturar todos los atributos extra.
        """
        self.especie = especie
        self.edad = edad
        # Guardamos cualquier otro atributo (ej. color, habitat)
        self.extra_attributes = kwargs  

    def hablar(self) -> str:
        return ""

    def moverse(self) -> str:
        return ""

    def describeme(self) -> str:
        return f"Soy un Animal del tipo {type(self).__name__}"

    def to_dict(self):
        """Convierte los atributos base a un diccionario."""
        data = {
            'tipo': type(self).__name__,
            'especie': self.especie,
            'edad': self.edad
        }
        # Añade todos los atributos extra guardados al diccionario
        data.update(self.extra_attributes)
        return data

# --- Clases Hijas (Subclases) ---
class Perro(Animal):
    def __init__(self, especie, edad, dueño, **kwargs):
        """
        Recibe **kwargs y los pasa al constructor 'super()'.
        """
        super().__init__(especie, edad, **kwargs) # Pasa los extras al padre
        self.dueño = dueño # Atributo específico de Perro

    def hablar(self) -> str:
        return "Guau!"

    def moverse(self) -> str:
        return "Caminando con 4 patas"
    
    def to_dict(self):
        """Convierte Perro a dict."""
        # Llama al to_dict() del padre (que ya incluye los extra_attributes)
        data = super().to_dict()
        # Añade su propio atributo 'dueño'
        data.update({'dueño': self.dueño})
        return data

class Vaca(Animal):
    def __init__(self, especie, edad, **kwargs):
        """Pasa los kwargs al padre."""
        super().__init__(especie, edad, **kwargs)

    def hablar(self) -> str:
        return "Muuu!"

    def moverse(self) -> str:
        return "Caminando con 4 patas"
    
    # No necesita to_dict() propio, usará el de Animal.

class Abeja(Animal):
    def __init__(self, especie, edad, **kwargs):
        """Pasa los kwargs al padre."""
        super().__init__(especie, edad, **kwargs)

    def hablar(self) -> str:
        return "Bzzzz!"

    def moverse(self) -> str:
        return "Volando"

    def picar(self) -> str:
        return "Picar!"
    
    def to_dict(self):
        data = super().to_dict() # Llama al padre (que tiene extras)
        data.update({'accion_especial': 'Picar'})
        return data