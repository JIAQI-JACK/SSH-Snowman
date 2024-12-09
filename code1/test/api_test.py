# encoding=utf8
# author: Qian wu
# create_time: 2024/12/4 11:19
# file: api_test.py
import requests

# I use the Python requests library to test services and print the result 
for i in range(1000):
    r = requests.post('http://127.0.0.1:10052/api/main/analyze_api')
    print(r.text)