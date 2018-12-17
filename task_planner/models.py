from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)


class Day(models.Model):
    pass


class Week(models.Model):
    pass