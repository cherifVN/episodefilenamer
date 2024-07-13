import os
import re
episode = int(input("Episode ou Spécial ? (Saisir 1 pour Episode ou 2 pour Spécial) : "))
# Chemin du dossier contenant les fichiers
file_path = os.path.dirname(__file__)
# Liste des fichiers dans le dossier
files = os.listdir(file_path)
# Parcourir chaque fichier
for file in files:
    # Vérifier si le nom du fichier contient un chiffre
    match = re.search("\d+", file)
    if match:
        # Si un chiffre est trouvé, renommer le fichier
        episode_number = match.group(0)
        if episode == 1:
            new_filename = f"Episode {episode_number}.mp4"
        elif episode == 2:
            new_filename = f"Special {episode_number}.mp4"
        os.rename(os.path.join(file_path, file), os.path.join(file_path, new_filename))
        print(f"Renommé {file} en {new_filename}")
