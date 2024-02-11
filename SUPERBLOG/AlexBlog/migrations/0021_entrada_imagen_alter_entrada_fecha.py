# Generated by Django 5.0.1 on 2024-02-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlexBlog', '0020_alter_entrada_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(default='imagenDefault', max_length=200, upload_to='static/imagenes/', verbose_name='Imagen del articulo.'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
