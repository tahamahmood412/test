# Generated by Django 4.2.5 on 2024-01-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelDataModel', '0002_rename_exceldatamodel_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=100)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='questions',
        ),
    ]
