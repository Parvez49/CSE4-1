# -*- coding: utf-8 -*-
"""Document Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w_RpaQfK2C88Jh4EUtWcLawbjHMmXUV3
"""

# Simulation of Document processing

work_time=[45,16,5,29,33,25,21]
jobs_num=57

print(" Document_Number Start_time Work_time Finish_time Cumul_time Break_Flag Number_Jobs ")

st=0
n=1
cumul=0
flag=0
finish=0
for i in work_time:
  cumul+=i
  finish+=i
  if cumul>=60:
    flag=1

  print("{:10}".format(n), "{:12}".format(st), "{:10}".format(i),
        "{:10}".format(finish),"{:12}".format(cumul),"{:8}".format(flag),
        "{:10}".format(jobs_num))
  
  jobs_num-=1
  st+=i
  n+=1
  if flag==1:
    flag=0
    cumul=0
    finish+=5
    st+=5