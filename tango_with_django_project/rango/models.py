from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    # When we reference this object in the GUI / application, what will the String
    # representing the instance of a particular category model be set to? in this case, 
    # it will be the name property
    def __str__(self):
        return self.name

class Page(models.Model):

    # The category property of the Page model is a reference to the Category
    # 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Pages'


class UserProfile(models.Model):
    
    # Links User_profile to User model 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Implementing for the lulz.
    username = models.CharField(max_length=50, unique=True)

    #The additional attributes we want to associate with a user. 
    website = models.URLField(blank=True)

    # this makes and uploads to a folder in media called 'profile_images'
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username