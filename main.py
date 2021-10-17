from pymongo import MongoClient
from environs import Env
import pprint
from mongodb_utils import aggregate_actions, match_payments


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
    db = client['ClientsDB']

    accounts = db['Account']
    accruals = db['Accrual']
    payments = db['Payment']

    pprint.pprint(aggregate_actions(accounts))
    matched_payments, unmatched_payments = match_payments(accruals, payments)
    pprint.pprint(matched_payments)
    pprint.pprint(unmatched_payments)


if __name__ == '__main__':
    main()
