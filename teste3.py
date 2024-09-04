import json

with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)

faturamentos = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento superior à média mensal: {dias_acima_da_media} dias")
