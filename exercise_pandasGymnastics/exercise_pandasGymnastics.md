# The exercises:

	1) Load the nutrition, physical activity and obesity survey dataset

[nutrition, physical activity and obesity survey dataset](https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system)

	2) Find out how many of the college graduates in the state of Washington consume fruits less than 1 time a day
		Sub questions:
		2.1 What are the column names?
		2.2 Is there an explicit index?
		2.3 What are all the unique topics in the topics column?
		2.4 For surveys on Fruits, what are the unique questions?
		2.5 How many surveys have there been on fruit consumption in the state of Washington?

	3) Make a choropleth of the states in the US for the percentage of overweight adults in 2011
		Sub steps:
		3.1 create a smaller dataFrame that only contains studies started in 2011 (df.YearStart == 2011), for the overall population (df.StratificationID1== 'OVERALL', for question 36 (df.QuestionID =='Q036'), and exclude the US overall stats (df.LocationAbbr !='US'))
		3.2 Sort the states for percentage of obese people (just to verify your later results)
		3.3 Install Chorogrid
		(3.4 optional) Come up with your own colorscheme on colorbrewer
		3.5 Plot the choropleth using Chorogrid
[Colorbrewer2.org](http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3)


![](http://3.bp.blogspot.com/-A-u151ml9D0/UOtevVSU4bI/AAAAAAAAKcE/4eeruUdZWCg/s640/1818.jpg)
