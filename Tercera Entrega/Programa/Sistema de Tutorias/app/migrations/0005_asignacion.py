# Generated by Django 3.2.7 on 2021-09-22 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210920_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staffs')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.students')),
            ],
        ),
    ]
