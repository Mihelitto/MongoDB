from pymongo import MongoClient
from pymongo.collection import Collection
from environs import Env
import _data


def drop_db(client: MongoClient, db_name: str) -> None:
    client.drop_database(db_name)


def fill_sessions(collection: Collection, sessions: list) -> None:
    collection.insert_many(sessions)


def fill_accrual(collection: Collection, accruals: list) -> None:
    collection.insert_many(accruals)


def fill_payments(collection: Collection, payments: list) -> None:
    collection.insert_many(payments)


def main():
    env = Env()
    env.read_env()

    mongo_host = env.str('MONGO_HOST', default='localhost')
    mongo_port = env.int('MONGO_PORT', default=27017)
    mongo_password = env.str('MONGO_PASSWORD', default='')
    mongo_login = env.str('MONGO_LOGIN', default='')

    auth_credentials = ''
    if mongo_login and mongo_password:
        auth_credentials = f'{mongo_login}:{mongo_password}@'
    mongo_uri = f'mongodb://{auth_credentials}{mongo_host}:{mongo_port}'

    client = MongoClient(mongo_uri)
    drop_db(client, 'ClientsDB')
    db = client['ClientsDB']

    account = db['Account']
    accrual = db['Accrual']
    payment = db['Payment']
    fill_sessions(account, _data.sessions)
    fill_accrual(accrual, _data.accruals)
    fill_payments(payment, _data.payments)


if __name__ == '__main__':
    main()
