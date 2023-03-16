def func():

    list1 = [2, 2, 1, 1, 1, 2, 2]

    most_frequent_list1 = max(set(list1), key=list1.count)
    less_frequent_list1 = min(set(list1), key=list1.count)
    print("Results for the first list: ", "\n", most_frequent_list1, less_frequent_list1)

    list2 = [3, 2, 3]

    most_frequent_list2 = max(set(list2), key=list2.count)
    less_frequent_list2 = min(set(list2), key=list2.count)
    print("Results for the second list: ", "\n", most_frequent_list2, less_frequent_list2)

    list3 = [3, 3, 2, 2, 3, 3, 1]

    most_frequent_list3 = max(set(list3), key=list3.count)
    less_frequent_list3 = min(set(list3), key=list3.count)
    print("Results for the third list: ", "\n", most_frequent_list3, less_frequent_list3)

func()








