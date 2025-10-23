# main.py

from view import SimulatedView
from viewmodel import AnimalViewModel
from repository import AnimalRepository

if __name__ == "__main__":
    
    # 1. Define la ruta a tu clave de Firebase
    KEY_PATH = "serviceAccountKey.json"
    
    # 2. Crea las instancias (inyectando dependencias)
    #    (main) -> crea Repositorio
    #    (main) -> crea ViewModel (y le pasa el Repositorio)
    #    (main) -> crea Vista (y le pasa el ViewModel)
    
    try:
        repo = AnimalRepository(KEY_PATH)
        vm = AnimalViewModel(repo)
        app_view = SimulatedView(vm)
        
        # 3. Inicia la aplicación
        app_view.run_interactive_session()
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{KEY_PATH}'.")
        print("Asegúrate de descargar la clave de servicio de Firebase y guardarla en la misma carpeta.")
    except Exception as e:
        print(f"Error crítico al iniciar: {e}")