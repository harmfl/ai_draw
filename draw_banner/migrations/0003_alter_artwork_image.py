# Generated by Django 3.2.25 on 2024-11-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw_banner', '0002_alter_artwork_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='image_draw'),
        ),
    ]
