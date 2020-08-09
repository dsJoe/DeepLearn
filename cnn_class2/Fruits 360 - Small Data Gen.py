import os


# In[2]:


def mkdir(p):
    if not os.path.exists(p):
        os.mkdir(p)


def link(src,dst):
    if not os.path.exists(dst):
        os.symlink(src,dst,target_is_directory=True)


# In[3]:


mkdir('../large_files/fruits-360-small')


# In[4]:


classes = [  'Apple Golden 1',
  'Avocado',
  'Lemon',
  'Mango',
  'Kiwi',
  'Banana',
  'Strawberry',
  'Raspberry']


# In[5]:


train_path_from = os.path.abspath('../large_files/fruits-360/Training/')
valid_path_from = os.path.abspath('../large_files/fruits-360/Test/')

train_path_to = os.path.abspath('../large_files/fruits-360-small/Training')
valid_path_to = os.path.abspath('../large_files/fruits-360-small/Validation')


# In[ ]:


mkdir(train_path_to)
mkdir(valid_path_to)


# In[6]:


for c in classes:
    link(train_path_from + '/' + c, train_path_to + '/' + c)
    link(valid_path_from + '/' + c, valid_path_to + '/' + c)