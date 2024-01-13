#Name: Jack Wyeth
def bubblesort(array,size):
    swap_counter=0
    for x in range(len(array)):
        for y in range(0, len(array)-x-1):
            if array[y]>array[y+1]:
                temp =array[y]
                array[y]=array[y+1]
                array[y+1]=temp
                swap_counter+=1
    return swap_counter



def hoare_partition(a, l, r):
    global qs_swap
    pivot = a[l]
    i = l 
    j = r
    while i<j:
        while i < j and a[i] <= pivot:
            i += 1
        while a[j] > pivot:
            j-=1
        
        a[i], a[j] = a[j], a[i]
        qs_swap+=1
    a[i], a[j] = a[j], a[i]
    qs_swap+=1
    a[l], a[j] = a[j], a[l]
    qs_swap+=1
    return j

def quick_sort(a, l, r):
    if l < r:
        p = hoare_partition(a, l, r)
        quick_sort(a, l, p - 1)
        quick_sort(a, p + 1, r)
 
def main():
    global qs_swap
    qs_swap=0
    arr=[]
    
    size=int(input())
    flag=0
    while(flag<size):
        var=int(input())
        arr.append(var)
        flag+=1
    #at this point in the program we have our array filled in and then we make four deep copies to apply to the four algorithms   
    bubble_array=[]
    quick_array=[]
    
    
    for val in arr:
        bubble_array.append(val)
        quick_array.append(val)
       
    barray=bubblesort(bubble_array,size)
    print(barray)
    

    quick_sort(quick_array, 0, size-1)
    print(qs_swap)




if __name__=="__main__": 
    
    main() 
