
from music21 import converter, stream, note
import pandas as pd

# Carregar e combinar os dois movimentos
part1 = converter.parse("jorgedofusa.mvt1.mxl")
part2 = converter.parse("jorgedofusa.mvt2.mxl")
score = stream.Score()
for p in part1.parts:
    score.append(p)
for p in part2.parts:
    score.append(p)

# Flatten para facilitar análise de frases
flat_notes = score.parts[0].flatten().notes.stream()

# Detecção de frases simples por pausa e métrica
phrases = []
current_phrase = []
for n in flat_notes:
    current_phrase.append(n)
    if isinstance(n, note.Rest) and n.quarterLength >= 1.0:
        if len(current_phrase) > 1:
            phrases.append(current_phrase)
            current_phrase = []

# Adiciona última frase se houver
if current_phrase:
    phrases.append(current_phrase)

# Construir uma lista resumida das frases
phrase_summary = []
for idx, ph in enumerate(phrases):
    dur = sum(n.quarterLength for n in ph)
    first_pitch = ph[0].nameWithOctave if isinstance(ph[0], note.Note) else "-"
    last_pitch = ph[-1].nameWithOctave if isinstance(ph[-1], note.Note) else "-"
    phrase_summary.append({
        "Frase": f"F{idx+1}",
        "Início (compasso)": ph[0].measureNumber,
        "Notas": len(ph),
        "Duração Total": dur,
        "Nota Inicial": first_pitch,
        "Nota Final": last_pitch
    })

# Exportar para CSV
df_frases = pd.DataFrame(phrase_summary)
df_frases.to_csv("frases_jorge_do_fusa.csv", index=False)
print("Arquivo frases_jorge_do_fusa.csv exportado com sucesso.")
