django-hashcash
===============

This project implements http://hashcash.io into the normal Django login form.
This is useful in that it may thwart brute force attacks on the login form.


Installation
------------

````
# settings.py

...

#
# Install django_hashcash into INSTALLED_APPS
#
INSTALLED_APPS += (
    'django_hashcash',
)

...

#
# Add details you got from https://hashcash.io/
#
HASHCASHIO_PUBLIC_KEY = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
HASHCASHIO_PRIVATE_KEY = 'PRIVATE-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
...
````

````
# urls.py

...
from django_hashcash.forms import HashCashAuthenticationForm

...

admin.autodiscover()
admin.site.login_template = 'django_hashcash/login.html'
admin.site.login_form = HashCashAuthenticationForm
...
````

Done!