import src.views

routes = [
    ('GET', '/convert', src.views.convert),
    ('POST', '/database', src.views.update_currency),
]