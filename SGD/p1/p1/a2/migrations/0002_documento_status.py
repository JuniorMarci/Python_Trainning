# Generated by Django 4.2.3 on 2023-09-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='status',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]