from bs4 import BeautifulSoup
import requests
import codecs

def parse():
    url = 'https://omsk.drom.ru/auto/'
    page = requests.get(url)  
    print(page.status_code)  
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', class_='css-1nvf6xk eojktn00')
    description = ''
    for data in block:  
        if data.find('a'):
            description = data.findAll('div', class_='css-16kqa8y e3f4v4l2')
    alphabet_eng = [chr(i) for i in range(65, 91)]
    alphabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    zapis = False
    naming = ''
    for text in str(description):
        for letter in text:
            if ((letter in alphabet_eng) or (letter in alphabet_rus)):
                zapis = True
            if (letter == '<' and zapis):
                zapis = False
                naming += '\n'
            if zapis:
                naming += letter
    file = codecs.open('save.txt','w', 'utf-8')
    file.write(naming)
    file.close