

def find_runner_up(n,arr):
    arr = list(set(arr))
    arr.sort()
    return arr[len(arr)-2]
   
     
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res=find_runner_up(n,arr)
    print(res)        
    # print(arr[arr.index(max(arr))]-1)
    

