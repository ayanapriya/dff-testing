import logging

from django.http import JsonResponse

from rest_framework import status as status_codes
from rest_framework.views import exception_handler

log = logging.getLogger('api_log')


def custom_exception_handler(exc, context):
    # https://www.django-rest-framework.org/api-guide/exceptions/#exception-handling-in-rest-framework-views
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    log.error('Error "%s" occurred. Context "%s"' % (exc, context))
    # Now add status code to the response. HTTP status code as 200 always
    if response is not None:
        if isinstance(response.data, list):  # list of errors
            response.data = {'errors': response.data, 'status': 0}
        elif isinstance(response.data, dict):
            response.data['status'] = 0
    return response


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    log.error(
        'Internal server error occurred for request "%s"' % request.__dict__
    )
    data = {
        'status': 0,
        'message': 'Server Error (500)',
        'data': {}
    }
    return JsonResponse(
        data,
        status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR
    )


def bad_request(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    log.error('"%s" occurred for request "%s"' % (exception, request))
    data = {
        'status': 0,
        'message': 'Bad Request (400)',
        'data': {}
    }
    return JsonResponse(data, status=status_codes.HTTP_400_BAD_REQUEST)
