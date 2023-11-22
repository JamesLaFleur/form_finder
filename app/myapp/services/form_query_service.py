from typing import Collection
from .. views import *

class Form_query_service:

    def __init__(self, form_repository: Collection, field_validator):
        self.form_repository = form_repository
        self.field_validator = field_validator

    def parse_query(self, query_string) -> dict[str, str]:
        split_query: list[str] = query_string.split("&")
        # TO DO - проверка, что получился не пустой список
        form_data: dict[str, str] = {}

        for item in split_query:
            item_data = item.split("=")
            # TO DO - проверка, что получился список с длиной 2 - ключ и значение
            form_data[item_data[0]] = item_data[1]

        return form_data

    def validate_form_data(self, form_data: dict[str, str])  -> dict[str, str]:
        typed_fields: dict[str, str] = {}
        for key, value in form_data.items():
            typed_fields[key] = self.field_validator.get_field_type(value)

        return typed_fields;
            

    def search_form_by_data(self, fields) -> dict[str, str] | str:
        parsed_data = self.parse_query(fields)
        typed_data = self.validate_form_data(parsed_data)

        form = self.form_repository.find_one(typed_data)
        if form is None:
            return typed_data
        else:
            return form.get("name")