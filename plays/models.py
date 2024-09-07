from django.db import models
from ckeditor.fields import RichTextField
from main.models import Play

class Theme(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, null=True)
    theme = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.play.name} - {self.theme}'

class Character(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, null=True)
    character = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.play.name} - {self.character}'

class Act(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, null=True)
    act = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.play.name} - {self.act} Analysis'
