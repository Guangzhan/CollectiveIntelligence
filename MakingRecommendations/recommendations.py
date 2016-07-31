# *-* coding:utf-8 *-*
# author:Guangzhan

import math
import numpy as np
critics = {'Lisa Rose': {'Lady in the water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just my Luck': 3.0, 'Superman Back': 3.5,
                         'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},

           'Gene Syemour': {'Lady in the water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just my Luck': 1.5, 'Superman Back': 5.0,
                            'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},

           'Michael Phillips': {'Lady in the water': 3.0, 'Snakes on a Plane': 3.0,
                                'Superman Back': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on  Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Back': 4.0,
                            'You, Me and Dupree': 2.5}
           }


# 返回两个用户之间的基于距离的相似度评价
def sim_distance(prefs, user1, user2):

    dic = {}
    for item in prefs[user1]:
        if item in prefs[user2]:
            dic[item] = 1
    print(dic)

    if len(dic) == 0:
        return 0
    # 欧式距离
    sum_of_squares = sum([math.pow(prefs[user1][item] - prefs[user2][item], 2) \
                          for item in prefs[user1] if item in prefs[user2]])
    return 1 / (1 + math.sqrt(sum_of_squares))


if __name__ == '__main__':
    distance = sim_distance(critics, 'Lisa Rose', 'Gene Syemour')
    print(distance)
