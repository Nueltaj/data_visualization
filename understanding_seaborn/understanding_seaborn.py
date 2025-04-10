# """understanding seaborn"""

# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.get_dataset_names()
# iris =sns.load_dataset("iris")
# planets =sns.load_dataset("planets")
# tips =sns.load_dataset("tips")
# titanic=sns.load_dataset("titanic")
# #plotting a scatter plot
# #showing the correlation between the tips and the tota bill
# # sns.scatterplot(x="tip",y="total_bill",data=tips,hue="day",size="size",palette="dark")
# # print(tips)

# #plotting a histogram
# #showing the distributation of numerical data
# # sns.histplot(tips["total_bill"],kde=True,bins=30)
# # plt.show()

# #plotting a barchart
# #compare categorical data
# # sns.barplot(data=tips,x="sex",y="tip",palette="dark")
# # plt.show()

# #plotting a boxplot
# #used to show data distributrion,man and quartiles
# # sns.boxplot(data=tips,x="day",y="tip",hue="sex",palette="dark")
# # plt.show()

# #plotting a pairplot
# #used to show automatic grid+scatterplots for all numerical columns
# # sns.pairplot(titanic.select_dtypes(["number"]),hue="pclass",palette="dark")
# # plt.show()

# #plotting a heatmap
# #used to show correlation
# # titanic_numeric_values=titanic.select_dtypes(["number"]).corr()
# # sns.heatmap(titanic_numeric_values,annot=True)
# # plt.show()

# #plotting a countplot
# #shows the number of times a category occurs
# # sns.countplot(x="sex",data=tips)
# # plt.show()

import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  

# Sample data  
data = {  
    'Category': ['A', 'A', 'B', 'B'],  
    'Value': [10, 20, 15, 25],  
    'Group': ['Group 1', 'Group 2', 'Group 1', 'Group 2']  
}  

# Create a DataFrame  
df = pd.DataFrame(data)  

# Create the bar plot  
plt.figure(figsize=(8, 5))  
sns.barplot(data=df, x='Category', y='Value', hue='Group', palette='muted')  

# Add title and labels  
plt.title('Two Bar Charts Combined')  
plt.xlabel('Category')  
plt.ylabel('Value')  

# Show the plot  
plt.legend(title='Groups')  
plt.show()  