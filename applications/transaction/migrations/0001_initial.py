# Generated by Django 3.1.2 on 2020-12-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile', verbose_name='Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('enable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('enable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('img', models.ImageField(upload_to='transaction')),
                ('id_bank_account_receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to='transaction.bank_account', verbose_name='Receiver')),
                ('id_bank_account_sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Sender', to='transaction.bank_account', verbose_name='Sender')),
                ('id_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.currency', verbose_name='Currency')),
                ('id_transaction_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.state', verbose_name='State')),
                ('id_transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.type', verbose_name='Type')),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='id_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.type'),
        ),
        migrations.AddField(
            model_name='currency',
            name='id_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.state', verbose_name='State'),
        ),
        migrations.AddField(
            model_name='bank_account',
            name='id_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.state', verbose_name='State'),
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country', verbose_name='Country')),
                ('id_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.state', verbose_name='State')),
            ],
        ),
    ]
