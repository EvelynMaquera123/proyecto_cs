# Generated by Django 3.1.2 on 2020-11-30 19:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0009_auto_20201129_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 19, 19, 56, 57812, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.curriculum')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.profession')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.school')),
            ],
        ),
    ]