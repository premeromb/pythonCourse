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

def write_on_file(data, word):
    file_output = open(word + '.txt', 'a', encoding="utf-8")
    file_output.write(data)
    file_output.close()


def do_request(soup):

    # TRANSLATIONS
    print(languages[language_to].capitalize() + " Translations:\n")
    write_on_file(languages[language_to].capitalize() + " Translations:\n", word)

    translation = soup.find_all('a', class_='translation')
    translation.pop(0)

    examples = soup.find_all('a', {"class": "translation"})
    examples.pop(0)
    examples.pop()

    print(examples[0].text.strip())
    write_on_file(examples[0].text.strip(), word)
   
    # EXAMPLES
    examples_translated = soup.find_all('div', {"class": "ltr"})

    print("\n\n" + languages[language_to].capitalize() + " Examples:\n")
    write_on_file("\n\n" + languages[language_to].capitalize() + " Examples:\n", word)

    sentence_list = [x.text.strip() for x in soup.select("#examples-content .text")]

    print(f"{sentence_list[2]}\n{sentence_list[3]}\n\n\n")
    write_on_file(f"{sentence_list[2]}\n{sentence_list[3]}\n\n\n", word)

def code_check(status_code):
    print(f"{status_code} OK") if status_code == 200 else print(f"{status_code} NOT OK")

def web_service_connect(url):
    user_agent = 'Mozilla/5.0'
    page = requests.get(url, headers={'User-Agent': user_agent})
    # code_check(page.status_code)
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



def program():
    global language_to
    select_language()
    select_word()

    if language_to == '0':
        for language in languages:
            if language != language_from:
                language_to = language
                set_url()
                do_request(web_service_connect(url))
    else:
        set_url()
        do_request(web_service_connect(url))
        
def test():
    write_on_file("ESTO ES UNA PRUEBITA", 'pruebita')

program()