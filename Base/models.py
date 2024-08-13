from django.db import models

# Create your models here.
class Uploadfile(models.Model):
    file=models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File uploaded on {self.uploaded_at}"