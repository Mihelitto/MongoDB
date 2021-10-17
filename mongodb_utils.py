from pymongo.collection import Collection


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


def match_payments(accrual: Collection, payment: Collection) -> tuple:
    lookup_pipeline = [
        {
            '$match': {
                '$expr': {
                    '$and': [
                        {'$lte': ['$date', '$$pay_date']}
                    ]
                }
            }
        },
        {'$sort': {'date': 1}},
    ]

    aggregation_pipeline = [
        {
            '$lookup': {
                'from': 'Accrual',
                'let': {'pay_month': '$month', 'pay_date': '$date'},
                'pipeline': lookup_pipeline,
                'as': 'accruals'
            }
        },
        {'$sort': {'date': 1}},
    ]

    all_accruals = list(accrual.find())
    payments = payment.aggregate(pipeline=aggregation_pipeline)

    free_payments = []
    matched_payments = []

    for payment in payments:
        pay_accruals = payment.pop('accruals', None)
        if pay_accruals:
            last_accrual = pay_accruals[-1]
            if last_accrual['month'] == payment['month']:
                matched_payments.append([payment, last_accrual])
                all_accruals.remove(last_accrual)
                continue
            else:
                for accrual in pay_accruals:
                    if accrual in all_accruals:
                        matched_payments.append([payment, accrual])
                        all_accruals.remove(accrual)
                        break
        free_payments.append(payment)

    return matched_payments, free_payments
