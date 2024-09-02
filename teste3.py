import json

def calcular_media(faturamentos):
    total_faturamento = sum(faturamento for faturamento in faturamentos if faturamento > 0)
    dias_com_faturamento = len([f for f in faturamentos if f > 0])
    return total_faturamento / dias_com_faturamento if dias_com_faturamento > 0 else 0

def processar_faturamento(json_data):
    dados = json.loads(json_data)
    
    faturamentos = [item['valor'] for item in dados['faturamento']]
    
    menor_faturamento = min(faturamentos)
    
    maior_faturamento = max(faturamentos)
    
    media_faturamento = calcular_media(faturamentos)
    
    dias_acima_da_media = len([f for f in faturamentos if f > media_faturamento])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

json_data = '''
{
  "faturamento": [
    {"dia": 1, "valor": 200},
    {"dia": 2, "valor": 150},
    {"dia": 3, "valor": 0},
    {"dia": 4, "valor": 300},
    {"dia": 5, "valor": 250},
    {"dia": 6, "valor": 350},
    {"dia": 7, "valor": 50}
  ]
}
'''

menor, maior, dias_acima = processar_faturamento(json_data)
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento superior à média: {dias_acima}")
