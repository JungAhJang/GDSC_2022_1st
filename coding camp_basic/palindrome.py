#palindrome이란 문자열을 뒤집었을 때도 동일한 문자열인 경우를 뜻합니다.

#소문자 알파벳으로만 이루어진 문자열 A가 주어졌을 때, 문자열 A가 palindrome인지를 판단하는 프로그램을 작성해보세요. 단, 함수를 이용하여 문제를 해결해주세요.

arr = list(input())

def find_palindrome(arr) :
    if arr == arr[::-1] :
        return print("Yes")
    return print("No")

find_palindrome(arr)
