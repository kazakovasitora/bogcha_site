# Generated by Django 4.0.4 on 2022-06-03 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bogcha_ilova', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='Darslarning_rasmi'),
            preserve_default=False,
        ),
    ]
