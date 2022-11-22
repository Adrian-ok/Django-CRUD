# Generated by Django 4.1.3 on 2022-11-16 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'estado_civil',
                'verbose_name_plural': 'estados_civiles',
                'db_table': 'estado_civil',
            },
        ),
        migrations.CreateModel(
            name='grup_sangre',
            fields=[
                ('id_sangre', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sangre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'grup_sangre',
                'verbose_name_plural': 'grup_sangres',
                'db_table': 'grup_sangre',
            },
        ),
        migrations.CreateModel(
            name='localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('localidad', models.CharField(max_length=100, unique=True)),
                ('cp', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'localidad',
                'verbose_name_plural': 'localidades',
                'db_table': 'localidad',
            },
        ),
        migrations.CreateModel(
            name='sector',
            fields=[
                ('id_sector', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nom_sector', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'sector',
                'verbose_name_plural': 'sectores',
                'db_table': 'sector',
            },
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_legajo', models.IntegerField(unique=True)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.IntegerField(unique=True)),
                ('fn', models.DateField()),
                ('telefono', models.BigIntegerField(unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('cant_hijos', models.IntegerField(default=0)),
                ('casa', models.BooleanField(default=False)),
                ('instruccion', models.CharField(choices=[('P', 'Primaria'), ('S', 'Secundaria'), ('T', 'Terciaria'), ('U', 'Universitaria')], default='S', max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('fi', models.DateField()),
                ('renovacion', models.DateField()),
                ('venc_libreta', models.DateField()),
                ('recordar', models.IntegerField()),
                ('lastupdate', models.DateTimeField(auto_now=True)),
                ('estado_civil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.estado')),
                ('grup_sangre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.grup_sangre')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.localidad')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.sector')),
            ],
        ),
    ]
