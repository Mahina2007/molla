from django.db import models


class Author(models.Model):
    """Author model representing book authors"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    country = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['country', 'is_active']),
        ]

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """Publisher model for book publishers"""
    name = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book model representing published books"""
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('SCI', 'Science'),
        ('HIS', 'History'),
        ('BIO', 'Biography'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    page_count = models.IntegerField()
    is_available = models.BooleanField(default=True)
    rating = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-publish_date', 'title']
        unique_together = ['title', 'author']

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Review(models.Model):
    """Review model for book reviews"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.rating} star review for {self.book.title}"
