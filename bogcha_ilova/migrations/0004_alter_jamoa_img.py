# Generated by Django 4.0.4 on 2022-06-13 14:47

import bogcha_ilova.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bogcha_ilova', '0003_jamoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jamoa',
            name='img',
            field=models.ImageField(upload_to='jamoa _rasmlari', validators=[bogcha_ilova.utils.rasm_olchami]),
        ),
    ]
