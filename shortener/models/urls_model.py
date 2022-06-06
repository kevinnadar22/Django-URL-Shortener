import datetime
import secrets
import string
from django.db import models
from django.contrib.sites.models import Site
from django.urls import reverse

# Urls Models
def create_alias():
    alias = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                        for i in range(6))
    return alias

class Urls(models.Model):

    views = models.IntegerField(default=0, null=True, blank=True)

    id =  models.IntegerField(primary_key = True)

    long_url = models.CharField(max_length=2048)
        
    alias = models.URLField(
        max_length=6, 
        unique=True,
        editable=False,
        default= create_alias)

    is_hidden = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=datetime.datetime.now)


    def get_absolute_url(self):
        return reverse("home")
    
    def __str__(self) -> str:
        current_site = Site.objects.get_current()
        return self.alias
    
    class Meta:
        verbose_name_plural = "URLS"



