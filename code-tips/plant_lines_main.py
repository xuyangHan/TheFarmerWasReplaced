import farm_utils

clear()

# plant in 12 * 12 grid
crops = [
    Entities.Sunflower, 
    Entities.Cactus, 
    Entities.Cactus, 
    Entities.Carrot, 
    Entities.Carrot, 
    Entities.Pumpkin, 
    Entities.Pumpkin, 
    Entities.Pumpkin, 
    Entities.Bush, 
    Entities.Bush, 
    Entities.Grass, 
    Entities.Grass
]

farm_utils.plant_columns(crops)

while True:
    for crop in crops:
        farm_utils.farm_column(crop)
        move(East)