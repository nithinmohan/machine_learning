
import numpy as np
import random
import matplotlib.pyplot as plt

def exp():
	def get_random_point():
			return [random.uniform(-1,1),random.uniform(-1,1)]

	def t_creator(polynomial):
			def t(random_point):
				return sign(polynomial(random_point[0])-random_point[1])
			return t

	def sign(num):
			if num>0:
				return 1
			else:
				return -1

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


	def eq(v1,v2):
		if(v1!=v2):
			return 1;
		return 0;


	p1=get_random_point()
	p2=get_random_point()
	coefficients = np.polyfit(p1, p2, 1)
	polynomial = np.poly1d(coefficients)
	all_points=[]
	for i in range(0,100):
		temp_point=get_random_point()
		temp_point.append(1)
		all_points.append(temp_point)

	t=t_creator(polynomial);

	y=[t(x) for x in all_points]

	y_matrix=np.array([y]).T
	x_matrix = np.array(all_points)
	g=np.linalg.pinv(x_matrix).dot(y_matrix)
	coefficients2 =h_to_coefficient(g.T[0])
	polynomial2 = np.poly1d(coefficients2)
	g=t_creator(polynomial2)

	all_points2=[]
	for i in range(0,1000):
		temp_point=get_random_point()
		temp_point.append(1)
		all_points2.append(temp_point)
	return sum([eq(t(x),g(x)) for x in all_points2])/float(len(all_points2))




	# draw_line(polynomial2)
	# draw_line(polynomial) 

	# colors = [get_color_for_point(t,point) for point in all_points]
	# # spliting all points to two array as size argument has to be 3rd
	# a=zip(*all_points)
	# plt.scatter(a[0],a[1],s=20, color=colors)

	# axes = plt.gca()
	# axes.set_xlim([-1,1])
	# axes.set_ylim([-1,1])
	# plt.show() 

print sum([exp() for x in range(0,1000)])/1000.0