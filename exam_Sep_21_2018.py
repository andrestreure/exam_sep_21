
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[52]:


NAME = "Andres Treure, 2015554"
COLLABORATORS = ""


# ---

# Fill in the cell above to provide us with your name and student number, like
# 
# NAME = "Adam Smith, #student number#"
# 
# where you replace "#student number#" with your ... (very good!)
# 
# Unfortunately, you are not allowed to work with "COLLABORATORS" in this exam.

# # exam September 21st, 2018
# 
# With this python part of the exam you can earn at max. 4 points.
# 
# 

# 
# In the first cell of the notebook, give us your name and student number in the way indicated above. 
# 
# Fill in the notebook (see below for code cells and text cells that you need to fill in).
# 
# If you look at the menus above (File, Edit, View etc.), there is one called "Cell". If you click on this, you can change the "Cell Type". Choose "Code" when you are typing python or R code. Choose "Markdown" when you are typing, well, markdown.
# 
# When you finish the notebook, make sure that you **save it with the output of your code included**. 
# 
# Then put it on github, e.g. by dragging it onto github (see instructions below). 
# 
# Finally, add a link to your README file with the name of this exam: "Exam September 21, 2018".
# 
# 

# ## Generating and plotting data
# 
# We start by importing the usual libraries.

# In[53]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import optimize
get_ipython().run_line_magic('matplotlib', 'inline')


# #### a) [0.5 point] Explain in words what the following code does. 

# In[54]:


n_observations = 100
x = np.random.uniform(0,2,size=n_observations)
df = pd.DataFrame({'x': x})

It creates a dataframe with a random variable called 'x'. In this dataframe are 100 random numbers of this variable between 0 and 2. 
# Now we are going to add some columns to the dataframe `df`.

# #### b) [0.5 points] Add two columns to the data frame: (i) column `y` where $y=3*x+5$ and (ii) column `z` where $z = (x-1)^2$.

# In[55]:


df['y']=3*x+5
df['z']=(x-1)**2

df.head()


# #### c) [0.5 point] Calculate the means and standard deviations for `x` and `y`. 
# 
# [hint: you can do this with one command or with four separate commands]

# In[56]:


df.describe()


# #### d) [0.5 points] Use your knowledge of statistics to explain the relations (i) between the means of `x` and `y` and (ii) between the standard deviations of `x` and `y`.

# In[57]:


(i) y = 3*x+5 so if you take the mean of x and y this will be no different
(ii) the standard deviation of y is 3 times the standard deviation of x, so no + 5. 
This is because all y's get + 5 so that makes the gap between a random y and the mean y nog bigger,
but if you do x*3 you make the gap between the mean and the random veriable bigger. 
You can see this 'gaps'in the standard deviation so that's why the standard deviation of y is 3 times the standard deviation of x. 


# #### e) [1 point] Plot a histogram of `x` with fractions (not absolute numbers) on the vertical axis. Add the label $x$ to the horizontal axis.

# In[58]:


plt.hist(df.x, normed=True, bins=30, label='x')
plt.xlabel('$x$')
plt.show()


# #### f) [0.5 points] Make a scatter plot of `y` vs `z` with the label $y$ on the horizontal axis and the label $z$ on the vertical axis.

# In[59]:


plt.scatter(df.y,df.z,label='y and z')
plt.xlabel('$y$')
plt.ylabel('$z$')
plt.show()


# This relation looks rather "perfect". We want to make a "noisy" version of this graph.
# 
# #### g) [0.5 points] Create a variable `z2` equal to `z` but with some "noise" added to it. That is, add a random variable (vector) with mean 0 to `z` to get `z2`. Then plot `y` against `z2`. Adjust the standard deviation of the "noise" variable such that the shape of the figure under f) can still be recognized but not perfectly.
# 
# [hint: under a) you have seen the library that contains functions to create a "noisy variable"]

# In[61]:


z2 = df.z + np.random.normal(0,0.1,100)

plt.scatter(df.y,z2,label='y and z2')
plt.xlabel('$y$')
plt.ylabel('$z2$')
plt.show()


# ## Github
# 
# After you have finished, we need to upload this notebook on github.

# Instructions on how to upload this on github can be found [on this page](http://janboone.github.io/programming-for-economists/github.html). This page has two screencasts: one shows how to drag the notebook onto your github page, the other shows how you can use the command line to upload your notebook.
# 

# Remember to update the README file in your repository to include a link to this notebook on github.
# 
# 
# The links that you should post start with “github.com/” and are NOT of the form “http://localhost”. Make sure you test your links after uploading.
