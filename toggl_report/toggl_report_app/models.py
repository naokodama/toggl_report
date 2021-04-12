from django.db import models

# Create your models here.

class TogglUser(models.Model):
    user_id = models.CharField(max_length = 20)
    api_token = models.CharField(max_length = 100)

    def __str__(self):
        return self.user_id

