document.addEventListener("DOMContentLoaded", () => {
  const foldersContainer = document.getElementById("folders-container");
  const modal = document.getElementById("add-folder-modal");
  const closeModalButton = document.querySelector(".close-button");
  const addFolderButton = document.getElementById("add-folder-button");
  const sortAZButton = document.getElementById("sort-az-button"); // Botón A-Z
  let localFolders = []; // Array para almacenar las carpetas localmente en la app

  // Función para limpiar el formulario del modal
  function clearForm() {
    document.getElementById("folder-name").value = '';
    document.getElementById("file-types").value = '';
  }

  // Función para actualizar la lista de carpetas en la UI
  function updateFolderList() {
    foldersContainer.innerHTML = ""; 
    localFolders.forEach((folder, index) => {
      const folderCard = document.createElement("div");
      folderCard.className = "folder-card";

      const folderTitle = document.createElement("h3");
      folderTitle.textContent = folder.nombre;

      const folderTypesLabel = document.createElement("p");
      folderTypesLabel.textContent = "Tipos de archivos:";
      folderTypesLabel.style.color = "#3c763d"; 

      const folderTypesValue = document.createElement("p");
      folderTypesValue.textContent = folder.tipos;
      folderTypesValue.style.color = "#000"; 
      folderTypesValue.style.marginTop = "10px"; 
      // Botón de eliminar (X)
      const deleteButton = document.createElement("span");
      deleteButton.className = "delete-button";
      deleteButton.textContent = "X";
      deleteButton.onclick = () => {
        localFolders.splice(index, 1);  
        updateFolderList();  
      };

      folderCard.appendChild(folderTitle);
      folderCard.appendChild(folderTypesLabel);
      folderCard.appendChild(folderTypesValue);
      folderCard.appendChild(deleteButton);
      foldersContainer.appendChild(folderCard);
    });
  }

  // Evento para abrir el modal de agregar carpeta
  addFolderButton.addEventListener("click", () => {
    clearForm(); 
    modal.style.display = "block"; 
  });

  // Cerrar el modal cuando se hace clic en la "X"
  closeModalButton.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Cerrar el modal cuando se hace clic fuera del contenido del modal
  window.addEventListener("click", (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });

  // Manejar el formulario de agregar carpeta
  document.getElementById("add-folder-form").addEventListener("submit", (event) => {
    event.preventDefault();

    const nombreCarpeta = document.getElementById("folder-name").value;
    const tiposArchivos = document.getElementById("file-types").value;

    if (nombreCarpeta && tiposArchivos) {
      // Almacenar la carpeta localmente
      localFolders.push({
        nombre: nombreCarpeta,
        tipos: tiposArchivos
      });

      updateFolderList();  
      modal.style.display = "none"; 
    } else {
      alert("Debe completar todos los campos");
    }
  });

  // Evento para ordenar A-Z
  sortAZButton.addEventListener("click", () => {
    localFolders.sort((a, b) => a.nombre.localeCompare(b.nombre));  
    updateFolderList(); 
  });

  // Evento para organizar
  document.getElementById("organize-button").addEventListener("click", () => {
    console.log("Enviando solicitud de organización:", localFolders);
    fetch('http://localhost:5001/api/organize', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        folders: localFolders
      })
    }).then(response => {
      console.log("Respuesta recibida:", response);
      if (response.ok) {
        alert("Escritorio organizado exitosamente");
      } else {
        alert("Error al organizar el escritorio");
      }
    }).catch(error => {
      console.error('Error al organizar el escritorio:', error);
      alert("Error al organizar el escritorio: " + error.message);
    });
  });
});
