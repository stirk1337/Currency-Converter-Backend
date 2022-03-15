import views

routes = [
    ('GET', '/ping', views.pong),
    ('GET', '/convert', views.convert),
    ('POST', '/database', views.update),
]