# Generated by Django 2.2.7 on 2020-03-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Актеры и режиссеры', 'verbose_name_plural': 'Актеры и режиссеры'},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='fees_in_world',
            new_name='fess_in_world',
        ),
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='режиссер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movies/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2019, verbose_name='Дата выхода'),
        ),
    ]
