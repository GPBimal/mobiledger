from django.db import models

class Uzerlist(models.Model):
    userid = models.AutoField(primary_key=True)
    uzername = models.TextField()
    uzerpw = models.TextField()
    uzerlevel = models.IntegerField()

    class Meta:
        db_table = 'uzerlist'

class Mainledger(models.Model):
    RecNo = models.AutoField(primary_key=True)
    IDNO = models.IntegerField(default=None, blank=True, null=True)
    NepDate = models.TextField()
    EngDate = models.TextField()
    Particular = models.TextField()
    AmtRs = models.FloatField(default=None, blank=True, null=True)
    AmtCode = models.IntegerField(default=None, blank=True, null=True)
    VatBillNo = models.IntegerField(default=0)
    Approved = models.IntegerField(default=0)

    class Meta:
        db_table = 'mainledger'

class Customer(models.Model):
    IDNO = models.IntegerField(primary_key=True)
    FullName = models.TextField()
    DistName = models.TextField()
    Address = models.TextField()
    PhoneNo = models.TextField()
    MobileNo = models.TextField()
    InstDate = models.TextField()
    RenDate = models.TextField()
    RenewAmt = models.FloatField(default=None, blank=True, null=True)
    RemBalRs = models.FloatField(default=None, blank=True, null=True)
    AgentName = models.TextField()
    Software = models.TextField()
    Remarks = models.TextField()
    ClntStat = models.IntegerField(default=1)
    RepDetails = models.CharField(max_length=256, default='-')
    PANNo = models.CharField(max_length=12, default='-')
    IsUpdated = models.IntegerField()

    class Meta:
        db_table = 'customer'