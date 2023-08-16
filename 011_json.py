# -*- coding:utf-8 -*-
import json

import json

data = [{
    'name': ' 王伟 ',
    'gender': ' 男 ',
    'birthday': '1992-10-18'
}]

print(type(json.dumps(data)))

with open('data.json','w+', encoding='utf-8') as f:
 f.write(json.dumps(data, indent=2, ensure_ascii=False))
