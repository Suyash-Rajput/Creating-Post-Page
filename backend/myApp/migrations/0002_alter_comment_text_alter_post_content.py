# Generated by Django 5.0.4 on 2024-04-09 08:35

import froala_editor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
