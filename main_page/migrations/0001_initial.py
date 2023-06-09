# Generated by Django 3.0.7 on 2023-04-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('comments', models.TextField()),
            ],
        ),
    ]
