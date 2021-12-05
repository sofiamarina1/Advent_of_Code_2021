def increased_measurements():
	f = open('depths.txt', 'r')
	x = len(f.readlines())

	file = open('depths.txt', 'r')
	depth = file.readline()
	#print("depth1 =", depth)

	increased = 0
	for i in range(x):
		new_depth = file.readline()
		print("old_depth =" ,depth)
		print("new_depth =" ,new_depth)
		if new_depth > depth:
			print("increase!")
			increased = increased + 1
		depth = new_depth
	print(increased)

increased_measurements()



