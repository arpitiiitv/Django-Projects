manage.py startapp shop
manage.py startapp blog
manage.py runserver

read documentation Models / reference field model
manage.py migrate
manage.py makemigrations
manage.py migrate

####################
#admin panel
python manage.py createsuperuser

open shop admin
from .models import Product
admin.site.register(Product)

## to set image from static file
<img src={%static "blog/arpit.jpg" %} alt="Cameraman" width="500" height="600">