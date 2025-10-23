# repository.py

import firebase_admin
from firebase_admin import credentials, firestore

# 1. Importamos las herramientas de colorama
from colorama import Fore, Style, init

# 2. Inicializamos colorama para que funcione en todas las terminales
#    autoreset=True hace que el color vuelva a la normalidad después de cada print.
init(autoreset=True)

# 3. Definimos nuestro tag naranja 🟠
#    Fore.YELLOW es el "naranja" estándar de la terminal.
FIREBASE_TAG = f"{Fore.YELLOW}[Firebase]{Style.RESET_ALL}"


class AnimalRepository:
    def __init__(self, service_account_key_path):
        """
        Inicializa la conexión con Firebase.
        """
        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate(service_account_key_path)
            firebase_admin.initialize_app(cred)
            
        self.db = firestore.client()
        self.collection_ref = self.db.collection('animales')
        
        # 4. Añadimos un mensaje de éxito en la conexión
        print(f"{FIREBASE_TAG} Conexión con Firestore establecida.")

    def register_animal(self, animal_object):
        """
        Recibe un objeto (Perro, Vaca, etc.) y lo guarda en Firebase.
        """
        try:
            animal_data = animal_object.to_dict()
            self.collection_ref.add(animal_data)
            
            # 5. Modificamos el print de éxito
            print(f"{FIREBASE_TAG} ✔️  Registro exitoso de: {animal_data['tipo']}")
            return True
        except Exception as e:
            # 6. Modificamos el print de error
            print(f"{FIREBASE_TAG} ❌ Error al registrar: {e}")
            return False

    def get_all_animals(self):
        """
        Obtiene todos los documentos de la colección 'animales'.
        """
        try:
            docs = self.collection_ref.stream()
            animal_list = [doc.to_dict() for doc in docs]
            return animal_list
        except Exception as e:
            # 7. Modificamos el print de error
            print(f"{FIREBASE_TAG} ❌ Error al obtener animales: {e}")
            return []