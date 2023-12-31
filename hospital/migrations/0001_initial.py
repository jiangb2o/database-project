# Generated by Django 3.0 on 2023-12-18 13:45

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='科室名')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('title', models.CharField(max_length=20, verbose_name='职称')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('gender', models.SmallIntegerField(blank=True, choices=[(0, '男'), (1, '女')], null=True, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_time', models.DateTimeField(verbose_name='挂号时间')),
                ('peirod', models.SmallIntegerField(choices=[(0, '8:00-10:00'), (1, '10:00-12:00'), (2, '14:00-16:00'), (3, '16:00-18:00')], verbose_name='挂号时段')),
                ('status', models.CharField(choices=[('registered', '已挂号'), ('cancelled', '已取消')], max_length=10, verbose_name='状态')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='hospital.Doctor', verbose_name='医生')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospital.Patient', verbose_name='患者')),
            ],
        ),
    ]
