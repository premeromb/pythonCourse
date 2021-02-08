import requests

from bs4 import BeautifulSoup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///adverts_price.db')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'adverts'
    id = Column(Integer, primary_key=True)
    name = Column(String, default="None")
    url = Column(String)
    price = Column(Integer, default=0)
    previous_price = Column(Integer, default=0)

    def __repr__(self):
        return self.string_field


Table.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sesion = Session()

## WEB ###

def web_service_connect(url):
    user_agent = 'Mozilla/5.0'
    page = requests.get(url, headers={'User-Agent': user_agent})
    return BeautifulSoup(page.content, 'html.parser')


def get_page_data(url):
    data = web_service_connect(url).find_all(
        'script', {"type": "application/ld+json"})[1].extract()
    data_str = [x for x in data]
    formated = (data_str[0].split('"'))
    return [formated[11], formated[-12]]    # [ name, price ]

## BD ##

def is_advert_exists(url):
    rows = sesion.query(Table).filter(Table.url == str(url)).all()
    if rows:
        return True
    return False

def add_advert(new_url):
    try:
        if not is_advert_exists(new_url):
            name_ad, price_ad = get_page_data(new_url)
            sesion.add(Table(name=name_ad, url=new_url, price=price_ad))
            sesion.commit()
            print("\n" + name_ad + " has been added!")
        else:
            print("\nERROR: This url has already been added")

    except:
        print("\n ERROR: URL not valid")

def drop_advert(id_drop):
    sesion.query(Table).filter(Table.id == id_drop).delete()
    sesion.commit()

def get_all_adverts():
    return sesion.query(Table).all()


## FUNCTIONS ##

def check_adverts():
    any_changes = False

    rows = sesion.query(Table).all()

    if rows:
        for row in rows:
            now_name, now_price = get_page_data(row.url)
            if row.price != int(now_price):
                print("Cambio de precio en anuncio: " + now_name + " con URL: " + row.url +
                      " before: " + str(row.price) + " now: " + str(now_price))
                row.name = now_name
                row.previous_price = row.price
                row.price = now_price
                sesion.commit()
                any_changes = True

        if any_changes == False:
            print("\nNo ad changed its price..")
    else:
        print("No ads to check..")


def new_advert():
    new_url = input("\nAd address: \n")
    add_advert(new_url)

def multiple_new_adverts():
    print("Multiple adverts add mode, write 'exit' to exit")
    while(True):
        income = input("\nAd address: \n")
        if income == 'exit':
            break
        else:
            add_advert(income)

def list_adverts():
    rows = get_all_adverts()
    print(
        "\n --- Adverts ---- \n\t[Id, Name, URL, Current price, Previous price] \n")

    if rows:
        for row in rows:
            print(" " + str(row.id) + "\t" + row.name + "\t" + row.url + "\t" +
                  str(row.price) + "\t" + str(row.previous_price))
    else:
        print("No ads here..")


def delete_advert():
    print("Saved adverts:")
    list_adverts()
    advert_id = input("\nWhat advert do you like to delete? \nEnter Id: ")
    drop_advert(advert_id)


def menu():
    while(True):
        print("\n\t | Menu options:               | \n \
        |    1.-Add a new advert      |\n \
        |    2.-Add multiple new ads  |\n \
        |    3.-Check for changes     |\n \
        |    4.-List all adverts      |\n \
        |    5.-Delete advert         |\n \
        |    0.-Exit                  |\n")

        option = input('Your option -> ')

        if option == '1':
            new_advert()
        elif option == '2':
            multiple_new_adverts()
        elif option == '3':
            check_adverts()
        elif option == '4':
            list_adverts()
        elif option == '5':
            delete_advert()
        elif option == '0':
            exit()
        else:
            print("\n You failed, stupid!")


# check for old ad (update ad date)

# control deleted ads

# control ad without price

# and so much more magic

# check a big price drop

# graphic interface

menu()

