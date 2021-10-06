#!/usr/bin/env python
# coding: utf-8

# In[16]:


#h 타이핑하면 주피터 노트북 사용법  / a b 는 추가 dd는 삭제 / 셀 실행은 커맨드 엔터 


# In[3]:


a = [1,2,3,4,5]
for index, num in enumerate(a):
    print(index, num)
#기본적으로 for 에 리스트를 순회할 경우 값만 추출하는데
#enumerate 메소드를 사용시 전부가능


# In[17]:


def mean(nums):
    return sum(nums) /len(nums)


# In[28]:


#소수판별
def is_prime(num):
    a=0
    for i in range(2, num+1):
        if num%i==0:
            a +=1
    return a
print(is_prime(7))
print(is_prime(5))
print(is_prime(17))
print(is_prime(3))


# In[ ]:




