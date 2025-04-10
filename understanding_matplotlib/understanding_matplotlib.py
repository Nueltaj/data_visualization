# # """understanding matplotlib"""

# import numpy as np
# import pandas as pd
#import matplotlib.pyplot as plt
# # import random
# # from matplotlib import style


# # # using the matplotlib package to create a scatter plot
# # # x_data = np.random.random(500) * 100
# # # y_data = np.random.random(500) * 100

# # # plt.scatter(x_data, y_data, s=10,c="black", marker="*", alpha=0.3)
# # # plt.show()


# # # using the matplotlib package to create a line chart
# # # linechart is preferably used when comparing data and mostly related to time
# # # years = [2000 + x for x in range(25)]
# # # weight =np.linspace(80,100,25)
# # # #shuffles the order of the weight
# # # np.random.shuffle(weight)
# # # plt.plot(years,weight,c="g",lw=3,linestyle="--")
# # # plt.show()


# # # using the matplotlib to create a barchart
# # # we use a barchart when we want to display categorical data ex:poll
#y = [20, 100, 10, 1, 50]
#plt.bar(x, y, color="red", align="center", width=0.6, edgecolor="green",lw=1)
#plt.show()

# # # using matplotlib to create a histogram
# # # we use histogram when we want to display numerical data
# # # also to know the frequency of occurences acrossed intervals
# # # ages = np.random.normal(20,1.5,1000)
# # # plt.hist(ages, bins= 20, cumulative=True)
# # # plt.show()


# # # using matplotlib to create a pie chart
# # # we use pie chart when it comes to categorical data
# # # to make comparisons
# # # langs = ["C++", "python", "java", "R", "C#"]
# # # votes = [50, 24, 17, 6, 25]
# # # # using explode to remove a certain section of the pie chart
# # # explodes = [0, 0, 0, 0.3, 0]
# # # plt.pie(votes, labels=langs, explode=explodes, autopct="%.2f%%",pctdistance=0.8)
# # # plt.show()


# # # using matplotlib to create a boxplot
# # # we use boxplot to determine the quartiles,mean,median
# # # heights=np.random.normal(172,8,300)
# # # plt.boxplot(heights)
# # # plt.show()


# # # customization of plots
# # # years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
# # # income = [55, 56, 62, 61, 72, 72, 73, 75]
# # # income_ticks = list(range(50, 81, 2))
# # # plt.plot(years, income)
# # # plt.title("Income of John in (USD)", fontsize=20, fontfamily="FreeMono")
# # # plt.xlabel("Year")
# # # plt.ylabel("Annual Income in (USD)")
# # # plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])
# # # plt.show()

# # # legends
# # # stock_a = [109, 102, 99, 101, 103, 100, 102]
# # # stock_b = [99, 99, 102, 104, 105, 103, 109]
# # # stock_c = [110, 115, 100, 105, 100, 98, 99]
# # # plt.plot(stock_a,label="XIAOMI")
# # # plt.plot(stock_b,label="APPLE")
# # # plt.plot(stock_c,label="SAMSUNG")
# # # plt.legend(loc="upper center")
# # # plt.show()

# # # using legend in piechart
# # # langs = ["C++", "python", "java", "R", "C#"]
# # # votes = [50, 24, 17, 6, 25]
# # # plt.pie(votes, labels =
# # # None, autopct="%.2f%%",pctdistance=0.8)
# # # plt.legend(labels=langs)
# # # plt.show()

# # # using style
# # # style.use("dark_background")
# # # #check the documentation
# # # langs = ["C++", "python", "java", "R", "C#"]
# # # votes = [50, 24, 17, 6, 25]
# # # plt.pie(votes, labels =
# # # None, autopct="%.2f%%",pctdistance=0.8)
# # # plt.legend(labels=langs)
# # # plt.show()


# # # x = np.arange(100)
# # # fig, axs = plt.subplots(2, 2)
# # # axs[0, 0].plot(x, np.sin(x))
# # # axs[0, 0].set_title("Sine Wave")

# # # axs[0, 1].plot(x, np.cos(x))
# # # axs[0, 1].set_title("Cosine Wave")

# # # axs[1, 0].plot(x, np.random.random(100))
# # # axs[1, 0].set_title("Random Function")

# # # axs[1, 1].plot(x, np.log(x))
# # # axs[1, 1].set_title("Logarithm")
# # # axs[1, 1].set_xlabel("Test")

# # # plt.tight_layout()
# # # #plt.show()
# # # plt.suptitle("Four Plot")
# # # plt.savefig("four_plot.png", dpi=300)


# # #3D projextion

# # # ax = plt.axes(projection="3d")
# # # x = np.random.random(50)
# # # y= np.random.random(50)
# # # z= np.random.random(50)
# # # ax.scatter(x,y,z)
# # # ax.set_title("3d projection")
# # # plt.show()

# # # #3d projection with surface
# # # ax=plt.axes(projection="3d")
# # # x=np.arange(-5,5,0.1)
# # # y=np.arange(-5,5,0.1)
# # # X,Y= np.meshgrid(x,y)

# # # Z=np.sin(X)*np.cos(Y)
# # # ax.plot_surface(X,Y,Z,cmap="twilight")
# # # ax.set_title("3d Plot")
# # # ax.set_xlabel("Test")
# # # plt.show()

# # #animation
# # heads_tails = [0, 0]  # Initialize a list to count heads and tails

# # for _ in range(100000):
# #     heads_tails[random.randint(0, 1)] += 1  # Randomly increment heads or tails count
# #     plt.bar(['Heads', "Tails"], heads_tails, color=["red", "blue"])  # Update bar chart
# #     plt.pause(0.001)  # Brief pause to visualize animation
# # plt.show()  # Display the final chart
# #radar chart
# #define the circle(radar foundation)
# circle=np.linspace(0, 2*np.pi, 5,endpoint=False).tolist()
# #copy the list
# circle+=circle[:1]
# attributes=["Power","Speed","Strength","Intelligence","Flight"]
# values=[90,80,75,90,75]
# #creates a circle
# values+=values[:1]

# #initialize a radar chart
# ax=plt.subplot(polar=True)

# #adjust x ticks(set branches)
# plt.xticks(circle[:-1], attributes)
# #set the yticks(scale)
# ax.set_rlabel_position(0)
# plt.yticks([20,40,60,80,100],["20","40","60","80","100"])
# plt.ylim(0,100)
# #add data
# ax.plot(circle,values)
# ax.tick_params(direction='out', length=6, width=2, colors='r',
#                    grid_color='r', grid_alpha=0.5,pad=20)
# #fill the radar chart with color
# ax.fill(circle,values,alpha =0.3)
# plt.title("Iron Man",loc="center",y=1.1)
# plt.show()

