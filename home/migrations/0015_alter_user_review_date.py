# Generated by Django 5.0 on 2024-01-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_user_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]