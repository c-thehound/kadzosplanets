# Generated by Django 2.2 on 2019-04-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='illustration',
            field=models.ImageField(default='', upload_to='illustrations'),
            preserve_default=False,
        ),
    ]