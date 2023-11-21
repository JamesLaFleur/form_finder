from request import request

REQUEST_URL = "http://127.0.0.1:8000/myapp/"

EXISTING_FORM_WITH_ONE_FIELD = {
    "email": "tester@gmail.com"
}

EXISTING_FORM_WITH_MANY_FIELDS = {
    "phone": "+7 988 765 33 88",
    "login": "Tom",
    "date_of_birth": "26.12.1995",
    "email": "tom@gmail.com",
    "password": "123456",
    "repeat_password": "123456"
}

EXISTING_FORM_WITH_MANY_FIELDS_EN_DATE = {
    "phone": "+7 988 765 33 88",
    "login": "Tom",
    "date_of_birth": "2003-07-05",
}

FORM_NOT_EXISTS = {
    "my_field": "+7 910 345 45 32",
    "my_date": "2015-11-11",
    "my_other_date": "21.10.1991",
    "my_name": "Tommy",
    "my_mail": "test@yandex.ru"
}

def create_query(data: dict) -> str:
    data_list: list = []

    for key, value in data.items():
        data_list.append(key + "=" + value)

    return "&".join(data_list)

result1 = request(REQUEST_URL, "POST", {"query": create_query(EXISTING_FORM_WITH_ONE_FIELD)})

result2 = request(REQUEST_URL, "POST", {"query": create_query(EXISTING_FORM_WITH_MANY_FIELDS)})

result3 = request(REQUEST_URL, "POST", {"query": create_query(EXISTING_FORM_WITH_MANY_FIELDS_EN_DATE)})

result4 = request(REQUEST_URL, "POST", {"query": create_query(FORM_NOT_EXISTS)})

print("--------------------------------------")
print(f"{'\033[92m'}START TESTING FORM PARSER{'\033[92m'}")

print("-----")
print(f"{'\033[96m'}EXISTING_FORM_WITH_ONE_FIELD:" + result1.body)
print("-----")

print("-----")
print(f"{'\033[96m'}EXISTING_FORM_WITH_MANY_FIELDS:" + result2.body)
print("-----")

print("-----")
print(f"{'\033[96m'}EXISTING_FORM_WITH_MANY_FIELDS_EN_DATE:" + result3.body)
print("-----")

print("-----")
print(f"{'\033[96m'}FORM_NOT_EXISTS:" + result4.body)
print("--------------------------------------")

print(f"{'\033[93m'}TESTING FINISHED")