from random import *
from time import *

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
        l.append(randint(0, number_of_data))
        if number_of_data > 100000 and n % (round(number_of_data/50)) == 0:
            print("Creating list : ", 100 * n / number_of_data, "%")



#Sorting algorithms-----------------------------------------------------------------------------------------------------
#Selection sort based algorithms
def selectionSort(t, n):
    for i in range(n-1):
        inf = i
        for j in range(i+1, n):
            if t[j] < t[inf]:
                inf = j
        t[i], t[inf] = t[inf], t[i]

def doubleSelectionSort(t, n):
    for i in range(n//2):
        inf = i
        sup = i
        for j in range(i+1, n-i):
            if t[j] < t[inf]:
                inf = j
            elif t[j] > t[sup]:
                sup = j
        t[inf], t[i] = t[i], t[inf]
        if sup == i:
            sup = inf
        t[sup], t[n-1-i] = t[n-1-i], t[sup]


#Bauble sort based algorithms
def baubleSort(t, n):
    for i in range(n):
        isSwaped = False
        for j in range(n-1-i):
            if t[j] > t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
                isSwaped = True
        if not isSwaped:
            break

def cocktailSort(t, n):
    isSwapped = True
    inf = 0
    sup = n-1
    while isSwapped:
        isSwapped = False
        for i in range(inf, sup):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                isSwapped = True
        if not isSwapped:
            break
        sup -= 1
        isSwapped = False
        for i in range(sup-1, inf-1, -1):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                isSwapped = True
        inf += 1

def combSort(t, n):
    isSwaped = True
    gap = n
    while isSwaped or gap != 1:
        isSwaped = False
        gap = max((gap * 10)//13, 1)
        for i in range(n-gap):
            if t[i] > t[i+gap]:
                t[i], t[i+gap] = t[i+gap], t[i]
                isSwaped = True

def oddEvenSort(t, n):
    isSwapped = True
    while isSwapped:
        isSwapped = False
        temp = 0
        for i in range(1, n-1, 2):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                isSwapped = True
        for i in range(0, n-1, 2):
            if t[i] > t[i+1]:
                t[i+1], t[i] = t[i], t[i+1]
                isSwapped = True



#Init code--------------------------------------------------------------------------------------------------------------
#Sorting algorithm used
algos = ["selectionSort", "doubleSelectionSort", "baubleSort", "cocktailSort", "combSort", "oddEvenSort"]

#One list for all the algorithms to be equal
First_list = []

#Time the sorting algorithm, test if the algorithm work, else, display the output
def run(i):
    #Init the list to sort
    list = First_list.copy()

    #Run and time the algo
    start_time = perf_counter()
    eval(algos[i] + "(list, number_of_data)")
    end_time = perf_counter()
    execution_time = end_time - start_time
    print(algos[i], execution_time)

    if not check_list(list):
        print("\n", algos[i], "\nPour la liste initiale\t", First_list, "\nL'algorithme renvoie\t", list, "\n")



#Main code--------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Inputs
    default_value = 10000
    number_of_data = input(f"Please enter the length of the random list to be sorted ('d' to put {default_value} from 0 to {default_value}) :\n")
    if number_of_data == "d":
        number_of_data = default_value
    else:
        number_of_data = int(number_of_data)


    #Create a random list
    rng(First_list)

    # Test all the algorithms
    for i in range(len(algos)):
        print(i + 1, "/", len(algos), " : ", algos[i])
        run(i)