from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    biography = models.TextField(blank=True)

    date_of_birth = models.DateField(null=True, blank=True)

    country = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Publisher(models.Model):

    name = models.CharField(max_length=255)

    website = models.URLField(blank=True)

    email = models.EmailField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Book(models.Model):

    title = models.CharField(max_length=255)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name="books"
    )

    categories = models.ManyToManyField(
        Category,
        related_name="books"
    )

    description = models.TextField()

    isbn = models.CharField(
        max_length=13,
        unique=True,
        
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock_quantity = models.PositiveIntegerField(default=0)

    published_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
