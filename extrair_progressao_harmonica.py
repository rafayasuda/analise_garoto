from music21 import converter, roman
import pandas as pd

# Carregar os arquivos MusicXML
score1 = converter.parse("caminho_para/jorgedofusa.mvt1.mxl")
score2 = converter.parse("caminho_para/jorgedofusa.mvt2.mxl")

def extract_progression(score):
    chords = score.chordify()
    progression = []
    for c in chords.recurse().getElementsByClass('Chord'):
        try:
            rn = roman.romanNumeralFromChord(c, score.analyze('key'))
            progression.append(rn.figure)
        except:
            progression.append("N/A")
    return progression

prog1 = extract_progression(score1)
prog2 = extract_progression(score2)

df = pd.DataFrame({
    "Compasso": list(range(1, max(len(prog1), len(prog2)) + 1)),
    "Movimento 1": prog1 + [""] * (len(prog2) - len(prog1)),
    "Movimento 2": prog2 + [""] * (len(prog1) - len(prog2)),
})

print(df)
df.to_csv("progressao_harmonica_jorge.csv", index=False)
