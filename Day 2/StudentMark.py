mark_list=[12,18,25,24,2,5,18,20,20,21]
n=10
def find_more_than_average(n,mark_list):
    total_mark=0
    for i in mark_list:
        total_mark+=i
    avg=total_mark/n
    above_avg=0
    for i in mark_list:
        if i>avg:
            above_avg+=1
    avg_percentage=above_avg/n*100
    return avg_percentage
def sort_marks(mark_list):
    mark_list=sorted(mark_list)
    return mark_list
def generate_frequency(mark_list):
    freq=[]
    for x in range(26):
        count=0
        for y in mark_list:
            if x==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_average(n,mark_list))
print(sort_marks(mark_list))
print(generate_frequency(mark_list))
