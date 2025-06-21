from django.db import models

# Create your models here.
class choices(models.Model):
    status_choice=[
        ('r','raina'),
        ('d','dhoni'),
        ('v','virat'),
    ]
    name=models.CharField(verbose_name='Cricketer_name',choices=status_choice,default='d',max_length=50)
    scores=models.IntegerField()