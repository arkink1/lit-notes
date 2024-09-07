from django.db import models

# Create your models here.
class Play(models.Model):
    name = models.CharField(max_length=69)
    playwright = models.CharField(max_length=69)

    def __str__(self):
        return f'{self.name} by {self.playwright}'

    class Meta:
        verbose_name_plural = 'Plays'

class Poem(models.Model):
    name = models.CharField(max_length=69)
    poet = models.CharField(max_length=69)

    def __str__(self):
        return f'{self.name} by {self.poet}'

    class Meta:
        verbose_name_plural = 'Poetry'

class Prose(models.Model):
    name = models.CharField(max_length=69)
    author = models.CharField(max_length=69)

    def __str__(self):
        return f'{self.name} by {self.author}'

    class Meta:
        verbose_name_plural = 'Proses'