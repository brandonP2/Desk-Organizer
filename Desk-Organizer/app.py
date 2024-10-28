from flask import Flask, request, jsonify
import os
import shutil
from pathlib import Path

app = Flask(__name__)

# Ruta del escritorio
desktop = Path(os.path.join(os.path.join(os.environ['HOME']), 'Desktop'))

# Verificar la ruta del escritorio
print("Ruta del escritorio:", desktop)

@app.route('/api/organize', methods=['POST'])
def organize():
    try:
        # Verifica si se recibe la solicitud
        print("Solicitud recibida en /api/organize")  
        data = request.json
        print("Datos recibidos:", data)  
        
        folders = data.get('folders', [])
        print("Carpetas recibidas para organizar:", folders)  

        for folder in folders:
            nombre_carpeta = folder['nombre']
            tipos_archivos = folder['tipos']

            # Crear la carpeta en el escritorio si no existe
            carpeta_path = desktop / nombre_carpeta
            print("Intentando crear la carpeta:", carpeta_path)  
            carpeta_path.mkdir(exist_ok=True)
            print(f"Carpeta '{nombre_carpeta}' creada o ya existente en el escritorio.")

            # Mover archivos de los tipos especificados a la carpeta
            for tipo in tipos_archivos.split(","):
                tipo = tipo.strip()
                archivos_encontrados = list(desktop.glob(f"*.{tipo}"))
                print(f"Archivos encontrados para mover con extensión .{tipo}: {archivos_encontrados}")
                for archivo in archivos_encontrados:
                    shutil.move(str(archivo), carpeta_path / archivo.name)
                    print(f"Archivo '{archivo.name}' movido a '{carpeta_path}'")

        return jsonify({"status": "organized"}), 200
    except Exception as e:
        print("Error en el servidor:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)

