from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="photo",blank=True,null=True)
    
    
    def __str__(self):
        return self.name
class Product(models.Model):
      name=models.CharField(max_length=50)
      slug=models.SlugField(unique=True)
      image=models.ImageField(upload_to="photos",blank=True,null=True)
      description=models.TextField(blank=True,null=True)
      Category=models.ForeignKey(Category,on_delete=models.PROTECT)
      price=models.FloatField()
      stock=models.IntegerField(blank=True,null=True)
      def __str__(self):
          return self.name
      
