# encoding=utf8
# author: sophia
# create_time: 2024/12/02 10:58
# file: main_api.py
import time
from flask import Blueprint, request, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route('/test', methods=['GET', 'POST'])
def test():
    requests_data = request.json or request.args or request.form or {}
    print('test: requests_data:{}'.format(requests_data))
    result = {
        "time": time.time(),
    }
    return jsonify(result)
