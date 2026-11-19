import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Fullname')),
                ('appoint_name', models.CharField(max_length=200, verbose_name='Appoint name')),
                ('time_in', models.TimeField(verbose_name='Time in')),
                ('time_out', models.TimeField(verbose_name='Time out')),
                ('date', models.DateField(verbose_name='Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='doctors.doctor')),
            ],
            options={
                'ordering': ['-date', '-time_in'],
            },
        ),
    ]
