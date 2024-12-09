# encoding=utf8
# author: Jiaqi Tang
# create_time: 2024/12/3 9:26
# file: data_collection.py

import json
import random
import requests


# Simulate data collection from SSH devices (in practical applications, it needs to be replaced with a real interface)
def collect_device_data(device_id):
    '''
    :param device_id: device id
    :return: json data
    '''
    # Simulate data use random
    device_status = random.choice(["online", "offline"])
    usage_time = random.randint(0, 100)
    environment_data = {
        "temperature": random.uniform(20, 30),
        "humidity": random.uniform(40, 60)
    }
    data = {
        "device_id": device_id,
        "device_status": device_status,
        "usage_time": usage_time,
        "environment_data": environment_data
    }
    return data


def get_data_from_ssh_cloud(user_id):
    # Because we don't have a real SSH cloud data center, we use test.com/get_data simulation
    ssh_cloud_data_url = 'https://www.test.com/get_data'
    try:
        r = requests.post(ssh_cloud_data_url, timeout=1,json={'user_id': user_id})
    except:
        pass
    # Simulate data energy_use as user's electricity consumption
    data = {'user_id': user_id,
            'usage_time': random.randint(20, 30),
            'energy_use': random.random() * 100}
    return data


def collect_user_data(user_id):
    '''
    :param user_id: user_id
    :return: json data
    '''
    data = get_data_from_ssh_cloud(user_id)
    return data


def get_all_data(user_id, device_id):
    device_data = collect_device_data(device_id)
    user_data = collect_user_data(user_id)
    return {'device_data': device_data,
            'user_data' : user_data}
