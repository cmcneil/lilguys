from django.db import models


class Lilguy(models.Models):
    """ A little guy ready for adventure. """

    # unique key code for editing the little guy
    code = models.CharField(max_length=22, unique=True)
    # the name of the little guy
    name = models.CharField(max_length=55)
    # the icon/avatar photo of the little guy
    pic = models.ImageField(upload_to="lilguybook", max_length=200)    
    # longitude and latitude positions of most recently logged location
    current_lon = models.FloatField()
    current_lat = models.FloatField()

