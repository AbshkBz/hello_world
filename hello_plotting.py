'''
Hello World program for plotting in python

inspired by Killol Govani's tutorial on medium
'''
# dependencies
import numpy as np
import matplotlib.pyplot as plt

# defining a couple of arrays
a = np.linspace(1,10,10).reshape(10,1)
b = np.random.rand(10)

# plot values in array a vs values in array b
plt.figure() # specify figure attributes
plt.subplot(2,1,1)
plt.plot(a,b)
plt.title("First plot using matplotlib") # give a title to the plot
plt.xlabel("X label") # name x-axis
plt.ylabel("Y label") # name y-axis
plt.grid(True) # shows grids in the plots
plt.show()

# plotting multiple data sets in the same plot
x = np.arange(1,5)
y = x **2 
plt.subplot(2,1,2)
plt.plot(a,b,'bo', x,y, 'r^')
plt.title("multiple data sets plotted in the same plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.show()

# above graphs plotted as subplots in a single column plot with two rows

# bar graph with matplotlib
divs = ["Satish","Arjun","Mrinal","Rahul"]
marks = [75,85,72,89]

plt.bar(divs, marks, color='blue')
plt.title("Mathematics exam marks out of 100")
plt.xlabel("Students")
plt.ylabel("Marks obtained")
plt.show()

# plot histogram
z = np.random.randn(100)
plt.hist(z,10)
plt.title('Histogram example')
plt.xlabel("data")
plt.ylabel("frequency")
plt.grid(True)
plt.show()

# scatter plot
plt.scatter(x,y)
plt.title("scatter plot example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
