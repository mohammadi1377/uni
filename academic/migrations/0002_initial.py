# Generated by Django 4.2.3 on 2023-07-15 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.professor'),
        ),
        migrations.AddField(
            model_name='class',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.room'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='user.student'),
        ),
        migrations.AddConstraint(
            model_name='room',
            constraint=models.UniqueConstraint(fields=('name', 'department'), name='unique_room_department'),
        ),
    ]
