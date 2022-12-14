# Generated by Django 4.1.3 on 2022-12-09 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('year_of_birth', models.CharField(blank=True, max_length=6, null=True)),
                ('year_of_death', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('time_period', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(blank=True, max_length=6, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=80, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='artists.artist')),
                ('genre', models.ManyToManyField(blank=True, related_name='artworks', to='artists.genre')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='field',
            field=models.ManyToManyField(blank=True, related_name='artists', to='artists.field'),
        ),
        migrations.AddField(
            model_name='artist',
            name='influenced_by',
            field=models.ManyToManyField(blank=True, related_name='influences', to='artists.artist'),
        ),
        migrations.AddField(
            model_name='artist',
            name='nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_artists', to='artists.country'),
        ),
        migrations.AddField(
            model_name='artist',
            name='state_of_residence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resident_artists', to='artists.country'),
        ),
        migrations.AddField(
            model_name='artist',
            name='style',
            field=models.ManyToManyField(blank=True, related_name='artists', to='artists.style'),
        ),
    ]
