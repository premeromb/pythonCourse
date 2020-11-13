from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker

# Crate database file
engine = create_engine('sqlite:///todo.db?check_same_thread=False') # ./todo.db for tests
    # check_same_thread=False for test purpose

Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
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
    task_input = input("Enter task\n")
    deadline_input = input("Enter deadline\n").split("-")


    session.add(Table(task=task_input, deadline=datetime(int(deadline_input[0]), int(deadline_input[1]), int(deadline_input[2])).date()))
    session.commit()
    print("The task has been added!")


def today_tasks():
    print("Today {}:".format(datetime.today().strftime("%d %b")))
    rows = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
    num_task = 1
    if len(rows) > 0:
        for row in rows:
            print(str(num_task) + ". " + row.task + row.deadline.strftime(". %-d %b"))
            num_task += 1
    else:
        print("Nothing to do!")

def weeks_tasks():
    day_time = datetime.today()
    for day in range(7):
    
        print(format(day_time.strftime("%A %d %b:")))
        rows = session.query(Table).filter(Table.deadline == day_time.date()).all()
        num_task = 1
        if len(rows) > 0:
            for row in rows:
                print(str(num_task) + ". " + row.task)
                num_task += 1
        else:
            print("Nothing to do!")
        if day < 6: 
            print()
        day_time += timedelta(days=1)



def all_tasks():
    print("All tasks:")
    rows = session.query(Table).order_by(Table.deadline).all()
    num_task = 1
    if len(rows) > 0:
        for row in rows:
            print(str(num_task) + ". " + row.task + row.deadline.strftime(". %-d %b"))
            num_task += 1
    else:
        print("Nothing to do!")


# menu 
while(1):
    menu_option = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit\n")
    print()

    if menu_option == '1':
        today_tasks()
    elif menu_option == '2':
        weeks_tasks()
    elif menu_option == '3':
        all_tasks()
    elif menu_option == '4':
        add_task()
    elif menu_option == '0':
        break
    print()
    
print("Bye!")
   