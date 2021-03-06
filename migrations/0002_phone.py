# Generated by Django 3.2.3 on 2022-01-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('hobby', models.TextField(null=True)),
                ('phone', models.CharField(max_length=150, null=True)),
                ('dob', models.DateField(null=True)),
                ('is_delete', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('delete_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
