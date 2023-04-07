from django.db import models
from django.urls import reverse

# Create your models here.


class BlogPostModel(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # пишем через blog:, потому что в юрлах мы указали, что имя нашего приложения blog. Тем самым, через blog: мы указываем, что ссылку надо искать именно в юрлах приложения blog. Тем самым избежим ошибки, если в разных приложениях будут ссылки с одинаковыми именами. Так же можно юзать и в {% url 'blog:details' blog.pk %}
        return reverse('blog:details', args=[self.pk,])