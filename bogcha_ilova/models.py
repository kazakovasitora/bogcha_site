from wsgiref.validate import validator
from django.db import models
from .utils import rasm_olchami
# Create your models here.

class Lesson(models.Model):
    img = models.ImageField(upload_to='Darslarning_rasmi')
    dars_nomi = models.CharField(max_length=10)
    malumoti = models.TextField()
    bolalarning_yoshi = models.IntegerField(default=1)
    joy_soni = models.IntegerField(default=5)
    dars_vaqti = models.DateTimeField()
    dars_narxi = models.IntegerField(default=0)

    #telegram = models.URLField()
    #facebook = models.URLField()
    #instagram = models.URLField()
    
    def __str__(self):
        return self.dars_nomi
    
class Jamoa(models.Model):
    img=models.ImageField(upload_to='jamoa _rasmlari', validators=[rasm_olchami])
    ismi=models.CharField(max_length=100)
    fani=models.CharField(max_length=100)

    telegram = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    
    def __str__(self):
        return self.ismi