#!/usr/bin/env python3
"""
Autor: Fábio Berbert de Paula <prefeito@fabio.city>
Data : 26/11/2018
"""

#pip install requests-html
from requests_html import HTMLSession

def cotacao():
    session = HTMLSession()

    #URL resultado da busca no Google por: cotação dólar
    r = session.get('https://www.google.com.br/search?q=cota%C3%A7%C3%A3o+dolar&oq=cota%C3%A7%C3%A3o+dolar&aqs=chrome..69i64j0l5.2721j1j4&sourceid=chrome&ie=UTF-8')

    #ID do span HTML que exibe o valor da cotação no resultado de busca
    selector = '#knowledge-currency__tgt-amount'

    return "R$ " + r.html.find(selector, first=True).text

print(cotacao())
