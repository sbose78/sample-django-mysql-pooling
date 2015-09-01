APP_DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.mysqlpool',  django_mysqlpool.backends.mysqlpool'
	'ENGINE': 'django_mysqlpool.backends.mysqlpool',
        'NAME': 'greenopia',
        'USER': 'greenopia',
        'PASSWORD': 'greenopia',
        'HOST': 'greenopiadb.chb8tkhm9yy6.us-west-2.rds.amazonaws.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
	'CONN_MAX_AGE' : None 
    }
}
