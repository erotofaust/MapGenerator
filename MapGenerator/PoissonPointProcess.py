import numpy as np
import random

def terrainMaker(map_size_x, map_size_y, lamb):
    poisson = np.random.poisson(lamb, map_size_x*map_size_y).reshape(map_size_x, map_size_y)
    map_terrain = np.zeros((map_size_x, map_size_y))
    
    for n in range(0,map_size_x):
        for m in range(0, int(map_size_y/2)-n%2):
            tic = poisson[n, 2*m+n%2]
            if tic > 0:
                for x in range(-3*tic,3*tic):
                    for y in range(-3*tic,3*tic):
                        try:
                            prob = random.random()
                            if prob < 0.1:
                                map_terrain[n + x, 2*m+n%2 + 2*y] = 5
                            elif prob < 0.15:
                                map_terrain[n + x, 2*m+n%2 + 2*y] = random.choice([5, 15])                          
                                
                        except:
                            pass
            else:
                pass
    
            
            
    return map_terrain

