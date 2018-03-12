import MapSizeCheck as msize
import CellularAutomata as cauto
import PoissonPointProcess as ppp
import DataManager as dm
import PostProcess as post

#%%
def main(dataArray):
    
    print("start")
    input_x = int(dataArray[0])
    input_y = int(dataArray[1])
    terrain_count = int(dataArray[2])
    grass_prob = dataArray[3]
    cellular_iter_num = int(dataArray[4])
    lamb = dataArray[5]
    snow_size = dataArray[6]
    
    
    #맵의 사이즈를 정한다.
    map_size = msize.getSize(input_x, input_y)
    print("complete : map_size_detection")
    
    #선언되어 있는 타일 및 지형 ID를 읽어온다.
    
    terrain_id = dm.readTerrainData(terrain_count)
    print("complete : read tileId and terrainId")

    #셀룰러 오토마타를 이용해 물 지형과 땅 지형을 구분한다.

    map_tile = cauto.tileMaker(map_size[0], map_size[1], grass_prob, cellular_iter_num)
    map_tile = cauto.snowMaker(map_size[0], map_size[1], map_tile, snow_size)
    print("complete : tile making by cellularautomata")

    #CellularAutomata
    #포아송 프로세스를 통해 돌과 나무를 뿌린다.
    
    map_terrain = ppp.terrainMaker(map_size[0], map_size[1], lamb)
    print("complete : terrain making by poisson point process")

    #PoissonPointProcess
    #맵 후처리를 하고 ID를 매핑한다.
    map_tile_real = post.tilePostProcess(map_size[0], map_size[1], map_tile)
    map_terrain_real = post.terrainPostProcess(map_size[0], map_size[1], terrain_id, map_terrain)
    map_terrain_real = post.deleteTerrain(map_size[0], map_size[1], map_tile_real, map_terrain_real)
    print("complete : post processing")

    #엑셀 파일로 저장한다.
    #DataManager
    dm.writeMapData(map_size[0], map_size[1], map_tile_real, map_terrain_real)
    print("complete : save the file")
    

#%%
if __name__ == "__main__":
    input_x = 300
    input_y = 150
    terrain_count = 2
    grass_prob = 0.4
    cellular_iter_num = 5
    lamb = 0.1
    snow_size = 5
    
    
    #맵의 사이즈를 정한다.
    map_size = msize.getSize(input_x, input_y)
    print("complete : map_size_detection")
    
    #선언되어 있는 타일 및 지형 ID를 읽어온다.
    
    terrain_id = dm.readTerrainData(terrain_count)
    print("complete : read tileId and terrainId")

    #셀룰러 오토마타를 이용해 물 지형과 땅 지형을 구분한다.

    map_tile = cauto.tileMaker(map_size[0], map_size[1], grass_prob, cellular_iter_num)
    map_tile = cauto.snowMaker(map_size[0], map_size[1], map_tile, snow_size)
    print("complete : tile making by cellularautomata")

    #CellularAutomata
    #포아송 프로세스를 통해 돌과 나무를 뿌린다.
    
    map_terrain = ppp.terrainMaker(map_size[0], map_size[1], lamb)
    print("complete : terrain making by poisson point process")

    #PoissonPointProcess
    #맵 후처리를 하고 ID를 매핑한다.
    map_tile_real = post.tilePostProcess(map_size[0], map_size[1], map_tile)
    map_terrain_real = post.terrainPostProcess(map_size[0], map_size[1], terrain_id, map_terrain)
    map_terrain_real = post.deleteTerrain(map_size[0], map_size[1], map_tile_real, map_terrain_real)
    print("complete : post processing")

    #엑셀 파일로 저장한다.
    #DataManager
    dm.writeMapData(map_size[0], map_size[1], map_tile_real, map_terrain_real)
    print("complete : save the file")
    
