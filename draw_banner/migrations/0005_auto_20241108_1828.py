# Generated by Django 3.2.25 on 2024-11-08 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('draw_banner', '0004_drawing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='ai_analysis',
        ),
        migrations.AlterField(
            model_name='drawing',
            name='image',
            field=models.ImageField(upload_to='saved_drawings/', verbose_name='绘画作品文件'),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('text', 'Text'), ('image', 'Image')], max_length=10)),
                ('content', models.TextField()),
                ('ai_response', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
