# viewmodel.py

from model import Perro, Vaca, Abeja
from repository import AnimalRepository

class AnimalViewModel:
    def __init__(self, repository: AnimalRepository):
        self._repository = repository
        self.animal_list_display = []
        self.status_message = ""

    def load_animals_command(self):
        # ... (sin cambios)
        print("... Cargando animales desde Firebase ...")
        self.animal_list_display = self._repository.get_all_animals()
        if not self.animal_list_display:
            self.status_message = "No se encontraron animales en la enciclopedia."
        else:
            self.status_message = f"Se cargaron {len(self.animal_list_display)} animales."

    def register_animal_command(self, tipo, especie, edad, **kwargs):
        # ... (sin cambios)
        animal_obj = None
        dueño = kwargs.pop('dueño', 'Desconocido') if tipo.lower() == 'perro' else None
        
        try:
            if tipo.lower() == 'perro':
                animal_obj = Perro(especie, edad, dueño, **kwargs)
            elif tipo.lower() == 'vaca':
                animal_obj = Vaca(especie, edad, **kwargs)
            elif tipo.lower() == 'abeja':
                animal_obj = Abeja(especie, edad, **kwargs)
            else:
                self.status_message = "❌ Tipo de animal no válido."
                return

            if animal_obj:
                success = self._repository.register_animal(animal_obj)
                if success:
                    self.status_message = f"¡{tipo.capitalize()} registrado con éxito!"
                else:
                    self.status_message = f"❌ Error al registrar {tipo}."
        except Exception as e:
            self.status_message = f"❌ Error al crear el objeto: {e}"

    def get_animal_details_by_index(self, index: int):
        # ... (sin cambios)
        try:
            if index < 0:
                return None
            return self.animal_list_display[index]
        except IndexError:
            self.status_message = "❌ Índice no válido."
            return None
            
    # --- ¡NUEVO MÉTODO! ---
    def delete_animal_by_index(self, index: int):
        """
        Comando para eliminar un animal basado en su índice en la lista.
        """
        try:
            if index < 0:
                self.status_message = "❌ Índice no válido."
                return

            # 1. Obtenemos el animal de nuestra lista en memoria
            animal_to_delete = self.animal_list_display[index]
            
            # 2. Obtenemos su ID de Firebase (que guardamos en get_all_animals)
            doc_id = animal_to_delete.get('doc_id')
            if not doc_id:
                self.status_message = "❌ Error: No se encontró el ID del documento."
                return

            # 3. Le pedimos al repositorio que lo borre por su ID
            success = self._repository.delete_animal_by_id(doc_id)
            
            if success:
                self.status_message = f"✔️ Animal '{animal_to_delete.get('tipo')}' eliminado."
                # 4. (Importante!) También lo quitamos de la lista local en memoria
                self.animal_list_display.pop(index)
            else:
                self.status_message = "❌ Error en el repositorio al eliminar."
                
        except IndexError:
            self.status_message = "❌ Índice no válido. (La lista tiene {len(self.animal_list_display)} elementos)"
        except Exception as e:
            self.status_message = f"❌ Error inesperado: {e}"