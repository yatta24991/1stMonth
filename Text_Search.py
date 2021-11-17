'''
Função para saber se uma determinada palavra chave está presente num ficheiro txt
'''
import re

def txt_search(file):
    keyword_lower = keyword.lower()
    with open(file) as f:
        txt = f.read().lower()
        txt_final = re.sub(r'[^\w\s]', '', txt) #função usada para retirar a pontuação
        txt_list = txt_final.split(' ')
        if keyword_lower in txt_list:
            print('Keyword found!')
        else:
            print('Keyword not found!')

filename = input('Enter the filename (with .txt): ')
keyword = input('Enter the keyword: ')
txt_search(filename)