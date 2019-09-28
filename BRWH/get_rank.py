from BRWH.util import *
import operator
# client = clickhouse_client()


def get_rank(k=15):
    # client.execute('CREATE TABLE users (Name String, Follower String) ENGINE = Log')
    # users = client.execute('SELECT * FROM users')

    # global usr_lst, repo_cnt, follower_lst, other_lang, repo_cnt, pr_score, avatar
    df = csv_load()
    score_dct = {}

    for tmp_idx in range(df.shape[0]):
        cur_usr = df.loc[tmp_idx]
        tmp_score = cur_usr.Follower + cur_usr.pagerank_score
        score_dct[cur_usr.Name] = (int(tmp_score), cur_usr.Follower, int(cur_usr.pagerank_score), cur_usr.repo_cnt, cur_usr.avatar_url, cur_usr.other_lang)
    #print(score_dct)
    # return

    #for tmp_name in :
    #    tmp_score = follower_lst[tmp_idx] + pr_score[tmp_idx]
    #    score_dct[tmp_name] = (tmp_score, follower_lst[tmp_idx], pr_score[tmp_idx], repo_cnt[tmp_idx], avatar[tmp_idx], other_lang[tmp_idx])

    sorted_x = sorted(score_dct.items(), key=operator.itemgetter(1))[::-1][:k]
    # print(sorted_x)
    res = []

    for tmp_name, tmp_info in sorted_x:
        res.append({})
        res[-1]['name'] = tmp_name
        res[-1]['score'],\
            res[-1]['follower'],\
            res[-1]['pr_score'],\
            res[-1]['repo'],\
            res[-1]['avatar_url'],\
            res[-1]['other_lang'] = tmp_info
        res[-1]['cat'] = 'user'
        res[-1]['url'] = "https://www.github.com/"+tmp_name
    return res
