import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo
df = pd.read_csv("resumo_acustico.csv")

# Converte vírgulas para ponto decimal, se necessário
df["MFCC_Médio"] = df["MFCC_Médio"].astype(str).str.replace(",", ".").astype(float)
df["Tempo estimado (BPM)"] = df["Tempo estimado (BPM)"].astype(str).str.replace(",", ".").astype(float)

# Plota o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df["MFCC_Médio"], df["Tempo estimado (BPM)"], s=100, edgecolors='k')
plt.xlabel("MFCC Médio")
plt.ylabel("Tempo Estimado (BPM)")
plt.title("Gráfico de Dispersão: MFCC Médio vs. Tempo (BPM)")
plt.grid(True)
plt.tight_layout()

# Salva como imagem
plt.savefig("figura5_dispersao_mfcc_bpm.png", dpi=300)
plt.show()
