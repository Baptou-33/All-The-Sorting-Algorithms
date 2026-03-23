from random import *

#Usefull functions------------------------------------------------------------------------------------------------------
#Check if the list is well-sorted
def check_list(l):
    for check in range(len(l) - 1):
        if l[check + 1] < l[check]:
            return False
    return True

#Create the list to be sorted
def rng(l):
    l.clear()
    for n in range(1, number_of_data + 1):
        l.append(randint(min_random, max_random))
        if number_of_data > 100000 and n % (round(number_of_data/50)) == 0:
            print("Creating list : ", 100 * n / number_of_data, "%")



#Sorting algorithms-----------------------------------------------------------------------------------------------------
#Selection sort
def selectionSort(t, n):
    for i in range(n-1):
        inf = i
        for j in range(i+1, n):
            if t[j] < t[inf]:
                inf = j
        t[i], t[inf] = t[inf], t[i]



#Init code--------------------------------------------------------------------------------------------------------------
#One list for all the algorithms to be equal
First_list = []



#Main code--------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Inputs
    default_value = 10000
    number_of_data = input(f"Please enter the lenght of the random list to be sorted ('d' to put {default_value} from 0 to {default_value}) :\n")
    if number_of_data == "d":
        number_of_data = default_value
        min_random = 0
        max_random = default_value
    else:
        number_of_data = int(number_of_data)
        min_random = int(input("Please enter the number min : "))
        max_random = int(input("Please enter the number max : "))

#Create a random list
rng(First_list)

selectionSort(First_list, number_of_data)
print(First_list)
print(check_list(First_list))