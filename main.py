from pymongo import MongoClient
from pymongo.collection import Collection
from environs import Env
import pprint


def aggregate_actions(account: Collection) -> list:
    aggregation_pipeline = [
        {
            '$project': {
                'number': 1,
                'type': '$sessions.actions.type',
                'action': '$sessions.actions',
            }
        },
        {'$unwind': '$action'},
        {'$unwind': '$action'},
        {'$sort': {'action.created_at': 1}},
        {
            '$group': {
                '_id': {'number': '$number', 'type': '$action.type'},
                'count': {'$sum': 1},
                'last': {'$last': '$action'},
            }
        },
        {
            '$project': {
                '_id': 0,
                'number': '$_id.number',
                'actions': {
                    'type': '$last.type',
                    'last': {'created_at': '$last.created_at'},
                    'count': '$count',
                }
            }
        },
        {
            '$group': {
                '_id': {'number': '$number'},
                'actions': {'$push': '$actions'}
            }
        },
        {'$sort': {'_id.number': 1}},
    ]

    aggregated_actions = account.aggregate(aggregation_pipeline)
    action_types = ['create', 'update', 'read', 'delete']

    result = []
    for account in aggregated_actions:
        actions = account['actions']
        exists_action_types = [action['type'] for action in actions]
        for action_type in action_types:
            if action_type not in exists_action_types:
                actions.append({'type': action_type, 'last': None, 'count': 0})
        result_account = {account['_id']['number']: {'actions': actions}}
        result.append(result_account)

    return result


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

    pprint.pprint(aggregate_actions(accounts))


if __name__ == '__main__':
    main()
