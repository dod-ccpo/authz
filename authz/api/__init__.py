from flask import Blueprint, jsonify, abort


api = Blueprint('api', __name__)

@api.route('/')
def root():
    return jsonify({'hello': 'world'})
