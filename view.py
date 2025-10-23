# view.py

from viewmodel import AnimalViewModel

class SimulatedView:
    def __init__(self, vm: AnimalViewModel):
        self.vm = vm
        print("🐾 Enciclopedia de Animales conectada a Firebase 🐾")

    def _show_animal_summary_list(self):
        """
        Muestra SÓLO la lista resumida de animales.
        Devuelve True si hay animales, False si no.
        """
        print("\n" + "="*30)
        print("   ENCICLOPEDIA - RESUMEN")
        print("="*30)
        
        # Lee la propiedad pública del ViewModel
        if not self.vm.animal_list_display:
            print(f"  {self.vm.status_message}")
            return False # No hay animales para mostrar
        else:
            print(f"  Total: {len(self.vm.animal_list_display)} animales registrados.")
            for i, animal_data in enumerate(self.vm.animal_list_display, 1):
                tipo = animal_data.get('tipo', 'Desconocido')
                especie = animal_data.get('especie', 'N/A')
                print(f"    {i}. {tipo} (Especie: {especie})")
            return True # Sí hay animales

    def _show_animal_detail_view(self):
        """
        Un sub-menú interactivo para pedir detalles de un animal específico
        de la lista que ya se mostró.
        """
        while True:
            choice = input("\n  -> Ingresa el # del animal para ver detalles (o 0 para volver): ")
            try:
                choice_num = int(choice)
                if choice_num == 0:
                    break # Salir del sub-menú de detalles
                
                # Pedimos al VM los datos del animal (recordar: índice = Nro - 1)
                animal_data = self.vm.get_animal_details_by_index(choice_num - 1)
                
                if animal_data:
                    # Si el VM nos da datos, los imprimimos
                    print("\n" + "—"*35)
                    print(f"    DETALLES DE: {animal_data.get('tipo', 'N/A').upper()}")
                    print("—"*35)
                    # No mostramos el 'doc_id' al usuario, es interno
                    for key, value in animal_data.items():
                        if key != 'doc_id': 
                            print(f"     {key.capitalize()}: {value}")
                    print("—"*35)
                else:
                    # El VM retornó None (índice malo)
                    print(f"  ❌ Número '{choice_num}' no está en la lista.")

            except ValueError:
                print("  ❌ Por favor, ingresa solo un número.")

    def _show_register_form(self):
        """Muestra un formulario para registrar un nuevo animal."""
        print("\n" + "="*30)
        print("   REGISTRAR NUEVO ANIMAL")
        print("="*30)
        
        try:
            # --- Datos base ---
            tipo = input("  Tipo (Perro, Vaca, Abeja): ")
            especie = input("  Especie (ej. mamífero, insecto): ")
            edad = int(input("  Edad (número): "))
            
            extra_data = {}
            
            # --- Datos específicos ---
            if tipo.lower() == 'perro':
                extra_data['dueño'] = input("  Dueño del perro: ")
            
            # --- Bucle para atributos dinámicos ---
            while True:
                add_attr = input("\n  ¿Deseas añadir un atributo personalizado? (s/n): ").lower()
                if add_attr != 's':
                    break
                
                attr_key = input("    Nombre del atributo (ej. color, raza, habitat): ")
                attr_value = input(f"    Valor para '{attr_key}': ")
                
                if attr_key:
                    extra_data[attr_key] = attr_value
                else:
                    print("    Nombre de atributo no válido.")
            # --- Fin del bucle ---

            self.vm.register_animal_command(tipo, especie, edad, **extra_data)
            print(f"\n  ESTADO: {self.vm.status_message}")

        except ValueError:
            print("❌ Error: La edad debe ser un número.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    # --- ¡NUEVA VISTA/FUNCIÓN! ---
    def _show_delete_view(self):
        """
        Muestra la lista de animales y pide un número para eliminar.
        """
        print("\n" + "="*30)
        print("   ELIMINAR UN ANIMAL")
        print("="*30)
        
        # 1. Cargar y mostrar la lista de animales
        self.vm.load_animals_command()
        has_animals = self._show_animal_summary_list() # Usamos la misma función
        
        if not has_animals:
            # El VM ya puso un mensaje (ej. "No hay animales")
            return # Salir si no hay nada
        
        # 2. Pedir el número a eliminar
        try:
            choice = input("\n  -> Ingresa el # del animal a ELIMINAR (o 0 para cancelar): ")
            choice_num = int(choice)
            
            if choice_num == 0:
                print("Cancelado.")
                return
            
            # 3. Llamar al comando del ViewModel (índice = Nro - 1)
            self.vm.delete_animal_by_index(choice_num - 1)
            
            # 4. Mostrar el resultado
            print(f"\n  ESTADO: {self.vm.status_message}")
            
        except ValueError:
            print("  ❌ Por favor, ingresa solo un número.")

    def run_interactive_session(self):
        """
        Bucle interactivo principal con todas las opciones.
        """
        while True:
            print("\n--- ¿Qué deseas hacer? ---")
            print("  1. Ver la enciclopedia (Cargar de Firebase)")
            print("  2. Registrar un nuevo animal")
            print("  3. Eliminar un animal") # <-- NUEVO
            print("  4. Salir") # <-- ACTUALIZADO
            
            choice = input("Elige una opción (1-4): ") # <-- ACTUALIZADO

            if choice == '1':
                # 1. Llama al comando para cargar datos en el VM
                self.vm.load_animals_command()
                # 2. Muestra la lista resumen
                has_animals = self._show_animal_summary_list()
                # 3. Si hay animales, entra al sub-menú de detalles
                if has_animals:
                    self._show_animal_detail_view()
                    
            elif choice == '2':
                self._show_register_form()
                
            elif choice == '3': # <-- NUEVO
                self._show_delete_view()
                
            elif choice == '4': # <-- ACTUALIZADO
                print("¡Adiós!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")