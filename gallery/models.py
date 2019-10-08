from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
class Category(models.Model):
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
 
class Image(models.Model):
    image = models.ImageField(blank=True)
    image_name = models.CharField(max_length=200, blank=True)
    image_description = models.TextField(max_length=400, blank=True)
    image_link = models.CharField(max_length=200, blank=True)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    
    
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
    
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

