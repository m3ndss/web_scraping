import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

#baixa a página
resposta = requests.get(url)
resposta.raise_for_status()

#analisa o HTML
soup = BeautifulSoup(resposta.text, "html.parser")

#encontra as frases
frases = soup.select(".text")

#exibe e salva as frases
with open("frases.txt", "w", encoding="utf-8") as arquivo:

    for frase in frases:
        texto = frase.get_text()
        print(texto)
        arquivo.write(texto + "\n")

print("\nscraping concluído!")
print("as frases foram salvas no arquivo frases.txt.")