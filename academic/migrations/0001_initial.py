# Generated by Django 4.1.9 on 2023-07-14 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the room name or number', max_length=50)),
                ('capacity', models.PositiveIntegerField(help_text='Enter the maximum number of occupants for the room')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.field')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the course', max_length=200)),
                ('code', models.CharField(help_text='Enter the course code', max_length=20, unique=True)),
                ('description', models.TextField(help_text='Enter a brief description of the course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(help_text='Enter the start time of the class')),
                ('end_time', models.DateTimeField(help_text='Enter the end time of the class')),
                ('days_of_week', models.CharField(help_text='Enter the days of the week the class meets', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.room')),
            ],
        ),
    ]
