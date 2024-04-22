# Generated by Django 5.0.3 on 2024-04-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('Online', 'Online'), ('Busy', 'Busy'), ('Offline', 'Offline')], default='Online', max_length=10),
        ),
    ]
