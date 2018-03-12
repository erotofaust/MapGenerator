import random
import copy

def tilePostProcess(map_size_x, map_size_y, map_tile):

    map_tile_temp = copy.deepcopy(map_tile)
    for i in range(0,10):
        for n in range(0, map_size_x):
            for m in range(0, int(map_size_y/2)-n%2):
                try:
                    if map_tile[n,2*m+n%2] == 0:
                            map_tile_temp[n,2*m+n%2] = 1001
                    elif map_tile[n,2*m+n%2] == 1:
                        
                        threshold = [map_tile[n, 2*m+n%2+2], map_tile[n+1, 2*m+n%2+1], map_tile[n+2, 2*m+n%2],
                                 map_tile[n-1, 2*m+n%2+1], map_tile[n, 2*m+n%2], map_tile[n+1, 2*m+n%2-1],
                                 map_tile[n-2, 2*m+n%2], map_tile[n-1, 2*m+n%2-1], map_tile[n, 2*m+n%2-2]]
                        if sum(threshold) > 3000:
                            map_tile[n, 2*m+n%2] = 0

                        check = [map_tile[n+1, 2*m+n%2+1], map_tile[n-1, 2*m+n%2+1], map_tile[n+1, 2*m+n%2-1], map_tile[n-1, 2*m+n%2-1]]
                        if sum(check) == 0:
                            map_tile[n,2*m+n%2] = 0
                            map_tile_temp[n,2*m+n%2] = 1001
                        elif sum(check) == 1:
                            map_tile[n,2*m+n%2] = 0
                            map_tile_temp[n,2*m+n%2] = 1001
                        elif sum(check) == 2:
                            if map_tile[n+1, 2*m+n%2+1] == 1 and map_tile[n-1, 2*m+n%2+1] == 1:
                                map_tile_temp[n,2*m+n%2] = 2009
                            elif map_tile[n+1, 2*m+n%2+1] == 1 and map_tile[n+1, 2*m+n%2-1] == 1:
                                map_tile_temp[n,2*m+n%2] = 2003
                            elif map_tile[n-1, 2*m+n%2-1] == 1 and map_tile[n-1, 2*m+n%2+1] == 1:
                                map_tile_temp[n,2*m+n%2] = 2007
                            elif map_tile[n-1, 2*m+n%2-1] == 1 and map_tile[n+1, 2*m+n%2-1] == 1:
                                map_tile_temp[n,2*m+n%2] = 2001
                        elif sum(check) == 3:
                            if map_tile[n+1, 2*m+n%2+1] == 0:
                                map_tile_temp[n,2*m+n%2] = 2004
                            elif map_tile[n-1, 2*m+n%2+1] == 0:
                                map_tile_temp[n,2*m+n%2] = 2002
                            elif map_tile[n+1, 2*m+n%2-1] == 0:
                                map_tile_temp[n,2*m+n%2] = 2008
                            elif map_tile[n-1, 2*m+n%2-1] == 0:
                                map_tile_temp[n,2*m+n%2] = 2006                      
                        elif sum(check) == 4:
                            check_2 = [map_tile[n, 2*m+n%2+2], map_tile[n+2, 2*m+n%2], map_tile[n-2, 2*m+n%2], map_tile[n, 2*m+n%2-2]]
                            if sum(check_2) == 4:
                                map_tile_temp[n,2*m+n%2] = 2005
                            elif sum(check_2) == 3:
                                if map_tile[n, 2*m+n%2+2] == 0:
                                    map_tile_temp[n,2*m+n%2] = 2012
                                elif map_tile[n+2, 2*m+n%2] == 0:
                                    map_tile_temp[n,2*m+n%2] = 2015
                                elif map_tile[n-2, 2*m+n%2] == 0:
                                    map_tile_temp[n,2*m+n%2] = 2013
                                elif map_tile[n, 2*m+n%2-2] == 0:
                                    map_tile_temp[n,2*m+n%2] = 2010
                            elif sum(check_2) == 2:
                                if map_tile[n, 2*m+n%2+2] == 0:
                                    map_tile_temp[n,2*m+n%2] = 2014
                                elif map_tile[n, 2*m+n%2+2] == 1:
                                    map_tile_temp[n,2*m+n%2] = 2011
                            
                        
                        
                        if sum(check) == 2:
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
                        
                        threshold = [map_tile[n, 2*m+n%2+2], map_tile[n+1, 2*m+n%2+1], map_tile[n+2, 2*m+n%2],
                                 map_tile[n-1, 2*m+n%2+1], map_tile[n, 2*m+n%2], map_tile[n+1, 2*m+n%2-1],
                                 map_tile[n-2, 2*m+n%2], map_tile[n-1, 2*m+n%2-1], map_tile[n, 2*m+n%2-2]]
                        if sum(threshold) > 3000:
                            map_tile[n, 2*m+n%2] = 0
                        
                    elif map_tile[n,2*m+n%2] > 3000:
                        pass
                        

                except:
                    map_tile_temp[n,2*m+n%2] = 1001
                
   
                if map_tile_temp[n,2*m+n%2] == 1:
                    print("there's some error")
                    map_tile[n,2*m+n%2] = 0
                
    
    return map_tile_temp
    

        

def terrainPostProcess(map_size_x, map_size_y, terrain_id, map_terrain):
    for n in range(0, map_size_x):
        for m in range(0, int(map_size_y/2)-n%2):
            if map_terrain[n,2*m+n%2] == 5:
                map_terrain[n,2*m+n%2] = random.choice(terrain_id)
            elif map_terrain[n,2*m+n%2] == 15:
                map_terrain[n,2*m+n%2] = random.choice(terrain_id)
    
    return map_terrain


def deleteTerrain(map_size_x, map_size_y, map_tile, map_terrain):
    for n in range(0, map_size_x):
        for m in range(0, int(map_size_y/2)-n%2):
            if map_tile[n,2*m+n%2]//1000 == 2 or map_tile[n,2*m+n%2]//1000 == 3:
                map_terrain[n,2*m+n%2] = 0
    return map_terrain
