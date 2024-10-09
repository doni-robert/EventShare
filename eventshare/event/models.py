from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    """ Model representing a category """
    name = models.CharField(max_length=100, unique=True, help_text="Enter a category")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='category_name_case_insensitive_unique',
                violation_error_message = "Category already exists (case insensitive match)"
            ),
        ]

class Event(models.Model):
    """ Model representing an event"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)
    organizer = models.ForeignKey("User", on_delete=models.RESTRICT)
    attendees = models.ManyToManyField("User", related_name="attending_events", blank=True)
    category = models.ManyToManyField(Category, help_text="Select a category for this event")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this event."""
        return reverse('book-detail', args=[str(self.id)])

class User(AbstractUser):
    """ Model representing a user """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        """Returns the URL to access a particular user instance."""
        return reverse('user-detail', args=[str(self.id)])

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
