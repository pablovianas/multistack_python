from django.db import models


# Create your models here.

class Service(models.Model):
    ICON_CHOICES = (
        ('twf_cleaning-1', 'twf_cleaning-1'),
        ('twf_cleaning-2', 'twf_cleaning-2'),
        ('twf_cleaning-3', 'twf_cleaning-3'),
    )


    name = models.CharField(max_length=50, null=False, blank=False)
    min_value = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    qtt_hours = models.IntegerField(null=False, blank=False)
    porcentage_comission = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    hours_bedroom = models.IntegerField(null=False, blank=False)
    value_bedroom = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    hours_room = models.IntegerField(null=False, blank=False)
    value_room = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    hours_bathroom = models.IntegerField(null=False, blank=False)
    value_bathroom = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    hours_kitchen = models.IntegerField(null=False, blank=False)
    value_kitchen = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    hours_yard = models.IntegerField(null=False, blank=False)
    value_yard = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    hours_others = models.IntegerField(null=False, blank=False)
    value_others = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=5)
    icon = models.CharField(null=False, blank=False, choices=ICON_CHOICES, max_length=14)
    position = models.IntegerField(null=False)