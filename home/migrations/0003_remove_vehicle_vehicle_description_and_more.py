# Generated by Django 5.0 on 2023-12-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_description',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_specification',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_description1',
            field=models.TextField(default='', max_length=57),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_description2',
            field=models.TextField(default='', max_length=57),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_description3',
            field=models.TextField(default='', max_length=57),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_description4',
            field=models.TextField(default='', max_length=57),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_specification1',
            field=models.TextField(default='', max_length=54),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_specification2',
            field=models.TextField(default='', max_length=54),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_specification3',
            field=models.TextField(default='', max_length=54),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_specification4',
            field=models.TextField(default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition1',
            field=models.TextField(max_length=57),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition2',
            field=models.TextField(max_length=57),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition3',
            field=models.TextField(max_length=57),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition4',
            field=models.TextField(max_length=57),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition5',
            field=models.TextField(blank=True, max_length=57),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition6',
            field=models.TextField(blank=True, max_length=57),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='TermsCondition7',
            field=models.TextField(blank=True, max_length=57),
        ),
    ]
