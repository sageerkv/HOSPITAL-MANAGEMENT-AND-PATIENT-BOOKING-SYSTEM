# Generated by Django 4.1.7 on 2023-04-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hos_app', '0005_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
    ]
