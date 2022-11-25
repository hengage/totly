from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.category_name}"
    
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)
    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    