# Generated by Django 4.2.13 on 2024-06-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0002_alter_mockmodel_description_alter_mockmodel_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mockmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
