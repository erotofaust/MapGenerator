import numpy as np
import random

def tileMaker(map_size_x, map_size_y, grass_prob, cellular_iter_num):
#    map_size_x = 100
#    map_size_y = 100
#    grass_prob = 0.4
#    cellular_iter_num = 5
 
    map_tile = np.full((map_size_x, map_size_y),-1)
    for n in range(0, map_size_x):
        for m in range(0, int(map_size_y/2)-n%2):
            a = random.random()
            if a < grass_prob :
                map_tile[n,2*m+n%2] = 0
                #grass tile
            else :
                map_tile[n,2*m+n%2] = 1
                #water tile

    # 랜덤으로 초기 지형값 세팅
    
    
    for i in range(0, cellular_iter_num):
        for n in range(0, map_size_x):
            for m in range(0, int(map_size_y/2)-n%2):
                try:
                    threshold = [map_tile[n, 2*m+n%2+2], map_tile[n+1, 2*m+n%2+1], map_tile[n+2, 2*m+n%2],
                                 map_tile[n-1, 2*m+n%2+1], map_tile[n, 2*m+n%2], map_tile[n+1, 2*m+n%2-1],
                                 map_tile[n-2, 2*m+n%2], map_tile[n-1, 2*m+n%2-1], map_tile[n, 2*m+n%2-2]]
                    if sum(threshold) <= 4:
                        map_tile[n, 2*m+n%2] = 0
                except:
                    map_tile[n, 2*m+n%2] = 0
                
        try:
            if map_tile[n,2*m+n%2] == 1:
                check = [map_tile[n+1, 2*m+n%2+1], map_tile[n-1, 2*m+n%2+1], map_tile[n+1, 2*m+n%2-1], map_tile[n-1, 2*m+n%2-1]]
                if sum(check) == 0:
                    map_tile[n,2*m+n%2] = 0
                elif sum(check) == 1:
                    map_tile[n,2*m+n%2] = 0
                elif sum(check) == 2:
                    if map_tile[n+1, 2*m+n%2+1] == 1 and map_tile[n-1, 2*m+n%2-1] == 1:
                        map_tile[n,2*m+n%2] = 0
                    elif map_tile[n-1, 2*m+n%2+1] == 1 and map_tile[n+1, 2*m+n%2-1] == 1:
                        map_tile[n,2*m+n%2] = 0
                elif sum(check) == 3:
                    if map_tile[n+1, 2*m+n%2+1] == 0:
                        map_tile[n, 2*m+n%2-2] = 1
                        map_tile[n-2, 2*m+n%2] = 1
                    elif map_tile[n-1, 2*m+n%2+1] == 0:
                        map_tile[n+2, 2*m+n%2] = 1
                        map_tile[n, 2*m+n%2-2] = 1
                    elif map_tile[n+1, 2*m+n%2-1] == 0:
                        map_tile[n, 2*m+n%2+2] = 1
                        map_tile[n-2, 2*m+n%2] = 1
                    elif map_tile[n-1, 2*m+n%2-1] == 0:
                        map_tile[n, 2*m+n%2+2] = 1
                        map_tile[n+2, 2*m+n%2] = 1                         
                elif sum(check) == 4:
                    map_tile[n, 2*m+n%2+2] = 0
                    map_tile[n+2, 2*m+n%2] = 0
                    map_tile[n-2, 2*m+n%2] = 0
                    map_tile[n, 2*m+n%2-2] = 0
                    temp = random.choice([0,0,1,1,2])
                    if temp == 0:
                        pass
                    elif temp == 1:
                        temp = random.choice([1,2,3,4])
                        if temp == 1:
                            map_tile[n, 2*m+n%2+2] = 0
                        elif temp == 2:
                            map_tile[n+2, 2*m+n%2] = 0
                        elif temp == 3:
                            map_tile[n-2, 2*m+n%2] = 0
                        elif temp == 4:
                            map_tile[n, 2*m+n%2-2] = 0
                    elif temp == 2:
                        temp = random.choice([1,2])
                        if temp == 1:
                            map_tile[n+2, 2*m+n%2] = 0
                            map_tile[n-2, 2*m+n%2] = 0
                        elif temp == 2:
                            map_tile[n, 2*m+n%2+2] = 0
                            map_tile[n, 2*m+n%2-2] = 0
        
        
        except: 
            map_tile[n,2*m+n%2] = 0
                    
    return map_tile

def snowMaker(map_size_x, map_size_y, map_tile, snow_size):
    snow_point1 = [int(map_size_x/2), int(map_size_y/2)]
    snow_point2 = [int(map_size_x/5), int(map_size_y/5)]
    snow_point3 = [int(map_size_x/5*4), int(map_size_y/5)]
    snow_point4 = [int(map_size_x/5), int(map_size_y/5*4)]
    snow_point5 = [int(map_size_x/5*4), int(map_size_y/5*4)]
    
    print(snow_point1)
    print(snow_point2)
    print(snow_point3)
    print(snow_point4)
    print(snow_point5)
    
    for n in range(0, map_size_x):
        for m in range(0, int(map_size_y/2)-n%2):
            if [n, 2*m+n%2]== snow_point1 or [n, 2*m+n%2]== snow_point2 or [n, 2*m+n%2]== snow_point3 or [n, 2*m+n%2]== snow_point4 or [n, 2*m+n%2]== snow_point5 :
                for k in range(1, snow_size+1):
                    for l in range(0,k):
                        if k == snow_size:
                            if l == 0:
                                map_tile[n ,2*m+n%2-k+2*l+1] = 3009
                            elif l == k-1:
                                map_tile[n ,2*m+n%2-k+2*l+1] = 3001
                            else:
                                map_tile[n ,2*m+n%2-k+2*l+1] = 3005
                                    
                        elif k == 1:
                            map_tile[n - (snow_size-k),2*m+n%2-k+2*l+1] = 3003
                            map_tile[n + (snow_size-k),2*m+n%2-k+2*l+1] = 3007
                        else:
                            if l == 0:
                                map_tile[n - (snow_size-k),2*m+n%2-k+2*l+1] = 3006
                                map_tile[n + (snow_size-k),2*m+n%2-k+2*l+1] = 3008
                            elif l == k-1:
                                map_tile[n - (snow_size-k),2*m+n%2-k+2*l+1] = 3002
                                map_tile[n + (snow_size-k),2*m+n%2-k+2*l+1] = 3004
                            else:
                                map_tile[n - (snow_size-k),2*m+n%2-k+2*l+1] = 3005
                                map_tile[n + (snow_size-k),2*m+n%2-k+2*l+1] = 3005
                          

    return map_tile
    
    