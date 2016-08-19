# How to think like a computer scientist - learn with Python

# Ch.4

# 1. Done

# 2.
def compare(x,y):
    if x < y:
        print x, "is less than", y
    elif x > y:
        print x, "is greater than", y
    else:
        print x, "and", y, "are equal"

# 3. 1 and 5 are the same [not(p or q) == not(p) and not(q)]. 3 and 4 are the same [not(p and q) == not(p) or not(q)]
'''
>>> truth_table("not(p or q)")
 p      q      not(p or q)
==========================
True    True    False  
True    False   False  
False   True    False  
False   False   True   

>>> truth_table("p and q")
 p      q      p and q
======================
True    True    True   
True    False   False  
False   True    False  
False   False   False  

>>> truth_table("not(p and q)")
 p      q      not(p and q)
===========================
True    True    False  
True    False   True   
False   True    True   
False   False   True    

>>> truth_table("not(p) or not(q)")
 p      q      not(p) or not(q)
===============================
True    True    False  
True    False   True   
False   True    True   
False   False   True 

>>> truth_table("not(p) and not(q)")
 p      q      not(p) and not(q)
================================
True    True    False  
True    False   False  
False   True    False  
False   False   True  
'''
