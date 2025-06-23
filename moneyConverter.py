import requests
import time

def CalcularTempo(funcao): 
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        return resultado
    return wrapper

@CalcularTempo
def MoneyConverter(mda_origem, mda_destino, valor):
    if valor < 0:
        raise ValueError("O valor convertido não pode ser negativo.")
    if mda_origem == '':
        mda_origem = 'USD'
    if mda_destino == '':
        mda_destino = 'EUR'
    # Set defaults before constructing URL and making API call
    url = f"https://economia.awesomeapi.com.br/last/{mda_origem}-{mda_destino}"
    response = requests.get(url)
    
    data = response.json()
    key = f"{mda_origem}{mda_destino}"
    if key not in data or 'bid' not in data[key]:
        raise KeyError(f"Chave '{key}' ou 'bid' não encontrada na resposta da API: {data}")
    cotacao = data[key]['bid']
    print(f"Valor de 1.00 {mda_origem} é de {cotacao} {mda_destino}.")
    valor_convertido = float(cotacao) * valor
    return valor_convertido

m_origem = input('Informe a moeda de origem (ex: USD): ').upper()
m_destino = input('Informe a moeda de destino (ex: EUR): ').upper()
valor_converter = float(input(f'Informe o valor a ser convertido: '))
valor_convertido=MoneyConverter(m_origem, m_destino, valor_converter)
print(f'{valor_converter:.2f} {m_origem} é igual a {valor_convertido:.2f} {m_destino}.')
