DEBUG = False
SECRET_KEY = 'h5f-7@dl)r)qpd3^gnu=p)7p$i*zeahqk0@gh90xq9c40vu0(#'
ALLOWED_HOSTS = ['*'] # set this to your real host in production!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webapp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '',
    }
}
STATIC_ROOT = '/webapp/static'
MEDIA_ROOT = '/webapp/media'
