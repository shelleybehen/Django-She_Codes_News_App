# Generated by Django 3.2.5 on 2021-08-28 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
