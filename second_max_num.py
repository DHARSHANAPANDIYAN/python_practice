
def find_runner_up(n,arr):
    arr_new=list(set(list(arr)))
    arr_new.sort()
    first_place=max(arr_new)
    arr_new.remove(first_place)
    second_place=max(arr_new)
    return second_place     
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res=find_runner_up(n,arr)
    print(res)       
    # print(arr[arr.index(max(arr))]-1)
    
