# Generated by Django 5.0 on 2024-01-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_programminglanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('work_id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=255)),
                ('work_title', models.ImageField(max_length=266, upload_to='')),
            ],
        ),
    ]
