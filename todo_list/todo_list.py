from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

from sqlalchemy.orm import sessionmaker

# Crate database file
engine = create_engine('sqlite:///todo.db?check_same_thread=False') 
    # check_same_thread=False for test purpose

Base = declarative_base()

class Table(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())
    
    def __repr__(self):
        return self.string_field
    
#Base.metadata.create_all(engine)
Table.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()



def add_task():
    session.add(Table(task=input("Enter task\n")))
    session.commit()
    print("The task has been added!")

def print_today_task():
    print("Today:")
    rows = session.query(Table).all()
    num_task = 1
    if len(rows) > 0:
        for row in rows:
            print(str(num_task) + ". " + row.task)
            num_task += 1
    else:
        print("Nothing to do!")

# menu 
while(1):
    menu_option = input("1) Today's tasks\n2) Add task\n0) Exit\n")
    print()

    if menu_option == '1':
        print_today_task()
    elif menu_option == '2':
        add_task()
    elif menu_option == '0':
        exit()

    print()