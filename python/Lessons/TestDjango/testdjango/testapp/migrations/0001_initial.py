# Generated by Django 3.1.3 on 2020-11-12 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('auto', 'Automatic'), ('mech', 'Mechanic')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_speed', models.IntegerField()),
                ('engine_type', models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol')], max_length=6)),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='testapp.transmission')),
            ],
        ),
    ]
