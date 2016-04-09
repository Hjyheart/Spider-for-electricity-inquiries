# -*- coding:UTF-8 -*-
import json

OUT_POS = "//Users//hongjiayong//PycharmProjects//电费查询//information.json"

information = []
information.append({'drlouming':'',
                    'drceng':'',
                    'DropDownList1':'',
                    'txt_fangjian':'',
                    'name':'',
                    'email':'',
                    'port':'2'})
information.append({'drlouming':'',
                    'drceng':'',
                    'drfangjian':'',
                    'name':'',
                    'email':'',
                    'port':'1'})
jsonData = json.loads(json.dumps(information))
with open(OUT_POS, 'w') as f:
    json.dump(jsonData, f)
    f.close()

with open(OUT_POS, 'r') as f:
    jsonData = json.load(f)
    f.close()
