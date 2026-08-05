def create_dictionary(n):

    # ********** Traditional Or Lengthy Way **********
    my_dict = {
        1: "item1",
        2: "item2",
        3: "item3",
        4: "item4",
        5: "item5",
        6: "item6",
        7: "item7"
    }

    dict1 = {i : f"item{i}" for i in range(1, n + 1) }

    # It changes the position of key and value
    dict2 = {value:key for key,value in dict1.items() }

    # print(my_dict)
    print(dict1)
    print(dict2)


def main():
    n = int(input("Enter the length of the dictionary: "))
    create_dictionary(n)
main()