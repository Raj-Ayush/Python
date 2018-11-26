import matplotlib.pyplot as plt
import time
from numpy.random import randint
# =============================================================================
# Make function of insertion sort
# =============================================================================
def Insertion_sort(x):
    for j in range(1,len(x)):
        key=x[j]
        i=j-1
        while((i>=0)and(x[i]>key)):
           x[i+1]=x[i] #shift number in slot i right to i+1
           i=i-1 
        x[i+1]=key
    return(x)
    

list1=[34,67,89,90,22]
print("Sorted list is",Insertion_sort(list1))



# =============================================================================
# Make function for calculating time of insertion sort
# =============================================================================
def Time_sorting(num):
# =============================================================================
#     Using randint function we generate random number upto 10000
# =============================================================================
    List=randint(1,10000,num)
    number_of_input.append(len(List))
    start_time=time.time()
    Insertion_sort(List)
    end_time=time.time()
    result_time=end_time-start_time
    print("For sorting of {}".format(num),"time taken {}".format(result_time))
    timing.append(result_time)
    
number_of_input=[]
timing=[]
Time_sorting(10)
Time_sorting(100)
Time_sorting(500)
Time_sorting(800)
Time_sorting(1000)
Time_sorting(2000)
Time_sorting(4000)
Time_sorting(6000)
Time_sorting(8000)
Time_sorting(10000)


#plotting observation
plt.title("INSERTION SORT TIME ANALYSIS")
plt.plot(number_of_input,timing)
plt.plot(number_of_input,timing,'ro')
plt.xlabel("Number_of_input(n)")
plt.ylabel("Time")
plt.show()




    
    
        
            
            
