import numpy as np
import random

def tileMaker(map_size_x, map_size_y):
    
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
        
    return map_tile