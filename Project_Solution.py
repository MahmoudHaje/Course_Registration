#-------------------------------------------------------------------------------
# Name:		module1
# Purpose:
#
# Author:	  mahmo
#
# Created:	 02/02/2019
# Copyright:   (c) mahmo 2019
# Licence:	 <your licence>
#-------------------------------------------------------------------------------

import io

class Course:

	# Constructor
	def __init__(self,
		semester,
		#id,
		name,
		points,
		hova,
		computer,
		Signal,
		Devices,
		prev1,
		prev2,
		prev3,
		option1,
		option2,
		tsamod):
		self.semester = semester
		#self.id = id
		self.name = name
		self.points = points
		self.hova = hova
		self.computer = computer
		self.Signal = Signal
		self.Devices = Devices
		self.prev1 = prev1
		self.prev2 = prev2
		self.prev3 = prev3
		self.option1 = option1
		self.option2 = option2
		self.tsamod = tsamod

	def __str__(self):
		return self.name


def csv_unireader(f, encoding="utf-8"):
	f = io.open(f, mode="r", encoding="utf-8")
	dict_all_courses = {}
	# just read the first line and do not do anything
	f.readline()
	# start from the second line
	for line in f:
		words = line.split("\t")
		current_id = words[1]
		del words[1]
		dict_all_courses[current_id] = Course(*words)# ask about it
	return dict_all_courses

#to check previos we must go for all the corses
def check_prevs(dict_all_courses, course_id_list_Student):
	for i, nm in enumerate(course_id_list_Student):
		course_id_list_Student[i] = str(nm)
	list_possible_courses = []
	for course_key, course_value in dict_all_courses.iteritems():
		list_courses = [course_value.prev1, course_value.prev2, course_value.prev3]
		possible = all(elem in course_id_list_Student or elem=='' for elem in list_courses)
		if possible and course_key not in course_id_list_Student:# == True:
			list_possible_courses.append(course_key)
	return list_possible_courses

#check tsamod form the list we got from check_prevs
def check_tsamod(dict_all_courses,list_possible_courses, course_id_list_Student):
	for i, nm in enumerate(course_id_list_Student):
		course_id_list_Student[i] = str(nm)
	for course in list_possible_courses:
		tsamod=dict_all_courses[course].tsamod
		if tsamod != '\n': # we take '\n' not '' cuz it is the last string in the line
			if tsamod.rstrip('\n')not in list_possible_courses and tsamod.rstrip('\n')not in course_id_list_Student:
				list_possible_courses.remove(course)
	return list_possible_courses

##check possiblaty form the list we got from check_tsamod
def check_possibility(dict_all_courses,list_possible_courses,course_id_list_Student):
	for i, nm in enumerate(course_id_list_Student):
		course_id_list_Student[i] = str(nm)
	for course in list_possible_courses:
		option1=dict_all_courses[course].option1
		option2=dict_all_courses[course].option2
		if option1 != '':
			if option1 not in course_id_list_Student and option2 not in course_id_list_Student:
				list_possible_courses.remove(course)
	return list_possible_courses


#check if student specle is computer
def check_computers(dict_all_courses,list_possible_courses):
	list_computers=[]
	for course in list_possible_courses:
		hova=dict_all_courses[course].hova
		if hova != '':
			list_computers.append(course)
		if hova == '':
			if dict_all_courses[course].computer!='':
				list_computers.append(course)
	return list_computers
#check if student specle is Signal
def check_Signal(dict_all_courses,list_possible_courses):
	list_Signal=[]
	for course in list_possible_courses:
		hova=dict_all_courses[course].hova
		if hova != '':
			list_Signal.append(course)
		if hova == '':
			if dict_all_courses[course].Signal!='':
				list_Signal.append(course)
	return list_Signal

