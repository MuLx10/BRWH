import json
f = open('./data/stats.json','r')
d = json.load(f)
f.close()

from copy import deepcopy as cp
newd = {"name":"", 
        "img": "https://placehold.it/100x100/11ff99",
        "children": []
        }
 
data = cp(newd)
data["name"] = "L"
#from tqdm import tqdm
for i in d[:10]:
    l, lc,rc = i['language'], i['license'],i['repo_cnt']
    #print(data)
    rcd = cp(newd)
    rcd['name'] = i['repo_cnt']
    if len(data['children']) < 1:
        ld = cp(newd)
        ld['name']=l
        ld['children'].append(rcd)
        lcd = cp(newd)
        lcd['name'] = lc
        lcd['children'].append(ld)
    for x in data['children']:
        if x['name'] == lc:
            for y in x['children']:
                if y['name'] == l:
                    ld = y
                else:
                    ld = cp(newd)
                    ld['name'] = l
            ld['children'].append(rcd)
            lcd = x
        else:
            lcd = cp(newd)
            lcd['name'] = lc
        lcd['children'].append(ld)
    data['children'].append(lcd)
#print(data)

f = open('./data/tree-data.json','w')
json.dump(data, f)
f.close()