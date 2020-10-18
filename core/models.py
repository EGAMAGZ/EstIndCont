from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number = models.CharField('Boleta', unique=True, max_length=10)
    profile_img = models.ImageField('Foto de Perfil', upload_to='profile-img')
    role=models.CharField('Cargo', max_length=30)

    class Meta:
        verbose_name='Miembro de Equipo'
        verbose_name_plural='Miembros de Equipo'
        ordering=["-user"]

    def __str__(self):
        return f"{self.surname},{self.name}"