#check if student specle is Devices
def check_Devices(dict_all_courses,list_possible_courses):
	list_devices=[]
	for course in list_possible_courses:
		hova=dict_all_courses[course].hova
		if hova != '':
			list_devices.append(course)
		if hova == '':
			if dict_all_courses[course].Devices!='':
				list_devices.append(course)
	return list_devices

#check if student have none specle
def check_NA(dict_all_courses,list_possible_courses):
	list_NA=[]
	for course in list_possible_courses:
		hova=dict_all_courses[course].hova
		if hova != '':
			list_NA.append(course)
	return list_NA

#get specialization from the file
def specialization_from_file(student1):
	f = open("student1.txt", "r")
	for line in f:
        #secar untill we got to "specialization"
		if "specialization" in line:
			specialization = line.partition('#') #he got all the line
			specialization=specialization[0] # he take before '#'
			specialization=specialization.partition(':') #('specialization ', ':', ' NA   ')
			specialization = specialization[2].replace(" ", "") # ' NA   ' --> 'NA'
			break
	f.close()
	return specialization


#return corses id from the file
def read_file_student1 (student1):
	course_id_list_Student = []#
	course_point_list = []#
	f = open("student1.txt", "r")
	for line in f:
        #search until we reach "Course"
        #we start getting the corse id after this line
		if "Course" in line:
			break
	for line in f:
		line.strip('\n')
		course_id_student, course_point = line.split('\t\t')
		course_id_student = int(course_id_student)
		course_point = float(course_point)
		course_id_list_Student.append(course_id_student)
		course_point_list.append(course_point)
	f.close()
	return course_id_list_Student

#retun list of point of the corses
def get_point(dict_all_courses,list_possible_courses):
	list_point=[]
	for course in list_possible_courses:
		point=dict_all_courses[course].points
		list_point.append(point)
	for i, nm in enumerate(list_point):
		list_point[i] = float(nm)
	return list_point


#choosing how much point and which corse he want
def student(dict_all_courses,list_possible,list_points,points_student,course_student):
	for i, nm in enumerate(list_possible):
		list_possible[i] = int(nm)
	print(list_possible)
	while course_student not in list_possible:
		course_student= input("the course u want to take is not posssble to take it , choose onther on:")
	corse_deleted_1=course_student#must return it to the list
	point=dict_all_courses[str(course_student)].points
	list_possible.remove(corse_deleted_1)
	points_student=points_student-float(point)
	course_points=float(point)
	list_points.remove(course_points)
	new_list_points=[]# new list to add point(consider how much points_student)
	new_list_corses=[]#new list to add the corse that are avaibale to take(consider how much points_student)
	new_list_points.append(list_points[0])
	new_list_corses.append(list_possible[0])
	count=list_points[0]
	corse_deleted_2=list_possible[0]# must return it to the list
	list_points.remove(list_points[0])
	list_possible.remove(list_possible[0])
	stop=0
    #from here to line 260, I appended the point to the list new_list_points, and corses to new_list_corses
    # consider how much point the studnet want to take
    # I had list_points and list_possible for corses and checked the sum numbers in list_points that equal to points_student
    # and if it is not eqaul i took the closer sum and printed that to the studnet
	for elemnt in range(0,len(list_points)):
		count2=count
		if count+list_points[elemnt]==points_student:
			new_list_points.append(list_points[elemnt])
			new_list_corses.append(list_possible[elemnt])
			break
		elif count+list_points[elemnt]>points_student:
			found=count+list_points[elemnt]-points_student
			if found in new_list_points:
					index=new_list_points.index(found)
					new_list_points.remove(found)
					new_list_corses.remove(new_list_corses[index])
					new_list_points.append(list_points[elemnt])
					new_list_corses.append(list_possible[elemnt])
					count-=found
					count+=list_points[elemnt]
					if count==points_student:
						break
			else:
				while found not in new_list_points and stop==0:
					found+=1
					if found in new_list_points:
						count2=count
						count2-=found
						count2+=list_points[elemnt]
						if(count2>count):
							index=new_list_points.index(found)
							new_list_points.remove(found)
							new_list_corses.remove(new_list_corses[index])
							new_list_points.append(list_points[elemnt])
							new_list_corses.append(list_possible[elemnt])
							count=count2
							stop=1
							if count==points_student:
								break
						else:
							stop=1
					if found>max(new_list_points):
						stop=1
				stop=0
		elif count+list_points[elemnt]<points_student:
			new_list_points.append(list_points[elemnt])
			new_list_corses.append(list_possible[elemnt])
			count+=list_points[elemnt]
	new_list_corses.append(course_student)
	new_list_points.append(course_points)
	if count!=points_student:
		print("we  could not found match for the point you want , we took the closer avablie number of points")
	print(new_list_points)
	print(new_list_corses)
	list_possible.append(corse_deleted_1)#appned the corse that we delete in the start of the func
	list_possible.append(corse_deleted_2)#appned the corse that we delete in the start of the func

	return new_list_corses

