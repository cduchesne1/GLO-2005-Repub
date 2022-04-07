from flask import make_response, jsonify
from werkzeug.exceptions import HTTPException


class ItemNotFoundException(HTTPException):
    def __init__(self, description):
        self.code = 404
        self.description = description
        self.response = make_response(jsonify({"code": 'ITEM_NOT_FOUND', "desc": description}), self.code)
