from django.db import models

# Create your models here.
# Each model here represents a table in the DB

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    idcategory = models.AutoField(primary_key=True)
    cat_name = models.CharField(db_column='Cat_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name_plural = "category"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Order(models.Model):
    idorder = models.AutoField(primary_key=True)
    date_ordered = models.DateField(db_column='Date_Ordered', blank=True, null=True)  # Field name made lowercase.
    number_ordered = models.IntegerField(db_column='Number_Ordered', blank=True, null=True)  # Field name made lowercase.
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct')  # Field name made lowercase.
    idsupplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='idSupplier')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Product(models.Model):
    idproduct = models.AutoField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buy_price = models.DecimalField(db_column='Buy_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sell_price = models.DecimalField(db_column='Sell_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idsupplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='idSupplier')  # Field name made lowercase.
    idcategory = models.ForeignKey(Category, models.DO_NOTHING, db_column='idCategory')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Sell(models.Model):
    idsell = models.AutoField(primary_key=True)
    date_sold = models.DateField(db_column='Date_Sold', blank=True, null=True)  # Field name made lowercase.
    number_sold = models.IntegerField(db_column='Number_Sold', blank=True, null=True)  # Field name made lowercase.
    idproduct = models.ForeignKey(Product, models.DO_NOTHING, db_column='idProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sell'
        verbose_name_plural = "sell"


class Stock(models.Model):
    idstock = models.AutoField(primary_key=True)
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    idproduct = models.ForeignKey(Product, models.DO_NOTHING, db_column='idProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock'
        


class Supplier(models.Model):
    idsupplier = models.AutoField(db_column='idSupplier', primary_key=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='Supplier_Name', max_length=25)  # Field name made lowercase.
    enterprise_name = models.CharField(db_column='Enterprise_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact_number = models.CharField(db_column='Contact_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_Id', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'
