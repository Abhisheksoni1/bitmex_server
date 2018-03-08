from django.db import models

# Create your models here.


class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=9632)

    class Meta:
        ordering = ('created',)
