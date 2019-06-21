# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:41:33 2019

@author: Nirbhay
"""
# project worcgfghffcghvk
from collections import OrderedDict

def search(A,B):
    ans = False
    for i in A:
        for j in B:
            if i==j:
                ans = True
    return ans
        
def not_common_books(A,B):
    recommend_list = {}
#    print(recommend_list)
    for key1,value1 in A.items():
        ans = False
        for key2,value2 in B.items():                  
            if key1 == key2:                              
                 ans = True
                 break
             
        if ans == False:
            recommend_list.update({key1:value1})
         
#    print(recommend_list)            
    return recommend_list



A = {'gita':4,'kuran':5,'bible':3}
B = {'gita':5,'bible':4}
found = search(A,B)
if found:
    if len(A)>len(B):
       recommend_books = not_common_books(A,B)
       for key,value in recommend_books.items():
           if value >= 3:
               print("B should read ",key)
    else:
        recommend_books = not_common_books(B,A)
        for key,value in recommend_books.items():
           if value >= 3:
               print("A should read ",key)
else:
    print("not common interest")
       
        
