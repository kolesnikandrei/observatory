from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    max_speed = models.IntegerField()
    engine_type = models.CharField(choices=[("diesel", "Diesel"), ("petrol", "Petrol"), ("electric", "Electric")],
                                   max_length=10)
    transmission = models.ForeignKey("Transmission", null=False, on_delete=models.PROTECT, related_name="cars")

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"car named {self.name}"


class Transmission(models.Model):
    type = models.CharField(choices=[("auto", "Automatic"), ("mech", "Mechanic")], max_length=4)

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"{self.type}"
