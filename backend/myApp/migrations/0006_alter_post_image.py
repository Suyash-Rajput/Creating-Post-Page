# Generated by Django 5.0.4 on 2024-04-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='1_tCLgoTtePAdJhGRImx-B-g.jpg', upload_to='post'),
        ),
    ]
