from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    detail = models.CharField(max_length=800, null=True)
    tagline = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.summary
