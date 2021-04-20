#!/usr/bin
# -*- coding:utf-8 -*-

import requests

# 查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url,params={'eid':'1'})
result = r.json()

# 断言 接口返回值
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "小米发布会"
assert result['data']['address'] == "水立方"
assert result['data']['start_time'] == "2019-07-10T10:00:00"











