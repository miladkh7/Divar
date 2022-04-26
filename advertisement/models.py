from django.core.validators import FileExtensionValidator
from django.db import models

from account.models import User
from category.models import Category
from location.models import Location


class Advertisement(models.Model):
    """
    This class represents Advertisement model
    Each user can one or more advertisement to publish
    """
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='advertisements')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="advertisements")
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
    
    def __str__(self):
        return f"{self.title} > {self.location.city.name}"
    
    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = "Advertisements"


class Image(models.Model):
    """
    This class represents Image model
    Each advertisement has one or many images
    """
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='images')
    image_file = models.FileField(
                                    upload_to='images/advertisement',
                                    validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg'))]
    )


class Attribute(models.Model):
    name = models.CharField(max_length=50)


class AdvAttrValue(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='attributes')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attributes')
    value = models.CharField(max_length=50)


