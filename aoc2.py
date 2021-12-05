import numpy as np

def increased_measurements():
	f = open('depths.txt', 'r')
	x = len(f.readlines())

	fi = open('depths.txt', 'r')
	#depth = file.readline()
	#print("depth1 =", depth)
	depths = []
	for i in range(x):
		depths.append(int(fi.readline()))

	file = open('depths.txt', 'r')

	increased = 0
	sums = np.zeros(len(depths))
	for i in range(len(depths)):
		sums[i] = sums[i] + depths[i]
		if i-1 >= 0: #and len(depths) - i >= 5:
			sums[i-1] = sums[i-1] + depths[i]
		if i-2 >= 0: #and len(depths)-i >= :
			sums[i-2] = sums[i-2] + depths[i]

	old_sum = 0
	for sum in sums:
		print('old_sum = ' ,old_sum)
		print('new_sum = ' ,sum)
		if sum > old_sum:
			increased = increased + 1
			print('increased!')
		old_sum = sum

	"""for i in range(x):
		if (i + 1) % 3 == 0:
			new_sum = new_sum + int(file.readline())
			print("old_sum", sum)
			print("new_sum", new_sum)
			if new_sum > sum:
				print("increased!")
				increased = increased + 1
			sum = new_sum
			new_sum = 0
		else:
			#print(type(file.readline()))
			new_sum = new_sum + int(file.readline())

		new_depth = file.readline()
		print("old_depth =" ,depth)
		print("new_depth =" ,new_depth)
		if new_depth > depth:
			print("increase!")
			increased = increased + 1
		depth = new_depth"""
	print(increased)
	#1249 too high

increased_measurements()



