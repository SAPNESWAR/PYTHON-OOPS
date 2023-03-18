def translate(dict,list1):
    list2=[]
    for i in list1:
        list2.append(dict[i])
    return list2
dict={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(translate(dict,list1))
