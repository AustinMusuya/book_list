from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

isbn_validator = RegexValidator(
    regex=r'^\d{10}|\d{13}$',
    message="ISBN must be exactly 10 or 13 digits."
)
def publication_date_validator(value):
    if value > date.today():
        raise ValidationError("Publication date must be in the past.")


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateField(validators=[publication_date_validator])
    isbn = models.CharField(unique=True, max_length=13, validators=[isbn_validator])

    def __str__(self):
        return f"{self.title} By {self.author}"
