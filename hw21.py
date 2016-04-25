import numpy as np
import random
#true=head
#false=tail
def ran01():
	return random.randint(0, 1)

def get_ran01_array():
	temp=[]
	for i in range(0,10):
		temp.append(ran01())
	return temp

def fill1000():
	temp=[]
	for i in range(0,1000):
		temp.append(get_ran01_array())
	return temp

def ratio_of_head(array):
	return sum(array)/10.0
def get_min_array(study_array):
	temp_ratio=1
	min_array=[]
	for array in study_array:
		if(temp_ratio>ratio_of_head(array)):
			temp_ratio=ratio_of_head(array)
			min_array=array
	return min_array
def exp():
	study_array=fill1000()
	v1=ratio_of_head(study_array[0])
	v2=ratio_of_head(study_array[random.randint(0,999)])
	v3=ratio_of_head(get_min_array(study_array))
	return v1,v2,v3

def final_exp():
	count_v1=0
	count_v2=0
	count_v3=0
	exp_count=1000
	for i in range(0,exp_count):
		temp_v1,temp_v2,temp_v3=exp()
		count_v1+=temp_v1
		count_v2+=temp_v2
		count_v3+=temp_v3
	return count_v1/float(exp_count), count_v2/float(exp_count), count_v3/float(exp_count)

v1,v2,v3=final_exp()
print v1,v2,v3