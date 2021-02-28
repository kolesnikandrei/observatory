import logging
from rest_framework import status


logger = logging.getLogger(__name__)


class ResponseWrapper:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return self.process_response(request, response)

    def process_response(self, request, response):
        content_type = response.get('Content-Type', None)

        if content_type != 'application/json':
            return response

        try:
            data = response.data
        except AttributeError:
            data = None

        response_status_code = response.status_code
        is_success = status.is_success(response_status_code)
        is_error = status.is_client_error(response_status_code) or status.is_server_error(response_status_code)

        response.data = {
            'status_code': response_status_code,
            'success': is_success
        }

        if is_error:
            errors = data
            data = None
            response.data['error'] = errors

        response.data['data'] = data
        response._is_rendered = False

        try:
            response.render()
        except AttributeError as e:
            logger.error(f'Can\'t wrap and render response: {e}. Status code: {response_status_code}')

        return response



