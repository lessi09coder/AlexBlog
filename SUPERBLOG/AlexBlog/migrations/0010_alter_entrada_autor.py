# Generated by Django 5.0.1 on 2024-02-02 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlexBlog', '0009_remove_usuario_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlexBlog.usuario'),
        ),
    ]
