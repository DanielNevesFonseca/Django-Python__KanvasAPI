from rest_framework.exceptions import APIException


class UniqueEmailError(APIException):
    status_code = 400
    default_code = "A user with that username already exists."
