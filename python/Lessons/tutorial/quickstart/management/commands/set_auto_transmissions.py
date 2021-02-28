from django.core.management.base import BaseCommand
from testapp.models import Car, Transmission


class Command(BaseCommand):
    help = 'Set transmission to auto'

    def handle(self, *args, **options):
        cars_with_mech = Car.objects.filter(transmission__type='mech')
        if not cars_with_mech:
            self.stdout.write(self.style.NOTICE('Cars with mech are absent'))
            return
        else:
            auto_transmission = Transmission.objects.filter(type='auto').first()
            for car_with_mech in cars_with_mech:
                car_with_mech.transmission = auto_transmission

            Car.objects.bulk_update(cars_with_mech, ['transmission'])
            self.stdout.write(self.style.SUCCESS('Cars were successfully updated'))
