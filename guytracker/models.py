from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image
import StringIO

class Lilguy(models.Model):
    """ A little guy ready for adventure. """

    # the name of the little guy
    name = models.CharField(max_length=55)
    # the icon/avatar photo of the little guy
    pic = models.ImageField(upload_to="lilguybook", max_length=200)    
    # the icon/avatar shrunk to 180px width.
    pic_180 = models.ImageField(upload_to="lilguybook/180", max_length=200, null=True, blank=True)
    # longitude and latitude positions of most recently logged location
    current_lon = models.FloatField()
    current_lat = models.FloatField()
    # Timestamp
    timestamp = models.DateTimeField(auto_now_add=True)
     
    def save(self, *args, **kwargs):
        """Override save to resize pic field."""
        if self.pic:
            EXTRA_IMAGE_SIZES = {'pic_180': (180, 270)}
            MAX_SIZE = (1280, 1280)
            imgFile = Image.open(StringIO.StringIO(self.pic.read()))
            #Convert to RGB
            if imgFile.mode not in ('L', 'RGB'):
                imgFile = imgFile.convert('RGB')
            for field_name, size in EXTRA_IMAGE_SIZES.iteritems():
                field = getattr(self, field_name)
                working = imgFile.copy()
                working.thumbnail(size, Image.ANTIALIAS)
                fp = StringIO.StringIO()
                working.save(fp, format="JPEG", quality=95)
                cf = ContentFile(fp.getvalue())
                field.save(name=self.pic.name, content=cf, save=False)
            imgFile.thumbnail(MAX_SIZE, Image.ANTIALIAS)
            output = StringIO.StringIO()
            imgFile.save(output, format="JPEG", quality=95)
            output.seek(0)
            self.pic = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.pic.name.split('.')[0], 'image/jpeg', output.len, None)
        
        super(Lilguy, self).save(*args, **kwargs)

    def __unicode__(self):
        return ("Lilguy: " + self.name + 
                ", "
                "currently located at (" + 
                str(self.current_lon) + ", " + 
                str(self.current_lat) + ") " )


class Chapter(models.Model):
    """Describes a user-created chapter in a Lilguy's life."""
    # The Lilguy that this chapter is about.
    lilguy = models.ForeignKey(Lilguy)
    # The (optional) title of the story. We default to a date?
    title = models.CharField(max_length=80, null=True, blank=True)
    # The story text.
    story_text = models.TextField()
    # The longitude at which the guy was found.
    found_at_lon = models.FloatField()
    # The latitude at which the guy was found
    found_at_lat = models.FloatField()
    # The longitude that the person plans to drop the guy near.
    dropped_at_lon = models.FloatField(null=True, blank=True)
    # The latitude that the person plans to drop the guy near.
    dropped_at_lat = models.FloatField(null=True, blank=True)
    # The author can include a picture of the guy.
    picture = models.ImageField(upload_to='adventures', max_length=200, null=True, blank=True)
    # Thumbs for the picture. Used on the site.
    picture_600 = models.ImageField(upload_to='adventures/600', 
                                    max_length=200, 
                                    null=True, 
                                    blank=True)
    # Timestamp
    timestamp = models.DateTimeField(auto_now_add=True)
    # Submiter's email(if subscribed)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        """Override save to resize picture field."""
        if self.picture:
            EXTRA_IMAGE_SIZES = {'picture_600': (600, 900)}
            MAX_SIZE = (1280, 1280)
            imgFile = Image.open(StringIO.StringIO(self.picture.read()))
            #Convert to RGB
            if imgFile.mode not in ('L', 'RGB'):
                imgFile = imgFile.convert('RGB')
            for field_name, size in EXTRA_IMAGE_SIZES.iteritems():
                field = getattr(self, field_name)
                working = imgFile.copy()
                working.thumbnail(size, Image.ANTIALIAS)
                fp = StringIO.StringIO()
                working.save(fp, format="JPEG", quality=95)
                cf = ContentFile(fp.getvalue())
                field.save(name=self.picture.name, content=cf, save=False)
            imgFile.thumbnail(MAX_SIZE, Image.ANTIALIAS)
            output = StringIO.StringIO()
            imgFile.save(output, format="JPEG", quality=95)
            output.seek(0)
            self.picture = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.picture.name.split('.')[0], 'image/jpeg', output.len, None)

        super(Chapter, self).save(*args, **kwargs)

    def __unicode__(self):
        return ("Chapter(title=" + self.title + 
                "lilguy.name=" + self.lilguy.name +
                ", story_text=" + self.story_text +
                ", found_at_lon=" + str(self.found_at_lon) +
                ", found_at_lat=" + str(self.found_at_lat) +
                ", dropped_at_lon=" + str(self.dropped_at_lon) +
                ", dropped_at_lat=" + str(self.dropped_at_lat))
