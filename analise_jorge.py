from music21 import converter, analysis, chord, interval

# Carrega a partitura
score = converter.parse("Jorge_do_Fusa.mxl")

# Tonalidade global
key = score.analyze('key')
print("Tonalidade global:", key)

# Modulações (apenas em compassos válidos)
print("\nModulações detectadas:")
modulations = []
measures = score.parts[0].getElementsByClass('Measure')
for i, measure in enumerate(measures):
    try:
        k = measure.analyze('key')
        modulations.append((i + 1, k))
        print(f"Compasso {i + 1}: {k}")
    except Exception:
        continue

# Harmonia: tentativa de cifragem (acordes básicos)
if len(score.parts) > 1:
    harmony = score.parts[1].chordify().flatten()
else:
    harmony = score.parts[0].chordify().flatten()

print("\nProgressões harmônicas (10 primeiros acordes detectados):")
for i, el in enumerate(harmony.recurse().getElementsByClass('Chord')):
    if i >= 10:
        break
    try:
        root = el.root().name  # nota raiz
        quality = el.quality   # tipo do acorde (major, minor, etc.)
        print(f"{i + 1}: {root} ({quality})")
    except Exception:
        print(f"{i + 1}: acorde não identificado")

# Melodia (n-gramas intervalares)
melody = score.parts[0].flatten().notes
intervals = []
for n1, n2 in zip(melody[:-1], melody[1:]):
    try:
        iv = interval.Interval(n1, n2)
        intervals.append(iv.directedName)
    except:
        continue

bigrams = list(zip(intervals[:-1], intervals[1:]))
print("\nBigramas intervalares (10 primeiros):")
print(bigrams[:10])

# Forma musical estimada (exemplo)
print("\nSegmentação formal (estimativa):")
sections = ['A', 'A', 'B', 'A']  # Adapte conforme sua análise da obra
for i, label in enumerate(sections):
    print(f"Seção {label} – Compassos {i*8 + 1} a {(i+1)*8}")
