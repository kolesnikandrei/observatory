from django.db import models

# Create your models here.


class Car(models.Model):

    name = models.CharField(max_length=100)
    max_speed = models.IntegerField(default=120)
    engine_type = models.CharField(max_length=10, choices=[('disel', 'Disel'), ('petrol', 'Petrol'), ("electric", "Electric")])
    transmission = models.ForeignKey('Transmission', null=False, on_delete=models.PROTECT, related_name='cars')
    # release_date = models.DateTimeField()

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"car named {self.name}"


class Transmission(models.Model):

    type = models.CharField(max_length=10, choices=[('auto', 'Auto'), ('mech', 'Mechanic')])
    model_name = models.CharField(max_length=10, null=True)

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"{self.type}"

