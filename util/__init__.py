from django.db import models

class SingletonModel(models.Model):

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs) -> None:
        self.pk = 1
        return super().save(*args,**kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
