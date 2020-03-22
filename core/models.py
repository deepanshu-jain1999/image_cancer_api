from django.db import models


class Media(models.Model):
    skin_image = models.ImageField(upload_to='Patient/%Y-%m-%d')
    web_opinion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.id}"
