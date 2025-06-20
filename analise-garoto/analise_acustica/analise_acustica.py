import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Carregar o áudio
audio_path = 'jorge_do_fusa.mp3.mp3'  # certifique-se de que o nome e caminho estão corretos
y, sr = librosa.load(audio_path)

# Cromagrama
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

# MFCCs
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Beat tracking
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

# Energia (intensidade dinâmica)
rms = librosa.feature.rms(y=y)[0]

# Gráfico: Cromagrama
plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', sr=sr)
plt.colorbar()
plt.title('Cromagrama')
plt.tight_layout()
plt.savefig("cromagrama.png")
plt.close()

# Gráfico: MFCCs
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time', sr=sr)
plt.colorbar()
plt.title('MFCCs')
plt.tight_layout()
plt.savefig("mfccs.png")
plt.close()

# Gráfico: Curva de energia
frames = range(len(rms))
times = librosa.frames_to_time(frames, sr=sr)

plt.figure(figsize=(10, 4))
plt.plot(times, rms, label='Energia RMS')
plt.xlabel('Tempo (s)')
plt.ylabel('Intensidade')
plt.title('Curva de Energia da Performance')
plt.legend()
plt.tight_layout()
plt.savefig("curva_energia.png")
plt.close()

# Dados resumidos
dados = {
    'Tempo estimado (BPM)': [tempo],
    'Número de batidas detectadas': [len(beats)],
    'Média de energia RMS': [np.mean(rms)],
    'Desvio padrão RMS': [np.std(rms)]
}

df = pd.DataFrame(dados)
df.to_csv("resumo_acustico.csv", index=False)

print("\n✅ Análise acústica concluída.")
print("Gráficos e resumo exportados como arquivos:\n- cromagrama.png\n- mfccs.png\n- curva_energia.png\n- resumo_acustico.csv")
