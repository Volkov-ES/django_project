# Generated by Django 3.2.13 on 2022-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_images'),
        ),
    ]
