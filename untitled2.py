# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 00:03:42 2021

@author: Tanmay
"""

n=int(input("enter the number of students : "))
student_list=[]
grade_list=[]
s=1
for i in range (1,n+1):
    student_list.append(int(input("enter the students total marks: ")))
print("marks list of student according to their roll number : " ,student_list)
for s in range(0,len(student_list)):
    if(student_list[s]>=91 and student_list[s] <=100):
        grade = "A"
    elif(student_list[s]>=81 and student_list[s] <=90):
        grade = "B"
    elif(student_list[s]>=71 and student_list[s]<=80):
        grade = "C"
    elif(student_list[s]>=61 and student_list[s]<=70):
        grade = "D"
    else:
        grade ="O"  
    grade_list.append(grade)
print("grades of the students according to their roll numbers: ",grade_list)

print("the marks of roll number 2 student is",student_list[1])
print("the grade of roll number 2 student is",grade_list[1])
           
