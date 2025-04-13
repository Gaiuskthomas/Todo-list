from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=30,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

