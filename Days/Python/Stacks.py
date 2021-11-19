#!/usr/bin/env python
# coding: utf-8

# ## Stacks in Python

# In[16]:


stack = []


# In[17]:


stack.append(14)
stack


# In[18]:


stack.append(7)
stack


# In[19]:


stack[-1]


# In[20]:


stack.pop()


# In[21]:


stack


# In[22]:


class Stack():
    
    def __init__(self):
        self.list_stack = []
        
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
        
    def push(self,item):
        self.list_stack.append(item)
        
    def pop(self):
        return self.list_stack.pop()
    
    def peek(self):
        
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]
        
    def __repr__(self):
        return repr(self.list_stack)
        


# In[23]:


new_stack = Stack()


# In[24]:


new_stack.is_empty()


# In[25]:


new_stack.push(14)


# In[26]:


new_stack.peek()


# In[35]:


new_stack.push(9)
new_stack.push(10)
print(new_stack)


# In[36]:


new_stack.peek()


# In[37]:


new_stack.is_empty()


# In[ ]:




