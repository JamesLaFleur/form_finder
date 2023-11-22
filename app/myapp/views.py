from django.shortcuts import render
from django.http import HttpResponse
from .models import mycol
from .services.form_query_service import Form_query_service
from .util.field_validator import Field_validator
from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt
def index(request):
    try:
        json_data: dict[str, str] = json.loads(request.body.decode(encoding='UTF-8'))

        form_query_service = Form_query_service(mycol, Field_validator())
        form = form_query_service.search_form_by_data(json_data.get("query"))
        return HttpResponse(json.dumps(form))
    except json.JSONDecodeError:
        return HttpResponse(json.dumps("Invalid data"))
