# Generated by Django 5.0.4 on 2024-05-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('studio', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
