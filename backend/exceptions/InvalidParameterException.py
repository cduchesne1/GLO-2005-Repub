import json

from flask import make_response, jsonify
from werkzeug.exceptions import HTTPException


class InvalidParameterException(HTTPException):
    def __init__(self, description):
        self.code = 400
        self.description = description
        self.response = make_response(jsonify({"code": 'INVALID_PARAMETER', "desc": description}), self.code)
