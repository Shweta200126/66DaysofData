#!/usr/bin/env python
# coding: utf-8

# In[19]:


from PIL import Image, ImageFilter, ImageFont, ImageDraw
from matplotlib.pyplot import imshow


# In[20]:


file_name = 'hillside.jpg'
im = Image.open(file_name)
imshow(im)


# In[21]:


print(im.size)
print(im.format_description)
print(im.mode)


# In[22]:


crop = (20,100,600,600)
cropped_image = im.crop(crop)
imshow(cropped_image)


# In[23]:


resized_im = im.resize((400,200))
imshow(resized_im)


# In[24]:


gray_scale = im.convert('LA')
imshow(gray_scale)


# In[25]:


effect = im.filter(ImageFilter.GaussianBlur(radius=5))
imshow(effect)


# In[26]:


draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 200)
draw.text((10, 10), "Shweta's Photo!", font=font)
imshow(im)


# In[ ]:




