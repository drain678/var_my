from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name