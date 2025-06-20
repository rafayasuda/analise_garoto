from music21 import converter, stream, analysis, harmony, roman
import pandas as pd

# Carregando os dois movimentos
try:
    score1 = converter.parse("jorgedofusa.mvt1.mxl")
except Exception as e:
    print("Erro ao carregar jorgedofusa.mvt1.mxl:", e)
    score1 = None

try:
    score2 = converter.parse("jorgedofusa.mvt2.mxl")
except Exception as e:
    print("Erro ao carregar jorgedofusa.mvt2.mxl:", e)
    score2 = None

if score1 is None or score2 is None:
    print("❌ Falha ao carregar os arquivos.")
    exit()

# Junta os movimentos
full_score = stream.Score()
full_score.append(score1.parts[0])
full_score.append(score2.parts[0])

# Estima a tonalidade
tonality = full_score.analyze('key')
print(f"Tonalidade estimada: {tonality.tonic.name} {tonality.mode}")

# Chordify e extração de acordes
chords = full_score.chordify()
chords = chords.flatten().getElementsByClass('Chord')

# Extrai cifras e acordes
data = []
for chord in chords:
    if chord.isTriad() or chord.isSeventh():
        try:
            rn = roman.romanNumeralFromChord(chord, tonality)
            data.append({
                'Offset': chord.offset,
                'Acorde': chord.pitchedCommonName,
                'Cifra_RomanNumeral': str(rn.figure)
            })
        except:
            data.append({
                'Offset': chord.offset,
                'Acorde': chord.pitchedCommonName,
                'Cifra_RomanNumeral': 'N/A'
            })

# Salva em CSV
df = pd.DataFrame(data)
df.to_csv("progressao_harmonica_jorge_do_fusa.csv", index=False, encoding='utf-8-sig')

print("✅ Arquivo gerado: progressao_harmonica_jorge_do_fusa.csv")
