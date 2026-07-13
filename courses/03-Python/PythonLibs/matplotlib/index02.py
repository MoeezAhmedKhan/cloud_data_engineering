# Essential Subplot functions in Matplotlib

# What is subplot?
# Subplot is used to show multiple plots (charts) in a single figure (canvas).

import matplotlib.pyplot as plt

# plt.subplot(num_of_rows, num_of_columns, index)
# rows = total rows of plots
# columns = total columns of plots
# index = position number of current plot (starts from 1)

# x = [1, 2, 3, 4]
# y = [10, 30, 20, 40]

# plt.subplot(1, 2, 1)  # (1 row, 2 columns, 1st plot) → Left side
# plt.plot(x, y)
# plt.title("Line Chart")

# plt.subplot(1, 2, 2)  # (1 row, 2 columns, 2nd plot) → Right side
# plt.bar(x, y)
# plt.title("Bar Chart")

# plt.show()


# Object-Oriented (OO) Approach to Subplots
# Instead of using plt.subplot(), we create a figure (fig) and axes (ax) objects.
# fig → the whole figure (canvas/window)
# ax → array of axes objects (individual plots)

# fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
# nrows = number of rows in grid
# ncols = number of columns in grid
# figsize = size of the figure (width, height in inches)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns → ax is array of 2 plots

x = [1, 2, 3, 4]
y = [10, 30, 20, 40]

# Plot on first axes (left plot)
ax[0].plot(x, y)               # line plot
ax[0].set_title("Line Plot")   # title for first plot

# Plot on second axes (right plot)
ax[1].bar(x, y, color="green")                # bar plot
ax[1].set_title("Bar Plot")    # title for second plot

fig.suptitle("Comparison of Line and Bar Plot")     # Sub Title
fig.tight_layout()      # Adjust Plot on Figure
plt.show()  # Display the figure with both plots


