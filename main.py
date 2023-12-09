import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Stock, Sale, Shop

DSN = 'postgresql://postgres:DilanOBrayen69@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
publisher2 = Publisher(name='Толстой')
title1 = Book(title='Капитанская дочка', publisher=publisher1)
title2 = Book(title='Руслан и Людмила', publisher=publisher1)
title3 = Book(title='Евгений Онегин', publisher=publisher1)
title4 = Book(title='Анна Каренина', publisher=publisher2)
title5 = Book(title='Война и мир', publisher=publisher2)
title6 = Book(title='Детство', publisher=publisher2)
name1 = Shop(name='Буквоед')
name2 = Shop(name='Лабиринт')
name3 = Shop(name='Книжный дом')
stock1 = Stock(book=title1, shop=name1)
stock2 = Stock(book=title2, shop=name1)
stock3 = Stock(book=title1, shop=name2)
stock4 = Stock(book=title3, shop=name3)
stock5 = Stock(book=title6, shop=name1)
stock6 = Stock(book=title4, shop=name3)
stock7 = Stock(book=title5, shop=name2)
sale1 = Sale(data_sale='09-11-2022', price='600', stock=stock1)
sale2 = Sale(data_sale='08-11-2022', price='500', stock=stock2)
sale3 = Sale(data_sale='05-11-2022', price='580', stock=stock3)
sale4 = Sale(data_sale='02-11-2022', price='490', stock=stock4)
sale5 = Sale(data_sale='26-10-2022', price='600', stock=stock1)
sale6 = Sale(data_sale='15-11-2022', price='650', stock=stock5)
sale7 = Sale(data_sale='25-10-2022', price='480', stock=stock6)
sale8 = Sale(data_sale='20-11-2022', price='510', stock=stock7)


session.add_all([publisher1, publisher2, title1, title2, title3, title4, title5, title6, sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, name1, name2, name3, stock1, stock2, stock3, stock4, stock5, stock6, stock7])
session.commit()

def getshops(data):
    subq = session.query(Book.title, Shop.name, Sale.price, Sale.data_sale).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    if data.isdigit():
        q = subq.filter(Publisher.id == data).all()
    else:
        q = subq.filter(Publisher.name == data).all()

    for title, name, sale, data_sale in q:
            print(f"{title:<30} | {name:<12} | {sale:<8} | {data_sale:'%d-%m-%Y'}")


if __name__ == "__main__":
    data = input('Введите имя или id издателя: ')
    getshops(data)
    session.close()
