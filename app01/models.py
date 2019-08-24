from django.db import models
import uuid

#Create your models here.
class UserInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    def __str__(self):
        return f'<{self.id}:{self.name}>'
#机台型号表
class Looms(models.Model):
    Id=models.AutoField(primary_key=True)
    Id_mac=models.CharField(max_length=4,unique=True,null=False)
    Model=models.CharField(max_length=30,null=False)
    Maker=models.CharField(max_length=20)
    Type=models.CharField(max_length=20)

#订单计划表
class Plans(models.Model):
    Id_plan=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    P_date=models.CharField(max_length=30,null=False)
    Id_mac=models.ForeignKey(to='Looms',on_delete=models.DO_NOTHING,to_field='Id')
