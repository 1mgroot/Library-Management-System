# Generated by Django 4.1.4 on 2022-12-13 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('lname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('email_address', models.CharField(blank=True, max_length=20, null=True)),
                ('mailing_country', models.CharField(blank=True, max_length=20, null=True)),
                ('mailing_city', models.CharField(blank=True, max_length=20, null=True)),
                ('mailing_street', models.CharField(blank=True, max_length=20, null=True)),
                ('mailing_room', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('authors', models.ManyToManyField(blank=True, related_name='books', to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('email_address', models.CharField(blank=True, max_length=20, null=True)),
                ('identification_type', models.CharField(max_length=20)),
                ('identification_num', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=1)),
                ('start_datetime', models.DateTimeField()),
                ('stop_datetime', models.DateTimeField()),
                ('customers', models.ManyToManyField(blank=True, related_name='events', to='library.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='DATE')),
                ('amount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyRoom',
            fields=[
                ('room_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('capacity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='DATE')),
                ('time_slot', models.CharField(max_length=10)),
                ('number_of_people', models.SmallIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.studyroom')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date', models.DateTimeField(db_column='DATE')),
                ('card_holder_lname', models.CharField(max_length=20)),
                ('card_holder_fname', models.CharField(max_length=20)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('invitation_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.author')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.event')),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('copy_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.book')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrow_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10)),
                ('borrow_date', models.DateTimeField()),
                ('expect_return_date', models.DateTimeField()),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('actural_return_date', models.DateTimeField(blank=True, null=True)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.copy')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.customer')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.invoice')),
            ],
        ),
    ]
