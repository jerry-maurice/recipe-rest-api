# Generated by Django 2.2.4 on 2019-08-20 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20190820_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='directions',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='directions',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipes'),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipes'),
        ),
    ]
