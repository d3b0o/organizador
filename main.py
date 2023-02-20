import os, shutil

carpetas = {}
while True:
    nombre_carpeta = input("Ingrese el nombre de la carpeta: ")
    extensiones = input("Ejemplo: jpg,png,mp4\nIngrese las extensiones separadas por comas: ").split(",")
    
    carpetas[nombre_carpeta] = extensiones

    seguir = input("¿Desea ingresar otra carpeta? (s/n): ")
    if seguir.lower() != "s":
        break


for folder in carpetas:
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    for extension in carpetas[folder]:
        for file in os.listdir():
            if file.endswith(extension):
                shutil.move(file, os.path.join(folder, file))
	
