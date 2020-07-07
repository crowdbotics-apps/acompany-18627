from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Actions(models.Model):
    "Generated Model"
    name = models.TextField()
    phone_number = models.TextField()


class Company(models.Model):
    "Generated Model"
    name = models.TextField()
    actions = models.ForeignKey(
        "home.Actions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="company_actions",
    )
