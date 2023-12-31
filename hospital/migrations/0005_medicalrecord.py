# Generated by Django 3.0 on 2023-12-26 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20231226_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symtom', models.CharField(max_length=200, verbose_name='症状')),
                ('diagnosis', models.CharField(max_length=200, verbose_name='诊断结果')),
                ('solution', models.CharField(max_length=200, verbose_name='治疗方案')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Registration', verbose_name='预约信息')),
            ],
        ),
    ]
