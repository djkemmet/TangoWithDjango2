from django.db import models

# Create your models here.

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

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