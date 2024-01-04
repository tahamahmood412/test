# Generated by Django 4.2.5 on 2024-01-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelDataModel', '0007_rename_question_question_short_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('short', 'Short Question'), ('long', 'Long Question')], default='short', max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='short_question',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]