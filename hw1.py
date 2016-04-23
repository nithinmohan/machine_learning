import numpy as np
import random
import matplotlib.pyplot as plt
def exp():
	def get_random_point():
		return np.array([random.uniform(-1,1),random.uniform(-1,1)])

	def t_creator(polynomial):
		def t(random_point):
			return sign(polynomial(random_point[0])-random_point[1])
		return t

	def h_to_coefficient(h):
		return np.array([-h[0]/h[1],-h[2]/h[1]])

	def draw_line(polynomial):
		x = np.array(range(-1,2))  
		y = polynomial(x)
		plt.plot(x, y)

	def get_color_for_point(t,point):
		if(t(point)==1):
			return'r'
		else:
			return'g'

	def sign(num):
		if num>0:
			return 1
		else:
			return -1

	p1=get_random_point()
	p2=get_random_point()
	coefficients = np.polyfit(p1, p2, 1)
	polynomial = np.poly1d(coefficients)

	t=t_creator(polynomial)

	all_points=[]
	for i in range(0,100):
		temp_point=get_random_point()
		temp_point=np.append(temp_point,1)
		all_points.append(temp_point)

	h=np.array([0,0,0])

	for n in range(1,50):
		for point in all_points:
			if(sign(np.inner(h,point))!=t(point)):
				h=h+point*t(point)
				break
		else:
			break
	#number of iteration to converge
	# return n

	#drawing
	polynomial2 = np.poly1d(h_to_coefficient(h))
	draw_line(polynomial2)
	draw_line(polynomial) 
	colors = [get_color_for_point(t,point) for point in all_points]
	# spliting all points to two array as size argument has to be 3rd
	a=zip(*all_points)
	plt.scatter(a[0],a[1],s=20, color=colors)

	axes = plt.gca()
	axes.set_xlim([-1,1])
	axes.set_ylim([-1,1])
	plt.show() 

	#error analysis
	# error_count=0
	# count/100.0


exp()
# sum=0
# for n in range(0,100000):
# 	sum=sum+exp()
# print sum/100000.0