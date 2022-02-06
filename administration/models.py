from django.db import models


# Create your models here.

class Service(models.Model):
    ICON_CHOICES = (
        ('twf_cleaning-1', 'twf_cleaning-1'),
        ('twf_cleaning-2', 'twf_cleaning-2'),
        ('twf_cleaning-3', 'twf_cleaning-3'),
    )


    name = models.CharField(max_length=50, null=False, blank=False)
    min_value = models.FloatField(null=False, blank=False)
    qtt_hours = models.IntegerField(null=False, blank=False)
    porcentage_comission = models.FloatField(null=False, blank=False)
    hours_bedroom = models.IntegerField(null=False, blank=False)
    value_bedroom = models.FloatField(null=False, blank=False)
    hours_room = models.IntegerField(null=False, blank=False)
    value_room = models.FloatField(null=False, blank=False)
    hours_bathroom = models.IntegerField(null=False, blank=False)
    value_bathroom = models.FloatField(null=False, blank=False)
    hours_kitchen = models.IntegerField(null=False, blank=False)
    value_kitchen = models.FloatField(null=False, blank=False)
    hours_yard = models.IntegerField(null=False, blank=False)
    value_yard = models.FloatField(null=False, blank=False)
    hours_others = models.IntegerField(null=False, blank=False)
    value_others = models.FloatField(null=False, blank=False)
    icon = models.CharField(null=False, blank=False, choices=ICON_CHOICES, max_length=14)
    position = models.IntegerField(null=False)