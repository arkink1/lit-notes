from django.db import models
from ckeditor.fields import RichTextField
from main.models import Prose

class Theme(models.Model):
    prose = models.ForeignKey(Prose, on_delete=models.CASCADE, null=True)
    theme = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.prose.name} - {self.theme}'

class Character(models.Model):
    prose = models.ForeignKey(Prose, on_delete=models.CASCADE, null=True)
    character = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.prose.name} - {self.character}'

class Chapter(models.Model):
    prose = models.ForeignKey(Prose, on_delete=models.CASCADE, null=True)
    chapter = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.prose.name} - {self.chapter} Analysis'

    class Meta:
        verbose_name_plural = 'Analyses'
