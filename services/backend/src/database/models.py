from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class CSVData(models.Model):
    BatchId = fields.IntField()
    Model = fields.CharField(max_length=128)
    Scenario = fields.CharField(max_length=128)
    Region = fields.CharField(max_length=128)
    Item = fields.CharField(max_length=128)
    Variable = fields.CharField(max_length=128)
    Year = fields.IntField()
    Unit = fields.CharField(max_length=128)
    Value = fields.FloatField()