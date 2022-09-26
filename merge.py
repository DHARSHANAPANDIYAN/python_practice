def merge_the_tools(string, k):
    # your code goes here
    temp = []
    temp_len = 0
    for item in string:
        temp_len += 1
        if item not in temp:
            temp.append(item)
        if temp_len == k:
            print (''.join(temp))
            temp = []
            temp_len = 0
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)