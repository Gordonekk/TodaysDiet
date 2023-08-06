# Generated by Django 4.2.4 on 2023-08-06 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='kind',
            field=models.CharField(choices=[('HQP', 'High-quality protein source'), ('HQPF', 'High-quality protein with fats'), ('CC', 'Complex carbohydrates'), ('F', 'Fiber')], default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
    ]
