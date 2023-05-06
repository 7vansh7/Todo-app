from django.db import models


class Item(models.Model):

    description = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description