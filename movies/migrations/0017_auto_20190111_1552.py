# Generated by Django 2.1.1 on 2019-01-11 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20190111_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['full_name'], 'verbose_name_plural': 'people'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='date_added',
        ),
    ]