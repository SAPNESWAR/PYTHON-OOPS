'''#wa python function which accepts a sentence and finds the number of letters and digits in the sentence.
it should returna list in which the first value should be letter count and second value should be digit count.
Ignore the spaces or any special characters in the sentences'''

def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return [l_count,d_count]
str1=input()
print(function(str1))
