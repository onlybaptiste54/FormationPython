from pathlib import Path


EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents"}

Base_dir = Path('/Users/berou/Documents/FormationPython/exercice/data')
#Le but c'est de trier les fichiers selon leur type( et donc leur extension) dans des sous-dossier 
# Déjà je vais essayer de trier les clés par leur valeur. 
for f in Base_dir.iterdir() :
    if f.is_file():

        Chemin_final = EXTENSIONS_MAPPING.get(f.suffix,"Divers")
        
        New_Dir = Base_dir / Chemin_final
        
        New_Dir.mkdir(parents=True, exist_ok=True)
        
        fichier_cible = New_Dir / f.name
        # On déplace le fichier
        f.rename(fichier_cible)
        print(f"Dossier {New_Dir} créé ou déjà existant.")
        
