import navigation
		
n = get_world_size()

def wait_for_all_drones(drones_set):
	while len(drones_set) > 0:
		removed_drones = []
		for drone in drones_set:
			if has_finished(drone):
				removed_drones.append(drone)
		for removed_drone in removed_drones:
			drones_set.remove(removed_drone)

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

# drone task 1
def drone_plant_and_sort_row():
	(start_x, start_y) = (get_pos_x(), get_pos_y())
	for i in range(n):
		if get_ground_type() == Grounds.Grassland:
			till()
		harvest()
		plant(Entities.Cactus)
		move(East)
	sort_line(start_x, start_y, East)

# drone task 2
def drone_sort_line():
	sort_line(get_pos_x(), get_pos_y(), North)
	

while True:
	navigation.goto_naive(0, 0)
	# each drone plant and sort a row first
	drones = set()
	for i in range(n):
		drone = spawn_drone(drone_plant_and_sort_row)
		if not drone:
			drone_plant_and_sort_row() # main drone to do the last row
		else:
			drones.add(drone)
		move(North)

	# wait all done before next task
	navigation.goto_naive(0, 0)
	wait_for_all_drones(drones)
		
	# each drone plant and sort a column
	for i in range(n):
		drone = spawn_drone(drone_sort_line)
		if not drone:
			drone_sort_line()
		else:
			drones.add(drone)
		move(East)
		
	# wait all done before harvest
	wait_for_all_drones(drones)
	harvest()