import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Stock, Sale, Shop

DSN = 'postgresql://postgres:DilanOBrayen69@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
title1 = Book(title='Капитанская дочка', publisher=publisher1)
title2 = Book(title='Руслан и Людмила', publisher=publisher1)
title3 = Book(title='Евгений Онегин', publisher=publisher1)
name1 = Shop(name='Буквоед')
name2 = Shop(name='Лабиринт')
name3 = Shop(name='Книжный дом')
stock1 = Stock(book=title1, shop=name1)
stock2 = Stock(book=title2, shop=name1)
stock3 = Stock(book=title1, shop=name2)
stock4 = Stock(book=title3, shop=name3)
sale1 = Sale(data_sale='09-11-2022', price='600', stock=stock1)
sale2 = Sale(data_sale='08-11-2022', price='500', stock=stock2)
sale3 = Sale(data_sale='05-11-2022', price='580', stock=stock3)
sale4 = Sale(data_sale='02-11-2022', price='490', stock=stock4)
sale5 = Sale(data_sale='26-10-2022', price='600', stock=stock1)


session.add_all([publisher1, title1, title2, title3, sale1, sale2, sale3, sale4, sale5, name1, name2, name3, stock1, stock2, stock3, stock4])
session.commit()
# x = str(input('Введите имя издателя: '))
# if x == 'Пушкин':
#     subq = session.query(Stock).subquery()
#     q = session.query(Book).join(subq, Book.id == subq.c.id_book).join(Sale.stock)
#     print(q)
#     for s in q.all():
#         print(s.id, s.title)
        # for el in s.stocks:
        #     print("\t", el.id, el.id_book)
        # subq = session.query(Sale).subquery()
        # q = session.query(Stock).join(subq, Stock.id == subq.c.id_stock)
        # print(q)
        # for s1 in q.all():
        #     print(s1.id, s1.id_book)
        #     for el in s1.id_book:
        #         print("\t", el.id, el.price, el.data_sale)

q = session.query(Shop).join(Stock.shop)
print(q)
for s in q.all():
    print(s.id, s.name)
    for hw in s.stocks1:
        print("\t", hw.id_book)

# subq = session.query(Book).subquery()
# q = session.query(Publisher).join(subq, Publisher.id == subq.c.id_publisher)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.books:
#         print("\t", hw.id, hw.title)
#
# subq = session.query(Sale).subquery()
# q = session.query(Stock).join(subq, Stock.id == subq.c.id_stock)
# for s in q.all():
#     # print(s.id)
#     for hw in s.sales:
#         print("\t", hw.data_sale, hw.price, hw.id_stock)
#
# subq = session.query(Stock).subquery()
# q = session.query(Shop).join(subq, Shop.id == subq.c.id_shop)
# for s in q.all():
#     # print(s.id)
#     for hw in s.stocks1:
#         print("\t", hw.id_shop)

# if __name__ == "__main__":
    # print(f'{publisher1}\n, {title1}\n, {title2}\n, {title3}\n, {sale1},\n {sale2},\n {sale3},\n {sale4},\n {sale5},\n {name1},\n {name3},\n {name2},\n {stock1},\n {stock2},\n {stock3},\n {stock4}')
