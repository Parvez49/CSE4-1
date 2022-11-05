# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EwRDjAeEdRcwhoNWZYr1SWt94POu6FGE
"""

import random as rnd
import math

def CLCG(m1,m2,a1,a2,seed1,seed2,R):
    Y1=seed1
    Y2=seed2
    n=100

    Y1 = a1 * Y1 % m1
    Y2 = a2 * Y2 % m2

    X = (Y1 - Y2) % (m1 - 1)
    preX=X
    cycle=1
    #for i in range (1, n):
    while True:
      #print(X)
      if (X > 0):
        R.append(X/m1)
      elif (X == 0):
        R.append((m1-1)/m1)
      Y1 = a1 * Y1 % m1
      Y2 = a2 * Y2 % m2

      X = (Y1 - Y2) % (m1 - 1)

      if X!=preX:
        cycle+=1
      else : break
    #print(X)
    print("Cycle length: ",cycle)

def Kolmogorov_Smirnov(R,n):
    R=sorted(R)
    d_plus_max = 0
    d_minus_max = 0
    i = 1
    for value in R:
        d_plus_i_value = ( (i/n) - value )
        d_minus_i_value=(value-((i-1)/n))
        if d_plus_i_value > d_plus_max:
            d_plus_max = d_plus_i_value
        if d_minus_i_value > d_minus_max:
            d_minus_max = d_minus_i_value
        i += 1
    #print(d_plus_i_value, d_minus_i_value)
    return max(d_plus_i_value, d_minus_i_value)
    
def autocorrelation_tests( R, n, gap_sequence ):
    little_m = gap_sequence
    start_index = 0
    big_n = n
    big_m = 0.0
    while (big_m + 1) < ( (big_n - start_index)/little_m ) :
        big_m = big_m + 1
    one_over_m_plus_one = ( 1.0/(big_m + 1.0 ) )
    rho_hat = 0.0
    sum_of_rho_hat = 0.0

    every_m_element = R[0::gap_sequence]

    for value in range(0, (len(every_m_element)-1) ):
        thisValue = float(every_m_element[value])
        nextValue = float(every_m_element[value+1])
        sum_of_rho_hat = sum_of_rho_hat + (thisValue * nextValue)

    sum_of_rho_hat = (one_over_m_plus_one * sum_of_rho_hat) - 0.25
    variance_of_rho =  math.sqrt( (13*big_m + 7 )) / (12*(big_m + 1))
    print("variance of rho: ",variance_of_rho)

    z_statistic = sum_of_rho_hat / variance_of_rho
    return z_statistic




m1 = 2147483563
m1=5011
a1 = 4001
m2 = 2147483399
m2=1059
a2 = 4069
R=list()
seed1=m1-100
seed2=m2-100
CLCG(m1,m2,a1,a2,seed1,seed2,R)
d=Kolmogorov_Smirnov(R[:301],300)

print("Uniform test: ")
print("Kolmogorov_Smirnov: ")
print("D value is: ",d)


print("Autocorrelation tests: ")
z=autocorrelation_tests(R[:301],300,2)
print("Value of Z: ",z)
#print(R[:301])