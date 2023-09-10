import enum

from django.forms import model_to_dict

from .models import MoneyTransactionModel


class RecordTypes(enum.Enum):
    earnings: str = 'earnings'
    spending: str = 'spending'

class DbManager:

    __MODEL_OBJECTS = MoneyTransactionModel.objects


    def create(self, data, earnings: bool = False) -> None:

        if not earnings:
            data = self._convert_spending(data)

        self.__MODEL_OBJECTS.create(**data)


    def get_latest(self):
        return [model_to_dict(record) for record in self.__MODEL_OBJECTS.all().order_by('time_create')[:3]]


    def update(self, updated_condition):
        ...

    def delete(self, deleted_condition):
        ...




    def _convert_spending(self, data: dict) -> dict:
        money = data.pop('money')
        data['money'] = -money
        return data

writer = DbManager()