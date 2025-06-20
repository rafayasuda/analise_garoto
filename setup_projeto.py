import os

# Nome da pasta principal
root_dir = "analise-garoto"

# Subpastas
folders = [
    "analise_simbólica",
    "analise_acustica",
    "integracao",
    "artigo"
]

# Arquivos iniciais
files = {
    "README.md": "# Análise Musical de Garoto\nEste repositório contém a análise simbólica e acústica da obra de Garoto.",
    "requirements.txt": "librosa==0.9.2\nmusic21==6.1.0\npandas\nmatplotlib\nscikit-learn\nnumpy==1.23.5\nscipy==1.9.3"
}

# Cria a estrutura
os.makedirs(root_dir, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(root_dir, folder), exist_ok=True)

# Cria arquivos de texto iniciais
for filename, content in files.items():
    with open(os.path.join(root_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Cria um artigo de exemplo em Word (docx) dentro da pasta artigo
with open(os.path.join(root_dir, "artigo", "sbcm_artigo2025.docx"), "wb") as f:
    f.write(b"")  # Arquivo vazio por enquanto

print("✅ Estrutura de projeto criada com sucesso em 'analise-garoto/'.")
