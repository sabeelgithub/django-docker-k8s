from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150,unique=True)
    created_at = models.DateField(auto_now=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
         return self.category_name
    
class Sub_Category(models.Model):
  sub_category_name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50,unique=True)
  category= models.ForeignKey(Category,on_delete=models.CASCADE)
  created_at = models.DateField(auto_now=True)
  modified_at = models.DateField(auto_now=True)
 
  def __str__(self):
        return self.sub_category_name
  
class Students(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
  created_at = models.DateField(auto_now=True)
  modified_at = models.DateField(auto_now=True)
 
  def __str__(self):
        return self.name
