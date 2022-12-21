from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', blank=False)
    description = models.CharField(max_length=250, verbose_name='Описание', blank=False)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def get_name_file(instance, filename):
        return '/'.join([get_random_string(length=5) + '_' + filename])

    image = models.ImageField(verbose_name='Картинка', upload_to=get_name_file, blank=False,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return str(self.name)
