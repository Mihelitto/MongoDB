from datetime import datetime


sessions = [
    {
        'number': '7800000000000',
        'name': 'Пользователь №1',
        'sessions': [
            {
                'created_at': datetime.fromisoformat('2016-01-01T00:00:00'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-01T01:20:01'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-01T01:21:13'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.fromisoformat('2016-01-01T01:33:59'),
                    }
                ],
            }
        ]
    },
    {
        'number': '7800000000001',
        'name': 'Пользователь №2',
        'sessions': [
            {
                'created_at': datetime.fromisoformat('2016-01-02T00:00:00'),
                'session_id': '6QBnQhFGgsdgfhgjjdaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-02T01:20:01'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-02T01:21:13'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.fromisoformat('2016-01-02T01:33:59'),
                    },
                    {
                        'type': 'update',
                        'created_at': datetime.fromisoformat('2016-01-02T01:45:59'),
                    }
                ],
            },
            {
                'created_at': datetime.fromisoformat('2016-01-10T00:00:00'),
                'session_id': '6QBnQhFGgsdgfhgjjdaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'create',
                        'created_at': datetime.fromisoformat('2016-01-10T01:33:59'),
                    },
                    {
                        'type': 'update',
                        'created_at': datetime.fromisoformat('2016-01-10T01:45:59'),
                    }
                ],
            }
        ]
    },
    {
        'number': '7800000000002',
        'name': 'Пользователь №3',
        'sessions': [
            {
                'created_at': datetime.fromisoformat('2016-01-03T00:00:00'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMdsgfhgjhjhjfhuooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-03T01:20:01'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-03T01:21:13'),
                    },
                    {
                        'type': 'update',
                        'created_at': datetime.fromisoformat('2016-01-03T01:23:50'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.fromisoformat('2016-01-03T01:33:59'),
                    }
                ],
            }
        ]
    },
    {
        'number': '7800000000003',
        'name': 'Пользователь №4',
        'sessions': [
            {
                'created_at': datetime.fromisoformat('2016-02-01T00:00:00'),
                'session_id': '6QBnQhFGgDdfghhghfgjfbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-02-01T01:20:01'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-02-01T01:21:13'),
                    },
                    {
                        'type': 'create',
                        'created_at': datetime.fromisoformat('2016-02-01T01:33:59'),
                    }
                ],
            }
        ]
    }
]


accruals = [
    {
        'date': datetime.fromisoformat('2016-02-01T01:33:59'),
        'month': datetime.fromisoformat('2016-02-01T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-03-01T01:33:59'),
        'month': datetime.fromisoformat('2016-03-01T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-04-03T01:33:59'),
        'month': datetime.fromisoformat('2016-04-03T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-05-05T01:33:59'),
        'month': datetime.fromisoformat('2016-05-05T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-06-07T01:33:59'),
        'month': datetime.fromisoformat('2016-06-07T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-07-10T01:33:59'),
        'month': datetime.fromisoformat('2016-07-10T01:33:59').month,
    }
]

payments = [
    {
        'date': datetime.fromisoformat('2016-04-06T01:33:59'),
        'month': datetime.fromisoformat('2016-04-06T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-05-10T01:33:59'),
        'month': datetime.fromisoformat('2016-05-10T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-07-01T01:33:59'),
        'month': datetime.fromisoformat('2016-07-01T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-01-01T01:33:59'),
        'month': datetime.fromisoformat('2016-01-01T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-08-01T01:33:59'),
        'month': datetime.fromisoformat('2016-08-01T01:33:59').month,
    },
    {
        'date': datetime.fromisoformat('2016-02-01T01:33:59'),
        'month': datetime.fromisoformat('2016-02-01T01:33:59').month,
    }
]
