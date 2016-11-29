from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=320, default="picture")
    picture = models.FileField()
