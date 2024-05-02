from django.db import models


# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE, default=None)
    resume = models.TextField(null=True, blank=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.release_date}, {self.resume}, {self.studio}, {self.duration}"


class Studio(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField(blank=True, null=True)
    address = models.TextField(null=True, blank=False)

    def __str__(self):
        return f"{self.name}, {self.creation_date}, {self.address}"