#add,delted and replace corsess (chose of student)
def delet_add(dict_all_courses,list_corses,list_possilbe_corses,count,points):
	print("this is the corses u must take:\n",list_corses)
	print("and they are:",count)
	choose=input("if you want to add corse press 1, if u wanna delet corse press 2, if you wanna replace press 3,if u dont wanna do anything press 0")
	while choose!=0 and choose !=1 and choose !=2 and choose !=3:
		choose=input("invalid input.if you want to add corse press 1, if u wanna delet corse press 2, if you wanna replace press 3,if u dont wanna do anything press 0")
	if choose==1:
		#add
		print("choose from the list corses:")
		print(list_possilbe_corses)
		corse_add=input("enter the corse id u want to add:")
		while corse_add not in list_possilbe_corses or corse_add in list_corses:
			corse_add=input("u cant take this corse plz choose onther one:")
		#we check if it grater thatn 24
		point_corse_add=dict_all_courses[str(corse_add)].points
		if points+float(point_corse_add)>24:
			print(" sory u cant add this corse, becuze the point now are greater than 24:",corse_add)
		else:
			list_corses.append(int(corse_add))

	if choose==2:
		# delet
		print("choose from the list corses:")
		print(list_corses)
		corse_delet=input("enter the corse id u want to delet:")
		while corse_delet not in list_corses:
			corse_delet=input("u cant delet this corse plz choose onther one:")
		#we check if it smaller  thatn 16
		point_corse_delete=dict_all_courses[str(corse_delet)].points
		if points-float(point_corse_delete)<16:
			print(" sory u cant add this corse, becuze the point now are smaller than 16:",corse_delet)
		else:
			list_corses.remove(int(corse_delet))

	if choose==3:
		#replace
		corse_add=input("enter the corse id u want to add:")
		while corse_add not in list_possilbe_corses or corse_add in list_corses:
			corse_add=input("u cant take this corse plz choose onther one:")
		corse_delet=input("enter the corse id u want to delet:")
		while corse_delet not in list_corses:
			corse_delet=input("u cant delet this corse plz choose onther one:")
		#we check if it grater thatn 24or less than 16
		point_corse_delete=dict_all_courses[str(corse_delet)].points
		point_corse_add=dict_all_courses[str(corse_add)].points
		points+=float(point_corse_add)
		points-=float(point_corse_delete)
		if points>24 or points<16:
			print("sory u cant replace these corses")
		else:
			list_corses.remove(corse_delet)
			list_corses.append(corse_add)
	print(list_corses)
	return list_corses

#writing file to student
def get_file_student(student1,final_list,final_list_points):
	f_res = open("studnet_file.txt", "w")
	f = open("student1.txt", "r")
	for line in f: #we read from the file that stduent sent to get his name and id
		if "Student name" in line or "Student Id" in line:
			f_res.write(line+ "\n")
	f.close()
	f_res.write("corse" + "\t" + "credit" + "\n")
	for i in range(len(final_list)):
		f_res.write(str(final_list[i]) + "\t" + str(final_list_points[i]) + "\n")
	f_res.close()



