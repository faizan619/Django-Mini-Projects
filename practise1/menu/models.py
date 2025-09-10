from django.db import models

# Create your models here.

class Menu(models.Model):
    # https://docs.djangoproject.com/en/5.2/topics/db/models/
    # https://docs.djangoproject.com/en/5.2/ref/templates/builtins/

    # servicesData = Services.objects.all().order_by("-services_icons")[:3]
    # serviceDetail = Services.objects.get(id=serviceid)    ## get specific Details with ID
    # for n in servicesData:
    #     print(n.services_icons)
