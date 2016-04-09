# -*- coding:UTF-8 -*-
import json

OUT_POS = "//Users//hongjiayong//PycharmProjects//电费查询//information.json"

information = []
information.append({'drlouming':'1',
                    'drceng':'4026',
                    'DropDownList1':'4029',
                    'txt_fangjian':'308',
                    'name':'欣颖',
                    'email':'502899772@qq.com',
                    'port':'2'})
information.append({'drlouming':'1',
                    'drceng':'2154',
                    'DropDownList1':'2286',
                    'txt_fangjian':'511',
                    'name':'俞灵',
                    'email':'540577189@qq.com',
                    'port':'2'})
information.append({'drlouming':'5',
                    'drceng':'4834',
                    'DropDownList1':'4845',
                    'txt_fangjian':'19519',
                    'name':'hjyheart',
                    'email':'764796124@qq.com',
                    'port':'2'})
information.append({'drlouming':'09',
                    'drceng':'0904',
                    'drfangjian':'090437',
                    'name':'小戴',
                    'email':'1093682075@qq.com',
                    'port':'1'})
information.append({'drlouming':'01',
                    'drceng':'0130',
                    'drfangjian':'013053',
                    'name':'夜晖',
                    'email':'1093682075@qq.com',
                    'port':'1'})
jsonData = json.loads(json.dumps(information))
with open(OUT_POS, 'w') as f:
    json.dump(jsonData, f)
    f.close()

with open(OUT_POS, 'r') as f:
    jsonData = json.load(f)
    f.close()