# Generated by Django 5.0.2 on 2024-04-13 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='usname',
            new_name='uname',
        ),
    ]
