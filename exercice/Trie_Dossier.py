from pathlib import Path

chemin = Path('/Users/berou/Documents/FormationPython/StructureDossier')

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}


for dossier_principal, sous_dossiers in d.items():
    for dossier in sous_dossiers:
        print(dossier)
        chemin_dossier = Path(chemin) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)