from django.db import models

# Create your models here.


class Articles(models.Model):
    article_title = models.CharField(max_length=200)
    article_content = models.CharField(default=1000)
    article_date = models.DateTimeField("Дата публткации")

    def __str__(self):
        return self.article_title
