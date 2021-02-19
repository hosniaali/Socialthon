# Generated by Django 3.1.6 on 2021-02-19 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210219_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charities',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='اسم الجمعية'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='charity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.charities', verbose_name='الجمعية'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id_no',
            field=models.CharField(max_length=10, unique=True, verbose_name='رقم الهوية/الإقامة'),
        ),
    ]
