from django.db import models

class Breakfast(models.Model):
    product_name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name

class Lunch(models.Model):
    product_name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name

class Dinner(models.Model):
    product_name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name
