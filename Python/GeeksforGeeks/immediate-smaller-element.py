"""
Given an integer array, for each element in the array check whether there exist a smaller element on the next immediate 
position of the array. If it exist print the smaller element. If there is no smaller element on the immediate next to the 
element then print -1.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains an integer N, where N is the size of array.
The second line of each test case contains N integers sperated with a space which is input for the array arr[ ]

Output:
For each test case, print the next immediate smaller elements for each element in the array.

Sample Input
2
5
4 2 1 5 3
6
5 6 2 3 1 7

Sample Output
2 1 -1 3 -1
-1 2 -1 1 -1 -1
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            print(arr[i+1],end=' ')
        else:
            print(-1,end=' ')
    print(-1,end=' ')
    print()
