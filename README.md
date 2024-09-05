# 🗂️ Desk Organizer

Este proyecto es una aplicación simple para organizar carpetas en tu escritorio. Utiliza Flask para el backend y npm para manejar tareas de frontend. ¡Sigue los pasos a continuación para ejecutar la aplicación en tu máquina!

## 🚀 Requisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- **Python 3** 🐍
- **Node.js** 🍃

## 🔧 Instalación y Ejecución

1. **Clona el repositorio**

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. **Configura el entorno en Terminal 1 🖥️**

    En la primera terminal, necesitarás crear y activar un entorno virtual de Python, instalar Flask y ejecutar el servidor:

    ```bash
    # Crear un entorno virtual
    python3 -m venv newenv

    # Activar el entorno virtual
    source newenv/bin/activate  # En Linux/Mac
    newenv\Scripts\activate      # En Windows

    # Instalar Flask
    pip install Flask

    # Ejecutar la app Flask
    python app.py
    ```

    El servidor Flask se ejecutará en [http://localhost:5000](http://localhost:5000).

3. **Ejecuta npm en Terminal 2 📦**

    En otra terminal, ejecuta el siguiente comando para levantar el entorno de frontend:

    ```bash
    npm start
    ```

    Esto iniciará el servidor de desarrollo y abrirá la aplicación en el navegador.

## 📁 Estructura del Proyecto

- `app.py`: Código backend en Flask.
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
- `templates/`: Plantillas HTML.
- `renderer.js`: Lógica para manejar la interacción del frontend.

## 🛠️ Desarrollo

Si haces cambios en el código y quieres probar, simplemente reinicia el servidor Flask o actualiza la página del navegador para ver los cambios. También puedes hacer lo siguiente:

- Para instalar dependencias nuevas: `pip install <nombre-paquete>` o `npm install`.
- Para desactivar el entorno virtual: `deactivate`.

¡Y eso es todo! 🎉 Con estos pasos tendrás tu aplicación ejecutándose localmente. ¡Disfruta de tu organizador de escritorio! 🗃️

### Notas adicionales:

- Si necesitas más dependencias de npm, agrégalas en el archivo `package.json`.
- Si estás en un sistema Windows, asegúrate de usar `newenv\Scripts\activate` para activar el entorno virtual.
