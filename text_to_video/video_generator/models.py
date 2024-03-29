from django.db import models


class Request(models.Model):
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.pk}"
