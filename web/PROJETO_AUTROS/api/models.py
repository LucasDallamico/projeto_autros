from django.db import models

class dispositivo_de_saida(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return f'{self.name} - {self.modulos.count()}'

    class Meta:
        verbose_name_plural = 'Dispositivos de saida'


class modulo(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')
    status = models.BooleanField(False)
    category = models.ForeignKey(
        dispositivo_de_saida,
        on_delete=models.deletion.DO_NOTHING,
        related_name='modulos'
    )

    def __str__(self):
        return self.name
