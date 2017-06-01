#!/usr/bin/env python

from pixivpy3 import *
import json
import os
from datetime import datetime

api = PixivAPI()
with open('config.json', 'r') as f:  # config file location
    config = json.load(f)

download_path = config['download_path']


for user in range(len(config["username"])):
    api.login(config['username'][user], config['password'][user])
    last_fave_id = int(config['last_fave_id'][user])

    json_result = api.me_favorite_works()
    my_ids = json_result.response
    for my_id in my_ids:
        if (my_id.work.favorite_id <= last_fave_id):
            break
        url = my_id.work.image_urls['large']
        for p in range(my_id.work.page_count):
            page_url = url[:-5] + str(p) + url[-4:]
            api.download(page_url, path=download_path)
            print('[' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] \033[1;32;40m::\033[0;37;40m ' + 'Downloaded [ Fave ID: ' +
                  str(my_id.work.favorite_id) + ' ID: ' + str(my_id.work.id) + ' Page: ' + str(p) + ' ] for user ' + config['username'][user])

    config['last_fave_id'][user] = str(my_ids[0].work.favorite_id)

print('[' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') +
      '] \033[1;32;40m::\033[0;37;40m ' + 'End of new faves')
with open('config.json', 'w') as f:
    json.dump(config, f)
