# Generated by Django 4.2.16 on 2024-11-19 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0002_alter_profile_user_type"),
        ("AI_analyse", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="connectstudentteacher",
            name="student_code",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_code_connections",
                to="login.profile",
                verbose_name="学生密码",
            ),
            preserve_default=False,
        ),
    ]
