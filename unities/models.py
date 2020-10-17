from django.db import models


from ckeditor.fields import RichTextField


# Create your models here.
from django.utils.text import slugify


class Unity(models.Model):
    number = models.IntegerField('Numero de Unidad', unique=True, default=1)
    name = models.CharField('Nombre de Unidad', max_length=120)
    slug = models.SlugField('Slug', unique=True, blank=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ["-number"]

    def save(self, *args, **kwargs):
        slug_text = f'unidad {self.number}'
        self.slug = slugify(slug_text)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number}){self.name}"


class UnityContent(models.Model):
    title = models.CharField('Titulo', max_length=120)
    unity = models.ForeignKey(Unity, on_delete=models.CASCADE, verbose_name='Unidad', null=True)
    content = RichTextField('Contenido', blank=True, null=True)
    slug = models.SlugField('Slug', blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Contenido de la Unidad'
        verbose_name_plural = 'Contenidos de la Unidad'
        ordering = ["-title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
