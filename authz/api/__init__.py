from flask import Blueprint, jsonify, abort

from authz.models import TaskOrder


api = Blueprint('api', __name__)

@api.route('/')
def root():
    return jsonify({'hello': 'world'})
