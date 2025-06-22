import requests;

def MoneyConverter(mda_origem, mda_destino, valor):
    url = f"https://economia.awesomeapi.com.br/last/{mda_origem}-{mda_destino}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cotacao = data[f"{mda_origem}{mda_destino}"]['bid']
        valor_convertido = float(cotacao) * valor
        return valor_convertido
    else:
        raise Exception("Erro ao consultar a API de câmbio.")
    
m_origem=input('Informe a moeda de origem (ex: USD): ').upper();
m_destino=input('Informe a moeda de destino (ex: EUR): ').upper();
valor_converter=float(input(f'Informe o valor a ser convertido: '));
valor_convertido=MoneyConverter(m_origem, m_destino, valor_converter);
print(f'{valor_converter:.2f} {m_origem} é igual a {valor_convertido:.2f} {m_destino}.');
