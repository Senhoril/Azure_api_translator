import requests, uuid, json

# SUA CHAVE E ENDPOINT
key = "your key here"
endpoint = "https://api.cognitive.microsofttranslator.com/"

location = "global"  # ou a região que você escolheu ao criar o recurso

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'pt',
    'to': 'en'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


# Lê o conteúdo do arquivo original
with open("entrada.txt", "r", encoding="utf-8") as file:
    original_text = file.read()

# Divide em blocos (limite da API é ~5000 caracteres por vez)
body = [{'text': original_text}]

# Envia o texto para tradução
response = requests.post(constructed_url, params=params, headers=headers, json=body)
response.raise_for_status()
result = response.json()

# Extrai a tradução
translated_text = result[0]['translations'][0]['text']

# Salva no novo arquivo
with open("traduzido.txt", "w", encoding="utf-8") as file:
    file.write(translated_text)

print("Tradução concluída! Veja o arquivo 'traduzido.txt'.")