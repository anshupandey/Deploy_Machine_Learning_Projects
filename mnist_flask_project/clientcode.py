# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:19:30 2019

@author: anshu
"""

import requests
url = "http://127.0.0.1:5000"
data = {"image":open("sample_image.png","rb")}
response = requests.post(url,files=data)
print(response.content)