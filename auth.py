import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ssbc.settings")
from django.contrib.auth.models import User

user = User.objects.get(username='root')
if not user:
    user = User.objects.create_user(username='root', password='root', email='root@root.com')
else:
    user.set_password('root')
user.save()


