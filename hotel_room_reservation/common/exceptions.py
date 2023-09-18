"""
common exceptions class
"""
from rest_framework import status


class CommonException(Exception):
    """
    a common exception class to handle exceptions
    """
    def __init__(self, message, status_code=status.HTTP_400_BAD_REQUEST, extras: dict = None):
        """
        adds structure that is suitable for rest endpoint
        :param message:
        :param status_code:
        :param extras:
        """
        self.error_message = message
        self.status_code = status_code
        self.details = extras

    def to_dict(self):
        """
        transform the exceptions to json structure
        :return:
        """
        error = {
            "status_code": self.status_code,
            "error": self.error_message,
        }
        if self.details is not None:
            error["details"] = self.details
        return error
