from users.models import User
from django.db import models

SHORT_TEXT_LEN = 200
# Create your models here
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='static/articles_image', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else: return self.text

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name