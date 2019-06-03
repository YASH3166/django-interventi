# Generated by Django 2.2.1 on 2019-06-03 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0007_intervento_urgente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preventivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('is_confermato', models.BooleanField(default=False)),
                ('data_inizio_lavori', models.DateField(blank=True, null=True)),
                ('data_fine_lavori', models.DateField(blank=True, null=True)),
                ('importo', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('annotazioni', models.TextField(blank=True, null=True)),
                ('data_inserimento', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_modifica', models.DateTimeField(auto_now=True)),
                ('fornitore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preventivi', to='interventi.Fornitore')),
                ('intervento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preventivi', to='interventi.Intervento')),
            ],
            options={
                'verbose_name_plural': 'Preventivi',
            },
        ),
        migrations.CreateModel(
            name='PreventivoAllegato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='preventivi/%Y/%m/%d/')),
                ('preventivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allegati', to='interventi.Preventivo')),
            ],
            options={
                'verbose_name_plural': 'PreventivoAllegati',
            },
        ),
    ]
