from django.db import models
from django.utils.timezone import now

# Create your models here.

class blog_content(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    blog_type=models.CharField(max_length=50)
    slug=models.CharField(max_length=200)
    timeStamp=models.DateTimeField(default=now)
    blog_thumbnail=models.ImageField(upload_to="static/image/A_blog")
    content=models.TextField()

    def __str__(self):
        return self.title + " And content type is" + self.blog_type