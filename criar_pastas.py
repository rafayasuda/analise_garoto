import os

# Nome da pasta raiz do projeto
root_folder = "garoto-choro-analise-computacional"

# Lista de subpastas que serão criadas dentro da pasta principal
folders = [
    "data",
    "figures",
    "notebooks",
    "scripts",
    "results",
    "docs"
]

# Cria a pasta principal
os.makedirs(root_folder, exist_ok=True)

# Cria as subpastas
for folder in folders:
    os.makedirs(os.path.join(root_folder, folder), exist_ok=True)

print(f"Estrutura de projeto criada com sucesso em: {os.path.abspath(root_folder)}")
