# Generated by Django 3.1.14 on 2024-10-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downapp', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
