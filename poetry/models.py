from django.db import models
from ckeditor.fields import RichTextField
from main.models import Poem

class Theme(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, null=True)
    theme = models.CharField(max_length=64)
    content = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.poem.name} - {self.theme}'

class Analysis(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.poem.name} - Analysis'
    
    class Meta:
        verbose_name_plural = 'Analyses'

class Context(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.poem.name} - Context'