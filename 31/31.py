def calc_sum(p1, p2, p5, p10, p20, p50, p100):
	s = p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100
	return s


ways = 1
for p100 in range(200//100 + 1):
	for p50 in range(200//50 + 1):
		if 50*p50 + p100 > 200: break

		for p20 in range(200//20 + 1):
			if 20*p20 + 50*p50 + p100 > 200: break

			for p10 in range(200//10 + 1):
				if 10*p10 + 20*p20 + 50*p50 + p100 > 200: break

				for p5 in range(200//5 + 1):
					if 5*p5 + 10*p10 + 20*p20 + 50*p50 + p100 > 200: break

					for p2 in range(200//2 + 1):
						if 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + p100 > 200: break

						for p1 in range(200 + 1):
							s = calc_sum(p1, p2, p5, p10, p20, p50, p100)
							if s > 200: break

							if s == 200: ways += 1


print(ways)