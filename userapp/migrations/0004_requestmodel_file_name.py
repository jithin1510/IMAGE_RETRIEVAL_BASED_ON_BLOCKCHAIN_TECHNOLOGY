# Generated by Django 4.1.3 on 2022-12-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_requestmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestmodel',
            name='file_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
