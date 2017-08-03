from django.db import models
from ..models import ContentType, ContentTypeManager
from ..search import BaseIndex


class GreenPowerProject(ContentType):

    INSTALLATION_TYPES = (
        ('solar-canopy', 'Solar - Canopy'),
        ('solar-rooftop', 'Solar - Roof Top Mount'),
        ('solar-wall', 'Solar - Wall Mount'),
        ('solar-ground-pole', 'Solar - Ground or Pole Mount'),
        ('solar-building-photovoltaic', 'Solar - Building Integrated Photovoltaic'),
        ('solar-other', 'Solar - Other')
    )

    OWNERSHIP_TYPES = (
        ('unknown', 'Unknown'),
        ('institution-owned', 'Institution Owned'),
        ('third-party-lease', 'Third-party Owned (Lease)'),
        ('third-party-purchase', 'Third-party Owned (Power Purchase Agreement'),
    )

    project_size = models.PositiveIntegerField()
    annual_production = models.PositiveIntegerField()
    installed_cost = models.PositiveIntegerField()
    date_installed = models.DateField()
    first_installation_type = models.CharField(max_length=200, choices=INSTALLATION_TYPES)
    second_installation_type = models.CharField(max_length=200, choices=INSTALLATION_TYPES)
    third_installation_type = models.CharField(max_length=200, choices=INSTALLATION_TYPES)
    ownership_type = models.CharField(max_length=200, choices=OWNERSHIP_TYPES)

    objects = ContentTypeManager()

    class Meta:
        verbose_name = 'Green Power Project'
        verbose_name_plural = 'Green Power Projects'


class GreenPowerProjectIndex(BaseIndex):
    def get_model(self):
        return GreenPowerProject

