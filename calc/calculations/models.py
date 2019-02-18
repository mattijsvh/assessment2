from django.db import models

class Nums(models.Model):
    nums = models.CharField(max_length = 50)