# Generated by Django 3.0.8 on 2021-04-03 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0003_produkty_producent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.AddField(
            model_name='produkty',
            name='kategora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.Kategoria'),
        ),
    ]
