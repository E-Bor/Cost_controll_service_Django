

class DbManager:

    def __init__(self, model):

        self._model_objects = model.objects

    def create(self, data: dict, user_id) -> None:
        data = self._clean_data(data)
        self._model_objects.create(user_id=user_id, **data)

    def get(self, filter: dict):
        return self._model_objects.filter(**filter)

    def get_latest(self, view_depth, user_id):

        records = [
            record.to_dict()
            for record
            in self._model_objects.filter(user_id=user_id)[:view_depth]
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
