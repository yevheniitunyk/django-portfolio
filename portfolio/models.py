from django.db import models

# Create your models here.

class PortfolioModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='portfolio/images')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
