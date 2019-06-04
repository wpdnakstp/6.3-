import datetime
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(max_length=1000)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chioce_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.chioce_text


class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to = "blogimg")
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(120,100)],
    format = "JPEG", options={'quality':60})