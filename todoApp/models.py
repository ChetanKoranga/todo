from django.db import models
from datetime import datetime

class todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.title,self.created_at)