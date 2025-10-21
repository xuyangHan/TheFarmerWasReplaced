def goto_naive(x_target, y_target):
	n = get_world_size()
	curX = get_pos_x()
	curY = get_pos_y()

	# Calculate horizontal distance and direction (shortest path)
	dx = (x_target - curX) % n

	# If dx <= n/2, move East dx steps; otherwise move West (n - dx) steps
	if dx <= n // 2:
		steps_x = dx
		dirX = East
	else:
		steps_x = n - dx
		dirX = West

	# Calculate vertical distance and direction (shortest path)
	dy = (y_target - curY) % n

	# If dy <= n/2, move North dy steps; otherwise move South (n - dy) steps
	if dy <= n // 2:
		steps_y = dy
		dirY = North
	else:
		steps_y = n - dy
		dirY = South

	# Move step by step, alternating between X and Y directions
	while steps_x > 0 or steps_y > 0:
		# Prioritize the direction with more remaining steps
		if steps_x >= steps_y and steps_x > 0:
			move(dirX)
			steps_x -= 1
		elif steps_y > 0:
			move(dirY)
			steps_y -= 1
		