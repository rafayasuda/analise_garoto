from music21 import converter, analysis, chord, interval, stream, key, note
import pandas as pd

# Carrega os dois arquivos do choro
score1 = converter.parse("jorgedofusa.mvt1.mxl")
score2 = converter.parse("jorgedofusa.mvt2.mxl")

# Combina em uma única partitura
score = stream.Score()
score.append(score1.parts)
score.append(score2.parts)

# Tonalidade global
global_key = score.analyze('key')

# Modulações por compasso
modulations = []
for measure in score.parts[0].getElementsByClass(stream.Measure):
    try:
        local_key = measure.analyze('key')
        modulations.append((measure.number, local_key.name))
    except:
        continue

# Progressões harmônicas (primeiros 15 acordes)
chords = score.chordify().recurse().getElementsByClass('Chord')
progressions = [c.pitchedCommonName for c in chords[:15]]

# Bigramas melódicos
melody_notes = score.parts[0].recurse().notes
intervals = []
for i in range(len(melody_notes) - 1):
    if isinstance(melody_notes[i], note.Note) and isinstance(melody_notes[i+1], note.Note):
        interv = interval.Interval(noteStart=melody_notes[i], noteEnd=melody_notes[i+1])
        intervals.append(interv.name)
ngrams = [(intervals[i], intervals[i + 1]) for i in range(len(intervals) - 1)][:15]

# Forma musical (estimativa simples)
sections = [
    ("A", 1, 8),
    ("A", 9, 16),
    ("B", 17, 24),
    ("A", 25, 32)
]

# Estrutura em tabela
df = pd.DataFrame({
    "Tonalidade Global": [global_key.name],
    "Modulações (compasso)": [modulations],
    "Progressões Harmônicas": [progressions],
    "Bigramas Melódicos": [ngrams],
    "Forma Estimada": [sections]
})

print(df.to_string(index=False))
