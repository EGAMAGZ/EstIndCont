from django.db import models

# Create your models here.
class TeamMember(models.Model):
    id_number = models.IntegerField('Boleta', unique=True)
    profile_img = models.ImageField('Foto de Perfil', upload_to='profile-img')
    name=models.CharField('Nombre',  max_length=60)
    surname=models.CharField('Apellido', max_length=60)
    role=models.CharField('Cargo', max_length=30)

    class Meta:
        verbose_name='Miembro de Equipo'
        verbose_name_plural='Miembros de Equipo'
        ordering=["-surname"]

    def __str__(self):
        return f"{self.surname},{self.name}"
