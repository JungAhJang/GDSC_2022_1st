arr = input() #만약 문자열을 list화 하지 않고, 바로 리스트화 하고 싶어서 input().split("")하면 오류가 난다
arr = list(arr)
arr.sort() 
sorted_arr = "".join(arr)
print(sorted_arr)