import BRWH.usr_repos as user_repos
import BRWH.usr as usr

repos_company = {}
num_usr = len(usr.usr_lst)

for userid in range(num_usr):
    if (usr.company_lst[userid] != 'none'):
        for repos in user_repos.userid_repos[userid]:
            repos_company.setdefault(repos,[]).append(usr.company_lst[userid])


recomand_company = {}
for userid in range(num_usr):
    tmp_user_company = {}
    count = 0
    for repos in user_repos.userid_repos[userid]:
        if(repos in repos_company.keys()):
            for cmpy in repos_company[repos]:
                tmp_user_company[cmpy]= tmp_user_company.get(cmpy, 0)+1
                count+=1

    if(count!=0):
        for company in tmp_user_company.keys():
            if(usr.company_lst[userid]!=company):
                recomand_company.setdefault(company,[]).append([userid, ((float)(tmp_user_company[company]))/((float)(count))])

for company in recomand_company.keys():
    recomand_company[company].sort(reverse = True, key = lambda x:x[1])

usr_url = {}
with open("./data/usr.csv",'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        linelist = line.split(',')
        usr_url[linelist[0]] = linelist[-2]


import pandas as pd


#f = open("./data/company_recommend.txt",'w')

data = []
for company in recomand_company.keys():
    d = {"name":company.upper(), "item":[]}
    tmp = "\n'"+company+"',s ["
    for userid, score in recomand_company[company][:9]:
        e = {"name":usr.usr_lst[userid],"score":int(100*score), "img":usr_url[usr.usr_lst[userid]], "url":"https://www.github.com/"+usr.usr_lst[userid]}
        d['item'].append(e)
    data.append(d)
        
    #    tmp+='[{} , {:.2f}, {}],'.format(usr.usr_lst[userid],score, usr_url[usr.usr_lst[userid]])
    #tmp = tmp[:-1]+"]"
    #f.writelines(tmp)

#f.close()

def get_recomend():
    return data