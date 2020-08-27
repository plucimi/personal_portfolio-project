from django.db import models

class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    post_date = models.DateField()
    post_description = models.TextField()

    def __str__(self):
        return self.title