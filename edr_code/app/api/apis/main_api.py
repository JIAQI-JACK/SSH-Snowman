# encoding=utf8
# author: sophia
# create_time: 2024/12/02 10:58
# file: main_api.py
import time
import random
from flask import Blueprint, jsonify
from service.data_collect.data_collection import get_all_data
from service.data_analysis.analysis import analyze_user, analyze_device
main_bp = Blueprint("main", __name__)


@main_bp.route('/analyze_api', methods=['GET', 'POST'])
def analyze_api():
    # Simulated user_id, device_id
    user_id = random.randint(1, 1000)
    device_id = random.randint(1, 1000)
    data = get_all_data(user_id, device_id)
    analyze_user_data = analyze_user(data['user_data'])
    analyze_device_data = analyze_device(data['device_data'])
    result = {
        "time": time.time(),
        "analyze_user_data": analyze_user_data,
        "analyze_device_data": analyze_device_data
    }
    return jsonify(result)
