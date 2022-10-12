# Generated by Django 4.1.2 on 2022-10-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default=0)),
                ('alt_no', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=100)),
                ('blood', models.CharField(max_length=100)),
                ('e_date', models.DateField()),
            ],
        ),
    ]
