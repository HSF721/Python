i = 0
j = 0
k = 0
l = 0
time = 0
for i in xrange(1,5):
	for j in xrange(1,5):
		if j == i:
			continue
		for k in xrange(1,5):
			if k == j or k == i:
				continue
			for l in xrange(1,5):
				if l == k or l == j or l == i:
					continue
				num = i * 1000 + j * 100 + k * 10 + l
				time += 1
				print(num)
				print(time)