############# MAIN

#read the file and creat dict that contain it
dict_all_courses = csv_unireader('course_list.txt')
# read file and return list that srudent took
course_id_list_Student=read_file_student1('student1.txt')
# return list that contain all possile corsese after consider the previos
list_possible_courses=check_prevs(dict_all_courses,course_id_list_Student)
# return list that contain all possile corsese after consider the tsamod
list_possible_courses=check_tsamod(dict_all_courses,list_possible_courses, course_id_list_Student)
# return list that contain all possile corsese after consider the possibalty
list_possible_courses=check_possibility(dict_all_courses,list_possible_courses,course_id_list_Student)
#read file and take the specializion ( NA ,COMPUTER,Signal,DEVICES)
specialization=specialization_from_file('student1.txt')
print(list_possible_courses)


point = input("Enter then number of points you want: ")
while point >24 or point<16:
	point = input("invalid number ,(16<point<24)Enter then number of points you want: ")
course= input("Enter the course ID u must take :")


if specialization=='NA':
	## return list that contain all possile corsese after consider the NA(hova=='')
	list_NA=check_NA(dict_all_courses,list_possible_courses)
	#return list that contain the point of the corses (float)
	list_point=get_point(dict_all_courses,list_NA)
	#return list corses after consider how much point he want and which corse he want take
	list_corses=student(dict_all_courses,list_NA,list_point,point,course)
    #count number of corses
	count_corses=len(list_corses)
    #return list of corses after asking the student to add,delete or replace corse
	final_list=delet_add(dict_all_courses,list_corses,list_NA,count_corses,point)

if specialization=='Computer':
    ## return list that contain all possile corsese after consider the NA(hova=='', and computer!='')
	list_computer=check_computers(dict_all_courses,list_possible_courses)
    #return list that contain the point of the corses (float)
	list_point=get_point(dict_all_courses,list_computer)
    #return list corses after consider how much point he want and which corse he want take
	list_corses=student(dict_all_courses,list_computer,list_point,point,course)
    #count number of corses
	count_corses=len(list_corses)
    #return list of corses after asking the student to add,delete or replace corse
	final_list=delet_add(dict_all_courses,list_corses,list_computer,count_corses,point)


if specialization=='Signal':
    ## return list that contain all possile corsese after consider the NA(hova=='', and Signal!='')
	list_singal=check_Signal(dict_all_courses,list_possible_courses)
    #return list that contain the point of the corses (float)
	list_point=get_point(dict_all_courses,list_singal)
    #return list corses after consider how much point he want and which corse he want take
	list_corses=student(dict_all_courses,list_singal,list_point,point,course)
    #count number of corses
	count_corses=len(list_corses)
    #return list of corses after asking the student to add,delete or replace corse
	final_list=delet_add(dict_all_courses,list_corses,list_singal,count_corses,point)

if specialization=='Devices':
    ## return list that contain all possile corsese after consider the NA(hova=='', and Devices!='')
	list_Devices=check_Devices(dict_all_courses,list_possible_courses)
    #return list that contain the point of the corses (float)
	list_point=get_point(dict_all_courses,list_Devices)
    #return list corses after consider how much point he want and which corse he want take
	list_corses=student(dict_all_courses,list_Devices,list_point,point,course)
    #count number of corses
	count_corses=len(list_corses)
    #return list of corses after asking the student to add,delete or replace corse
	final_list=delet_add(dict_all_courses,list_corses,list_Devices,count_corses,point)

#retur points of the final_list corses
final_list_points=[]
for corse in final_list:
	final_list_points.append(float(dict_all_courses[str(corse)].points))
print(final_list_points)
#wrting file for student
get_file_student('student1.txt',final_list,final_list_points)