from music21 import converter, stream

# Carregar os dois arquivos separadamente
score1 = converter.parse("jorgedofusa.mvt1.mxl")
score2 = converter.parse("jorgedofusa.mvt2.mxl")

# Unir os dois movimentos
combined_score = stream.Score()
for part1, part2 in zip(score1.parts, score2.parts):
    combined_part = stream.Part()
    combined_part.append(part1)
    combined_part.append(part2)
    combined_score.append(combined_part)

# Salvar como partitura combinada se quiser
# combined_score.write('musicxml', fp='jorge_completo.mxl')

# Exemplo de análise: tonalidade global
key = combined_score.analyze('key')
print("Tonalidade global combinada:", key)

# Analisar modulações por compasso (parte 1 como referência)
print("\nModulações detectadas por compasso:")
for i, measure in enumerate(combined_score.parts[0].getElementsByClass('Measure')):
    try:
        k = measure.analyze('key')
        print(f"Compasso {i + 1}: {k}")
    except:
        continue
