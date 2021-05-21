from django.db import models
from django.contrib.auth.models import User

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
