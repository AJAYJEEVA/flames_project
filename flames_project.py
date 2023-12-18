#!/usr/bin/env python
# coding: utf-8

# In[ ]:


user_1=str(input("your name:"))
user_2=str(input("your gf or friend name"))

# changeing input into list and lowercase if there is any space make combine

a=list(user_1.lower().replace('',''))
b=list(user_2.lower().replace('',''))
c=[]

for i in a:
    for j in b:
        if i == j:
            c+=i
        else:
            continue
            
#for removing commmon letter

for i in range(len(c)):
    try:
        a.remove(c[i])
        b.remove(c[i])
    except ValueError:
        pass

    
d=len(a) + len(b)

flames=['friend','love','affection','marriage','ememy','sister']
while len(flames) > 1:  # 6>1 true
    formula=d % len(flames) - 1 # 3%5
    if formula >= 0:
        left=flames[formula + 1:] #slicing in left
        right=flames[:formula]
        flames=left+right
    else:
        flames=flames[:len(flames) - 1]
        
def friends():
    print("your were a friends")
    
def love():
    print("your were in love")
    
def affection():
    print("you have just have affection")
    
def marriage():
    print("your were in marriage")
    
def ememy():
    print("you two were ememy")
    
def sister():
    print("she is your sister")
    

        
print(flames)   


# In[ ]:





# In[ ]:





# In[ ]:




