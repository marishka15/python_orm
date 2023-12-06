import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    # homeworks = relationship("Homework", back_populates="course")

    def __str__(self):
        return f'Publisher {self.id}:{self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=True)

    # course = relationship(Course, back_populates="homeworks")
    publisher = relationship(Publisher, backref="books")

    def __str__(self):
        return f'Book {self.id}: ({self.title}:{self.id_publisher})'

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    # homeworks = relationship("Homework", back_populates="course")

    def __str__(self):
        return f'Shop {self.id}:{self.name}'
class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="stocks1")


    def __str__(self):
        return f'Stock {self.id}:{self.id_book}:{self.id_shop}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    data_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=True)
    count = sq.Column(sq.Integer, nullable=True)
    stock = relationship(Stock, backref="sales")

    def __str__(self):
        return f'Sale {self.id}:{self.data_sale}:{self.price}:{self.id_stock}'



def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)