from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

from .validators import validate_file_extension


# Create your models here.
class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField('Foto de Perfil', upload_to='profile-img')
    description = models.TextField('Descripción', blank=True, null=True, default='No ha dado descripcion')

    class Meta:
        verbose_name='Miembro de Equipo'
        verbose_name_plural='Miembros de Equipo'
        ordering=["-user"]

    def __str__(self):
        return self.user.get_full_name()


class ProsoftDoc(models.Model):
    title = models.CharField('Titulo', max_length=120)
    document = models.FileField(upload_to='prosoft/', validators=[validate_file_extension])
    slug = models.SlugField('Slug', blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Documento de Prosoft'
        verbose_name_plural = 'Documentos de Prosoft'
        ordering = ['-created','title']

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('prosoft-doc', kwargs={'document_slug': self.slug})

    def __str__(self) -> str:
        return self.title
