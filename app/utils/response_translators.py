from decimal import Decimal
from logging import exception
from rest_framework import status
import json
import ast
from rest_framework.response import Response

def basic_response_translator(is_success, data, total_result=None, start=None, end=None, total_count=None):
    response_translator = {"success": is_success}
    if total_result:
        response_translator["total_result"] = total_result
    elif total_result == 0:
        response_translator["total_result"] = total_result
    if start:
        response_translator["start"] = start
    elif start == 0:
        response_translator["start"] = start
    if total_count:
        response_translator["total_count"] = total_count
    elif total_count == 0:
        response_translator["total_count"] = 0
    if end:
        response_translator["end"] = end
    elif end == 0:
        response_translator["end"] = end
    response_translator["data"] = data
    return response_translator


def basic_response(message, status):
    return Response(message, status=status)


def main_exception(error_message, status):
    if error_message:
        return Response(error_message, status=status.HTTP_412_PRECONDITION_FAILED)

