from marshmallow_sqlalchemy import ModelSchema 
from marshmellow_sqlalchemy.fields import fields
# from . import StocksLocation, Account, AccountRole

class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole

class AccoutSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account

# class WeatherLocationSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated',
    ))


#   class Meta:
#     model = WeatherLocation

