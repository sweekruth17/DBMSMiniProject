# Generated by Django 3.1.4 on 2020-12-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idcategory', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(blank=True, db_column='Cat_Name', max_length=20, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('idorder', models.AutoField(primary_key=True, serialize=False)),
                ('date_ordered', models.DateField(blank=True, db_column='Date_Ordered', null=True)),
                ('number_ordered', models.IntegerField(blank=True, db_column='Number_Ordered', null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idproduct', models.AutoField(db_column='idProduct', primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, db_column='Product_Name', max_length=30, null=True)),
                ('buy_price', models.DecimalField(blank=True, db_column='Buy_Price', decimal_places=2, max_digits=10, null=True)),
                ('sell_price', models.DecimalField(blank=True, db_column='Sell_Price', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('idsell', models.AutoField(primary_key=True, serialize=False)),
                ('date_sold', models.DateField(blank=True, db_column='Date_Sold', null=True)),
                ('number_sold', models.IntegerField(blank=True, db_column='Number_Sold', null=True)),
            ],
            options={
                'db_table': 'sell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('idstock', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
            ],
            options={
                'db_table': 'stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('idsupplier', models.AutoField(db_column='idSupplier', primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(db_column='Supplier_Name', max_length=25)),
                ('enterprise_name', models.CharField(blank=True, db_column='Enterprise_Name', max_length=50, null=True)),
                ('contact_number', models.CharField(blank=True, db_column='Contact_Number', max_length=15, null=True)),
                ('mobile_number', models.CharField(blank=True, db_column='Mobile_Number', max_length=15, null=True)),
                ('email_id', models.CharField(blank=True, db_column='Email_Id', max_length=30, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=100, null=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
    ]
