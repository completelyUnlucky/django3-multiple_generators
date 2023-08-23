from django.db import models

# Create your models here.


class Nickname(models.Model):
    nickname = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return self.nickname
