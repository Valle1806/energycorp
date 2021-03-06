from django.db import models
# Para asociar los contadores a su respectivo Cliente
from users.models import Client

# Create models here........................................................................
""" The models in this File are the objetcs than respresent the Publicity."""

class Commercial(models.Model):
    """Represent a substation object"""
    codeCommercial = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    urlCommercial = models.CharField(max_length=255)
    nameCommercial = models.CharField(max_length=255)
    contractorCommercial = models.CharField(max_length=255)
    resourceCommercial = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The Commercial was created: {}'.format(
            self.nameCommercial
        )
