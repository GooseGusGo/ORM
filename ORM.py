import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

class Database:

    def import_data_from_json(self):
        with open('data.json', 'r') as fd:
            data = json.load(fd)
        for record in data:
            model = {'publisher': Publisher, 'shop': Shop, 'book': Book, 'stock': Stock, 'sale': Sale,}[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()

    def get_publisher(self):
        get_query = input("Введите имя или id издателя: >")
        res = session.query(Publisher).filter(Publisher.id == get_query or Publisher.name == get_query)
        for i in res.all():
            print(f'id: {i.id} Имя: {i.name}')


if __name__ == '__main__':

    DSN = "postgresql://postgres:postgres@localhost:5432/netology_db"
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    db = Database()
    db.import_data_from_json()
    db.get_publisher()
