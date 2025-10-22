# 🌱 Solving Maze and Dinosaur in *The Farmer Was Replaced*

## Recap

If you’ve been following along, you already know that [**The Farmer Was Replaced**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) isn’t just a cozy farming simulator — it’s a visual sandbox for **learning automation and programming logic**.

So far, we’ve written scripts that let our drone plant crops efficiently — arranging trees, cactus, and pumpkins in smart, algorithmic patterns to maximize yield.

![Sorted Cactus](../assets/sorted_cactus.jpg)

In this post, we’ll move beyond farming and explore new puzzles that push our logical thinking even further — starting with the **Dinosaur Hat challenge**, and later venturing into **maze solving**.

---

## 🦖 Dinosaur Mode

In this puzzle, you can equip the **Dinosaur Hat** to transform into a dinosaur with a growing tail:

```python
change_hat(Hats.Dinosaur_Hat)
```

Your goal? Eat the randomly spawned **apple** on the farm.

Just like in the classic **Snake** game, each apple you eat makes your tail grow longer — and speeds up your movement. The rule is simple but unforgiving:
👉 **You can’t collide with your own tail.**

The longer your tail grows, the higher your score — or in this case, the more rewards you earn:

> Each full round gives you *n² × Items.Bone* at harvest.

### 🧩 The Idea: A Safe, Predefined Path

When you first encounter this challenge, a simple but powerful idea might come to mind:

> Instead of chasing the apple directly, what if the dinosaur always follows a **pre-defined safe route** that covers the entire farm?

That’s exactly the concept behind a **[Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path)** — a path that visits every tile on a grid exactly once.

In our case, we don’t need to compute such a path dynamically (which is a hard algorithmic problem).
We can design one manually — a repeating, snake-like traversal pattern that guarantees full coverage.

![Long Dinosaur](../assets/long_dinosaur.jpg)

### 🧠 Designing the Traversal Pattern

Let’s make this concrete by setting a manageable grid size:

```python
set_world_size(8)
```

A full traversal of a large 32×32 field could take over 30 minutes — so an 8×8 grid makes experimentation much faster. (Though yes, a full 32×32 sweep can yield *millions of bones* if you’re patient!)

Here’s the plan for our route:

* The dinosaur moves **column by column**, alternating directions.
* **Even-numbered columns** (0, 2, 4, …) go all the way **up to the top**.
* **Odd-numbered columns** (1, 3, 5, …) come **down to the bottom − 1**, leaving the very bottom row free, making that open bottom row acts as a **return path** to the origin (0, 0).
* When you reach the rightmost edge, move along the bottom back home.

This creates a **looping, Hamiltonian-style route** that never crosses itself — a perfect safety net for our growing dinosaur.

### 🧾 Code Outline

```python
import navigation

clear()

change_hat(Hats.Dinosaur_Hat)
n = get_world_size()

while True:
	for x in range(n):
		# decide vertical target for this column
		if x % 2 == 0:
			target_y = n - 1   # even column index: go to the very top
		else:
			target_y = 1       # odd column index: go down but leave row 0 free
	
		# move vertically until we reach target_y
		while get_pos_y() != target_y:
			if target_y > get_pos_y():
				navigation.dinosaur_safe_move(North)
			else:
				navigation.dinosaur_safe_move(South)
	
		# after finishing the column, move east if there are more columns
		if x < n - 1:
			move(East)
	
	# finished scanning all columns
	# return to origin using the open bottom row y=0
	# first move down to y=0 (if not already there)
	while get_pos_y() != 0:
		navigation.dinosaur_safe_move(South)
	
	# then move west back to x=0
	while get_pos_x() != 0:
		navigation.dinosaur_safe_move(West)
	
	# now at (0,0)
```

``` python
# navigation.py
def dinosaur_safe_move(direction):
	# Move in the given direction if possible.
	# If movement is blocked, temporarily change hats as a workaround.
	
	if can_move(direction):
		move(direction)
	else:
		change_hat(Hats.Carrot_Hat)
		change_hat(Hats.Dinosaur_Hat)
```

This deterministic route ensures the dinosaur always has a valid move, regardless of where apples spawn.

### 🔍 Next Steps

This strategy is reliable but not optimal — especially on larger farms.
Possible improvements include:

* **Adaptive pathing:** Instead of always traversing the entire field, detect where the next apple will spawn and shorten the path dynamically.
* **Early turns:** If you can confirm there’s a clear path back home, you can allow the dinosaur to “cut corners” safely.

We’ll revisit these optimizations later. For now, enjoy watching your pixelated reptile devour apples, grow endlessly, and harvest a *mountain of bones*. 🦴

--- 

## 