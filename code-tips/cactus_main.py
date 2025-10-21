import navigation
import farm_utils

n = get_world_size()

def sort_line(start_x, start_y, direction):
	navigation.goto_naive(start_x, start_y)
	for i in range(n):
		navigation.goto_naive(start_x, start_y)
		swap_count = 0
		for j in range(n - 1 - i):
			if measure() > measure(direction):
				swap_count += 1
				swap(direction) 
			move(direction)
		if swap_count == 0:
			break
			
while True:			
	clear()
	farm_utils.plant_all(Entities.Cactus) 
		
	
	for i in range(n):
		sort_line(i, 0, North)
	
	for i in range(n):
		sort_line(0, i, East)
	
	harvest()