import tkinter as tk
from tkinter import ttk, messagebox
import os
import shutil
from pathlib import Path

# Definir la lógica de tu programa aquí
def organizar_escritorio():
    desktop = Path(os.path.join(os.path.join(os.environ['HOME']), 'Desktop'))  # Ruta del escritorio
    for i in range(lista_carpetas.size()):
        carpeta_info = lista_carpetas.get(i)
        nombre_carpeta, tipos_archivos = carpeta_info.split(" (")
        tipos_archivos = tipos_archivos[:-1]  # Remove the closing parenthesis

        # Crear la carpeta en el escritorio si no existe
        carpeta_path = desktop / nombre_carpeta
        carpeta_path.mkdir(exist_ok=True)

        # Mover archivos de los tipos especificados a la carpeta
        for tipo in tipos_archivos.split(","):
            tipo = tipo.strip()
            for archivo in desktop.glob(f"*.{tipo}"):
                shutil.move(str(archivo), carpeta_path / archivo.name)
                print(f"Moviendo {archivo.name} a {carpeta_path}")

# Función para agregar una nueva carpeta y su tipo de archivo
def agregar_carpeta():
    nombre_carpeta = entry_carpeta.get()
    tipos_archivos = entry_tipos.get()
    if nombre_carpeta and tipos_archivos:
        lista_carpetas.insert(tk.END, f"{nombre_carpeta} ({tipos_archivos})")
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar el nombre de la carpeta y los tipos de archivos.")

# Configuración básica de la interfaz
root = tk.Tk()
root.title("Organizador de Escritorio")

# Entrada para agregar nuevas carpetas
ttk.Label(root, text="Nombre de la carpeta:").grid(column=0, row=0, padx=10, pady=5, sticky='W')
entry_carpeta = ttk.Entry(root)
entry_carpeta.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Tipos de archivos (separados por coma):").grid(column=0, row=1, padx=10, pady=5, sticky='W')
entry_tipos = ttk.Entry(root)
entry_tipos.grid(column=1, row=1, padx=10, pady=5)

ttk.Button(root, text="Agregar Carpeta", command=agregar_carpeta).grid(column=0, row=2, columnspan=2, pady=10)

# Lista de carpetas agregadas
lista_carpetas = tk.Listbox(root, width=50)
lista_carpetas.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Botón para organizar el escritorio
ttk.Button(root, text="Organizar Escritorio", command=organizar_escritorio).grid(column=0, row=4, columnspan=2, pady=10)

# Ejecutar la interfaz
root.mainloop()