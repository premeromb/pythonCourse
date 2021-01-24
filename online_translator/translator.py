import requests

from bs4 import BeautifulSoup

languages = {
    '1': 'arabic',
    '2': 'german',
    '3': 'english',
    '4': 'spanish',
    '5': 'french',
    '6': 'hebrew',
    '7': 'japanese',
    '8': 'dutch',
    '9': 'polish',
    '10': 'portuguese',
    '11': 'romanian',
    '12': 'russian',
    '13': 'turkish'
}
language_from = ""
language_to = ""
word = ""
url = " "


def print_data_request(soup):

    # TRANSLATIONS
    print("\n" + languages[language_to].capitalize() + " Translations:")
    
    translation = soup.find_all('a', class_='translation')
    translation.pop(0)

    examples = soup.find_all('a', {"class": "translation"})
    examples.pop(0)
    examples.pop()

    for iterable in range(5):
        if len(examples) > iterable:
                print(examples[iterable].text.strip())

    # EXAMPLES
    examples_translated = soup.find_all('div', {"class": "ltr"})

    counter = 0

    print("\n" + languages[language_to].capitalize() + " Examples:")

    sentence_list = [x.text.strip() for x in soup.select("#examples-content .text")]

    for i in range(5):
        print(f"{sentence_list[i * 2]}\n{sentence_list[i * 2 + 1]}\n")

def code_check(status_code):
    print(f"{status_code} OK") if status_code == 200 else print(f"{status_code} NOT OK")

def web_service_connect(url):
    user_agent = 'Mozilla/5.0'
    page = requests.get(url, headers={'User-Agent': user_agent})
    code_check(page.status_code)
    return BeautifulSoup(page.content, 'html.parser')


def set_url():
    global url
    url = 'https://context.reverso.net/translation/' + languages[language_from] + '-' + languages[language_to] + '/' + word 


def select_language():
    global language_to, language_from
    print("Hello, you're welcome to the translator. Translator supports: ")

    for  key, value in languages.items():
        print(key + ". " + value.capitalize())

    print('Type the number of your language:')
    language_from = input()
    print('Type the number of language you want to translate to: ')
    language_to = input()

def select_word():
    global word
    print("Type the word you want to translate:")
    word = input().lower()

select_language()
select_word()

set_url()

print_data_request(web_service_connect(url))
