from django.db import models

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(verbose_name='Genero de mascota',max_length=10)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'genero'
        verbose_name_plural = 'generos'
        ordering = ['gender']

    def __str__(self) -> str:
        return self.gender

class MascotType(models.Model):
    mascotType = models.CharField(verbose_name='Tipo de mascota', max_length=20)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'tipo de mascota'
        verbose_name_plural = 'tipo de mascotas'
        ordering = ['mascotType']

    def __str__(self) -> str:
        return self.mascotType

class Mascot(models.Model):
    idMascot = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    name = models.CharField(verbose_name='Nombre',max_length=80)
    mascotType = models.ForeignKey(MascotType,verbose_name='Tipo de Mascota',on_delete=models.CASCADE)
    breed = models.CharField(verbose_name='Raza de mascota', max_length=40)
    gender = models.ForeignKey(Gender,verbose_name='Genero de Mascota',on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(verbose_name='Imagen',upload_to='mascotas',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'
        ordering = ['name','mascotType']

    def __str__(self) -> str:
        return self.name
