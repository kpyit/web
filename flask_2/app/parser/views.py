from flask import render_template, redirect, request, url_for, flash, jsonify
  
import requests
import os
from bs4 import BeautifulSoup #pip install beautifulsoup4
 
from . import parser
from .. import db
from ..models import User
 
from urllib.parse import urlparse

import threading 
from multiprocessing import Process, Manager
import time 

 
#  
PARENT_F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(PARENT_F, 'static', 'parsed_images')


def download_image_url(image_url, dict_u):
 
    start_time = time.time()
    response = requests.get(image_url)
    if response.status_code == 200:
        #  
        filename = os.path.basename(image_url) 
        with open(UPLOAD_FOLDER+'\\'+filename, "wb") as file:
            file.write(response.content)
    
    dict_u[filename] = {'image_url':image_url,
                        'filename':UPLOAD_FOLDER+filename,
                        'time':f"{time.time() - start_time:0.2f}",
                        'threds': 'multi'}

# http://127.0.0.1:5000/parser/get-images
@parser.route('/get-images', methods=['GET', 'POST'])
def form_get_images():
    return render_template('parser/get_images.html', form=None)

# /parser/parse-images 
# http://127.0.0.1:5000/parser/parse-images
@parser.route('/parse-images', methods=['GET', 'POST'])
def asunc_get_images():
    content_type = request.headers.get('Content-Type')  
    if request.is_json:     
        request_data = request.get_json() 
        site = request_data['url']
        # return jsonify({"status":200, "content":{}})  
        response = requests.get(site)
        url_parts = urlparse(site)
        base_URL = 'http://' + url_parts.hostname + '/'
        html_content = response.content
        
        soup = BeautifulSoup(html_content, "html.parser")
        
        image_tags = soup.find_all("img")
        # извлекаем адреса
        image_urls = [img["src"] for img in image_tags] 
        #цикл закачки  
        manager = Manager()
        dict_files_load = manager.dict()
        processes = []
         
        for image_url in image_urls:
            proc = Process(target=download_image_url, args=(base_URL + image_url, dict_files_load,))
            processes.append(proc)
            proc.start()
            
        for p in processes:
            p.join()
            
        simple_dict = dict_files_load.copy() 
        # отрпавка данных  
        # return jsonify({"status":response.status_code,"content":image_urls})  
        return jsonify({"status":response.status_code,"content":  simple_dict })  
    else:
        return jsonify({"status":"Content type is not supported."}) 
   
# curl -X POST -H "Content-type: application/json" -d "{\"name\" : \"John\", \"age\" : \"5\"}" "localhost:5000/string_example"