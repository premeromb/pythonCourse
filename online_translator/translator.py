import requests

from bs4 import BeautifulSoup


languages = {"fr": "french", "en": "english"}

language_from = ""
language_to = ""
word = ""

def make_request(url):

    user_agent = 'Mozilla/5.0'
    page = requests.get(url, headers={'User-Agent': user_agent})

    if page.status_code == 200:
        print("200 OK")

    soup = BeautifulSoup(page.content, 'html.parser')

    translation = soup.find_all('a', class_='translation')

    tr = []
    for result in translation:
        tr.extend(result.text.split())
    tr.pop()
    tr.pop(0)

    print("\nContext examples: \n")
    print(languages[language_to].capitalize() + " Translations:")

    for index in range(5):
        print(tr[index])
    
    examples = soup.find_all('div', class_='src ltr')

    examples_translated = soup.find_all('div', class_='trg ltr')


    print("\n" + languages[language_to].capitalize() + " Examples:")

    for iterable in range(5):
        print(examples[iterable].text.strip(), end=':\n')
        print(examples_translated[iterable].text.strip(), end='\n\n')


def translation():
    url = 'https://context.reverso.net/translation/' + languages[language_from] + '-' + languages[language_to] + '/' + word 
    make_request(url)


def select_language():
    global language_from, language_to, word
    print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
    language_to = input()
    print("Type the word you want to translate:")
    word = input()

    if language_to == "fr":
        language_from = "en"
    else:
        language_from = "fr"

    print('You chose "{}" as the leguage to translate "{}" to.'.format(language_to,
                                                                       word))


select_language()

translation()

# make_request('https://context.reverso.net/translation/english-french/cheese')