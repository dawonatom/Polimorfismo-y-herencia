# Enciclopedia de Animales (Demo MVVM-R) 🐾

Este es un proyecto de consola en Python que demuestra la implementación de patrones de arquitectura de software avanzados (MVVM-R) para gestionar una "enciclopedia" de animales. El proyecto evolucionó desde un simple ejercicio de polimorfismo hasta una aplicación completa con persistencia en la nube.

El objetivo principal es mostrar la **separación de responsabilidades** (Separation of Concerns), creando un código limpio, mantenible y fácilmente escalable, incluso en una aplicación de consola.

## ✨ Características

  * **Arquitectura Limpia:** Implementa el patrón **MVVM-R** (Model-View-ViewModel-Repository).
  * **Base de Datos en la Nube:** Conectado a **Google Firestore** (Firebase) para persistencia de datos en tiempo real.
  * **Funcionalidad CRUD Completa:**
      * **C**reate: Registrar nuevos animales.
      * **R**ead: Ver la lista completa y los detalles de cada animal.
      * **D**elete: Eliminar animales de la enciclopedia.
  * **Modelo de Dominio Polimórfico:** Utiliza **Herencia** y **Polimorfismo** (la superclase `Animal` y subclases `Perro`, `Vaca`, `Abeja`).
  * **Atributos Dinámicos:** Permite añadir atributos personalizados (ej. `color`, `habitat`) a cualquier animal al momento del registro.
  * **Interfaz de Consola Interactiva:** Menús claros para la interacción del usuario.
  * **Logging Mejorado:** Usa `colorama` para mostrar mensajes específicos del repositorio (ej. `[Firebase]`) en color.

## 🏗️ Arquitectura (MVVM-R)

El proyecto está estrictamente separado en cuatro capas:

1.  **Modelo (Model - `model.py`):**

      * Define la estructura de los datos (las clases `Animal`, `Perro`, `Vaca`, `Abeja`).
      * Contiene la lógica de negocio (métodos como `hablar()` o `to_dict()`).
      * No sabe nada sobre la base de datos ni la interfaz.

2.  **Vista (View - `view.py`):**

      * Es la interfaz de usuario (la consola).
      * Es "tonta": solo es responsable de mostrar información y capturar la entrada del usuario.
      * Usa `print()` e `input()`.
      * Llama a "Comandos" en el ViewModel, pero no sabe *qué* hacen.

3.  **Modelo de Vista (ViewModel - `viewmodel.py`):**

      * Maneja el estado de la aplicación (ej. qué animal está seleccionado, la lista de animales cargada).
      * Provee "Comandos" (métodos) que la Vista puede llamar (ej. `load_animals_command()`).
      * **No habla directamente con la base de datos**. Le pide los datos al Repositorio.

4.  **Repositorio (Repository - `repository.py`):**

      * Es la **única** capa que sabe cómo hablar con la base de datos (Firebase).
      * Abstrae toda la lógica de `get`, `add`, `delete` de Firestore.
      * Entrega al ViewModel objetos `Model` o diccionarios limpios.

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1\. Requisitos Previos

  * Python 3.7 o superior.
  * `pip` (el gestor de paquetes de Python).
  * Una cuenta de Google para crear un proyecto de Firebase.

### 2\. Configuración del Proyecto

1.  **Clona el repositorio** (o descarga los archivos en una carpeta):

    ```bash
    # (Si estás usando git)
    git clone https://github.com/dawonatom/Polimorfismo-y-herencia.git
    ```

2.  **Crea un entorno virtual** (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    .\venv\Scripts\activate   # En Windows
    ```

3.  **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

### 3\. Configuración de Firebase

1.  Ve a la [Consola de Firebase](https://console.firebase.google.com/).
2.  Crea un nuevo proyecto.
3.  En el menú de la izquierda, ve a **Compilación \> Firestore Database**.
4.  Haz clic en **Crear base de datos**.
5.  Inicia en **Modo de prueba** (esto permite leer y escribir sin reglas de seguridad).
6.  En la consola, haz clic en el ícono de engranaje ⚙️ (junto a "Descripción general del proyecto") \> **Configuración del proyecto**.
7.  Ve a la pestaña **Cuentas de servicio**.
8.  Haz clic en el botón **"Generar nueva clave privada"** y confirma.
9.  Esto descargará un archivo `.json`. **Renómbralo a `serviceAccountKey.json`** y colócalo en la misma carpeta donde está `main.py`.

**¡IMPORTANTE\!** Nunca subas tu archivo `serviceAccountKey.json` a un repositorio público (añádelo a tu `.gitignore`).

## 🏃‍♂️ Cómo Usar

Una vez que tengas las dependencias instaladas y el archivo `serviceAccountKey.json` en su lugar, simplemente ejecuta `main.py`:

```bash
python main.py
```

Aparecerá el menú principal en tu consola, permitiéndote registrar, ver y eliminar animales de tu base de datos en Firebase.

## 📂 Estructura de Archivos

```
.
├── 📂 venv/              # Entorno virtual
├── 📜 main.py            # Punto de entrada. Inicia y conecta las capas.
├── 📜 model.py           # La capa de Modelo (Clases Animal, Perro, Vaca, Abeja).
├── 📜 view.py            # La capa de Vista (Maneja todos los 'print' e 'input').
├── 📜 viewmodel.py        # La capa de ViewModel (Lógica de la UI, comandos).
├── 📜 repository.py       # La capa de Repositorio (Habla con Firebase).
├── 📜 serviceAccountKey.json # Tu clave privada de Firebase (¡SECRETO!)
└── 📜 requirements.txt    # Lista de dependencias
```