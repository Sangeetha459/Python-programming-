def swap_elements(lst,pos1,pos2):
    if pos1<1 or pos1>len(lst) or pos2<1 or pos2>len(lst):
        return "invalid"
    lst[pos1-1],lst[pos2-1]=lst[pos2-1],lst[pos1-1]
    return lst
lst=[1, 2, 3, 4, 5]
pos1=2
pos2=5
print(swap_elements(lst,pos1,pos2))


