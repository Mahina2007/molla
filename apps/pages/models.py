# from django.db import models
#
# class ContactModel(models.Model):
#     full_name = models.CharField(max_length=128)
#     email = models.EmailField()
#     phone_number = models.CharField(
#         max_length=15, null=True, blank=True
#     )
#     subject = models.CharField(
#         max_length=255, null=True, blank=True
#     )
#     message = models.TextField()
#
#     is_read =  models.BooleanField(default=False)
#     comment = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.full_name} - {self.email}"
#
#     class Meta:
#         verbose_name = 'contact'
#         verbose_name_plural = 'contacts'
#
# class Author(models.Model):
#     """Author model representing book authors"""
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     birth_date = models.DateField()
#     country = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     joined_date = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['name']),
#             models.Index(fields=['country', 'is_active']),
#         ]
#
#     def __str__(self):
#         return self.name
#
#
# class Publisher(models.Model):
#     """Publisher model for book publishers"""
#     name = models.CharField(max_length=100)
#     founded_year = models.IntegerField()
#     website = models.URLField()
#
#     def __str__(self):
#         return self.name
#
#
# class Book(models.Model):
#     """Book model representing published books"""
#     GENRE_CHOICES = [
#         ('FIC', 'Fiction'),
#         ('NON', 'Non-Fiction'),
#         ('SCI', 'Science'),
#         ('HIS', 'History'),
#         ('BIO', 'Biography'),
#     ]
#
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
#     genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
#     publish_date = models.DateField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     page_count = models.IntegerField()
#     is_available = models.BooleanField(default=True)
#     rating = models.FloatField(null=True, blank=True)
#
#     class Meta:
#         ordering = ['-publish_date', 'title']
#         unique_together = ['title', 'author']
#
#     def __str__(self):
#         return f"{self.title} by {self.author.name}"
#
#
# class Review(models.Model):
#     """Review model for book reviews"""
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
#     reviewer_name = models.CharField(max_length=100)
#     content = models.TextField()
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return f"{self.rating} star review for {self.book.title}"

from django.db import models
from django.utils import timezone

# ========= MODELLAR =========

class Department(models.Model):
    """Kafedra"""
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    """O'qituvchi"""
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="instructors")
    hire_date = models.DateField()

    class Meta:
        ordering = ["full_name"]
        indexes = [models.Index(fields=["department"])]

    def __str__(self):
        return self.full_name

class Student(models.Model):
    """Talaba"""
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    year_of_study = models.PositiveSmallIntegerField()  # 1-4
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name

class Course(models.Model):
    """Fan"""
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=160)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="courses")
    credits = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"

class Prerequisite(models.Model):
    """Fan uchun old shart (prereq)"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prereqs_for")
    prerequisite = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="is_prereq_of")

    class Meta:
        unique_together = [("course", "prerequisite")]

class Term(models.Model):
    """OвЂquv davri (yil+semestr)"""
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=16,
                                choices=[("SPRING", "SPRING"), ("FALL", "FALL"), ("SUMMER", "SUMMER")])

    class Meta:
        unique_together = [("year", "semester")]

    def __str__(self):
        return f"{self.year} {self.semester}"

class Section(models.Model):
    """Fan kesimidagi guruh (section)"""
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="sections")
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name="sections")
    term = models.ForeignKey(Term, on_delete=models.PROTECT, related_name="sections")
    capacity = models.PositiveIntegerField(default=30)

    class Meta:
        unique_together = [("course", "instructor", "term")]
        indexes = [models.Index(fields=["term"])]

    def __str__(self):
        return f"{self.course.code} - {self.term}"

class Enrollment(models.Model):
    """Talabaning section ga yozilishi"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="enrollments")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(default=timezone.now)
    grade = models.CharField(
        max_length=2, null=True, blank=True,
        choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("F", "F")]
    )

    class Meta:
        unique_together = [("section", "student")]
        indexes = [models.Index(fields=["student", "section"])]

    def __str__(self):
        return f"{self.student} -> {self.section}"

class Exam(models.Model):
    """Imtihon (midterm/final)"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="exams")
    kind = models.CharField(max_length=10, choices=[("MID", "MID"), ("FIN", "FIN"), ("QUIZ", "QUIZ")])
    date = models.DateField()
    max_score = models.PositiveIntegerField(default=100)

    class Meta:
        unique_together = [("section", "kind")]

class ExamResult(models.Model):
    """Imtihon natijasi"""
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="results")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exam_results")
    score = models.FloatField()

    class Meta:
        unique_together = [("exam", "student")]
        indexes = [models.Index(fields=["student"])]
