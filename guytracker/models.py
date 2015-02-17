from django.db import models
# Create your models here.

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

