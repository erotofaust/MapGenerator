import numpy as np

def getSize(input_x, input_y):   
    
    map_x_max = int(input_x) - int(input_x) % 2
    map_y_max = int(input_y) - int(input_y) % 2
    
    # map_x_max, map_y_max는 반드시 짝수여야 함
    
    print("맵의 x축 개수는 %d" %map_x_max)
    print("맵의 y축 개수는 %d" %int(map_y_max/2))

    map_size = np.array([map_x_max, map_y_max])
    
    # map의 사이즈 지정
    # 이때 좌표계 특성에 따라 총 타일 수는 약 map_x_max*map_y_max*0.5

    return map_size