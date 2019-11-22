from djongo import models

class Machine(models.Model):
    ee_tag = models.CharField('EE Tag #', max_length=60, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    alias = models.CharField('Alias', max_length=60)
    ip = models.CharField('IP Address', max_length=15)
    description = models.TextField('Description', max_length=250, blank=True)
    updated = models.DateTimeField('Last Updated', auto_now=True)

    class Meta:
        ordering = ['ee_tag']
