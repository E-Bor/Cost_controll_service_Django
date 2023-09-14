import enum

from django.db.models import Model
from django.forms import model_to_dict

from .models import EarningModel, SpendingModel


class RecordTypes(enum.Enum):
    earnings: str = 'earnings'
    spending: str = 'spending'

class DbManager:

    def __init__(self, model):

        self._model_objects = model.objects

    def create(self, data: dict) -> None:
        data = self._clean_data(data)
        self._model_objects.create(**data)

    def get(self, filter: dict):
        return self._model_objects.filter(**filter)

    def get_latest(self, view_depth):
        records = [
            model_to_dict(record)
            for record
            in self._model_objects.all().order_by('time_create')[:view_depth]
        ]
        for record in records:
            self._date_to_iso(record)
        return records

    def update(self, filter: dict, new_values: dict):
        self._model_objects.filter(**filter).update(**new_values)

    def delete(self, filter: dict):
        to_delete = self._model_objects.filter(**filter)
        to_delete.delete()

    def _clean_data(self, data) -> dict:
        data = data.dict()
        data.pop('csrfmiddlewaretoken')

        return {k: v for k, v in data.items() if 'Button' not in k}

    def _date_to_iso(self, record):
        record['time_create'] = record.get('time_create').isoformat()
