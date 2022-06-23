# Generated by Django 4.0.5 on 2022-06-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
