from django.db import models
# Create your models here.

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

    def __unicode__(self):
        return ("Lilguy: " + self.name + " (" + self.code + 
                "), currently located at (" + str(self.current_lon) + 
                ", " + str(self.current_lat) + ") " )

class Chapter(models.Model):
    """Describes a user-created chapter in a Lilguy's life."""
    # The Lilguy that this chapter is about.
    lilguy = models.ForeignKey(Lilguy)
    # The (optional) title of the story. We default to a date?
    title = models.CharField(max_length=80)
    # The story text.
    story_text = models.TextField()
    # The longitude at which the guy was found.
    found_at_lon = models.FloatField()
    # The latitude at which the guy was found
    found_at_lat = models.FloatField()
    # The longitude that the person plans to drop the guy near.
    dropped_at_lon = models.FloatField()
    # The latitude that the person plans to drop the guy near.
    dropped_at_lat = models.FloatField()
    # The author can include a picture of the guy.
    picture = models.ImageField(upload_to='adventures', max_length=200)
    
    def __unicode__(self):
        return (self.__class__.__name__ + 
                "(title=" + title + 
                "lilguy.name=" + lilguy.name
                ", story_text=" + story_text +
                ", found_at_lon=" + str(found_at_lon) +
                ", found_at_lat=" + str(found_at_lat) +
                ", dropped_at_lon=" + str(dropped_at_lon) +
                ", dropped_at_lat=" + str(dropped_at_lat))
