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


def web_service_connect(url):
    user_agent = 'Mozilla/5.0'
    page = requests.get(url, headers={'User-Agent': user_agent})
    # code_check(page.status_code)
    return BeautifulSoup(page.content, 'html.parser')


def get_price(url):
    data = web_service_connect(url).find_all(
        'script', {"type": "application/ld+json"})[1].extract()
    data_str = [x for x in data]
    return int(data_str[0].split('"')[-12])


def add_advert(new_url):
    sesion.add(Table(url=new_url, price=get_price(new_url)))
    sesion.commit()
    print("New URL has been added!")


def check_adverts():
    any_changes = False

    rows = sesion.query(Table).all()

    if len(rows) > 0:
        for row in rows:
            now_price = get_price(row.url)
            if row.price != now_price:
                print("Cambio de precio en anuncio: " + row.url +
                      " before: " + str(row.price) + " now: " + str(now_price))
                row.previous_price = row.price
                row.price = now_price
                sesion.commit()
                any_changes = True

    if any_changes == False:
        print("Nothing to do here..")


def new_advert():
    new_url = input("Ad address: \n")
    add_advert(new_url)


def list_adverts():

    rows = sesion.query(Table).all()

    print(
        "\n --- Adverts ---- \n\t[Id, URL, Current price, Previous price] \n")

    if len(rows) > 0:
        for row in rows:
            print(" " + str(row.id) + "\t" + row.url + "\t" +
                  str(row.price) + "\t" + str(row.previous_price))

    else:
        print("No ads here..")


def menu():
    while(True):
        print("\n\t | Menu options:            | \n \
        |    1.-Add a new advert   |\n \
        |    2.-Check for changes  |\n \
        |    3.-List all adverts   |\n \
        |    0.-Exit               |\n")

        option = input('Your option -> ')

        if option == '1':
            new_advert()
        elif option == '2':
            check_adverts()
        elif option == '3':
            list_adverts()
        elif option == '0':
            exit()
        else:
            print("\n You failed, stupid!")


# add ad name

# better output

# control deleted ad

# control ad without price

# and so much more magic

# check a big price drop

# graphic interface

menu()
