from django.db import models

# Create your models here.

# Las tablas se representan mediante clases en python
class Usuario(models.Model):
    username = models.CharField(max_length = 10, primary_key = True, unique = True)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.username