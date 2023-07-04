import requests
from bs4 import BeautifulSoup

url = 'https://www.kabum.com.br/busca/Teclado?page_number=1&page_size=100&facet_filters=&sort=most_searched'

headers = {
    'User-Agent':"Mozila/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chorme/86.0.4240.198 Salfari/537.36"
}

site = requests.get(url, headers=headers)
soup =  BeautifulSoup(site.content, 'html.parser')

for i in range(1,10):
    url_pag = f'https://www.kabum.com.br/busca/Teclado?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
    teclados = soup.find_all('div', class_='sc-d55b419d-7 ffpHYT productCard')
    site = requests.get(url_pag, headers=headers)
    soup =  BeautifulSoup(site.content, 'html.parser')

    with open ('precos_teclados.csv', 'a', encoding='UTF-8') as t:
        for teclado in teclados:
            nome = teclado.find('span', class_='sc-d99ca57-0 kUQyzS sc-d55b419d-16 fMikXK nameCard').get_text().strip()
            preco = teclado.find('span', class_='sc-3b515ca1-2 gybgF priceCard').get_text().strip()
            num_price = preco[3:]
            num_price = num_price.replace('.', '')
            num_preco = num_price.split(',')
            linha = nome + ';' + num_preco[0] + '\n'
            t.write(linha)
