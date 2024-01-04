from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [
        ('short', 'Short Question'),
        ('long', 'Long Question'),
        ('numerical', 'Numerical Question'),
    ]

    sr_no = models.CharField(max_length=100)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='short')
    short_question = models.CharField(max_length=100, blank=True, null=True)
    long_question = models.TextField(blank=True, null=True)
    numerical_question = models.CharField(max_length=100, blank=True, null=True)
    marks = models.IntegerField()  # Change to IntegerField for whole number values
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.sr_no} - Type: {self.get_question_type_display()} - Marks: {self.marks} - Chapter: {self.chapter} - Subject: {self.subject}"
