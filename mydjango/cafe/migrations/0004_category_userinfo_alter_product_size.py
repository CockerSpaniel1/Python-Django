# Generated by Django 5.0.2 on 2024-03-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_rename_pic_product_pid_alter_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('L', 'LARGE'), ('M', 'MEDIUM'), ('S', 'SMALL')], max_length=1),
        ),
    ]
