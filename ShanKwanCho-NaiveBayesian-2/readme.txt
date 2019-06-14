

Brief description

First of all, familiar with the Tableau
I tried to find the corelationship between individual colum (age, workclass, ...etc ) with comparing with the income.
On Tableau, I basically added the sheet and rename into sex , income , age , etc and for each attributes..
For example, to visualize the co-relationship between two attributes, i put 'age' in columns and rows for number of measures and
add the income into the color tab to visualize. Those can be applied into many attributes with same approach.
For Binning, i did for Age, Capital-gain , capital-loss and hours per week.


#handling missing values!
i approached two ways for handling missing mode_values.
This is done with the Google Colab IDE.
The first one is basically filling the missing values like ? with the mode of the attributes
I find the mode of the attributes(workclass,occupation,native_country) and replace with the mode result of each attributes.
Workload can be see in the Preprocess folder and test folder.
The second one is basically drop the rows of the missing values by using the dropna hard-code :
df = df.replace(' ?',np.nan).dropna(axis=0)  <- this apply for each attributes
Especially the rows that contain ? in each attributes


#Naive Bayes
For implementation of naive bayes, what I understand so far is upon given dataset, we have X1= <=50K and X2 = >50k
From the equation,(  P(x1| y1,y2,y3,...) = p(y1,y2,y3,...|x1) times p(x1) ) / (p(y1,y2,y3,...))
similarity = (  P(x1| y1,y2,y3,...) = p(y1,y2,y3,...|x1) times p(x2) ) / (p(y1,y2,y3,...))
by ratio, we can obmit the (p(y1,y2,y3,...)) (dinominator)
we need to find the probability of each P(x1) and p(x2) for each attributes
for example, p(y1=y|x1) = p(y1=y,x1) / p(x1) = number of <=50K and <=50 / number of <= 50K  similarity to p(x2)
We find the probability of each attributes by creating the list and input them into and update those probability and return as list.
As in main function, pass all the dict together and compare with the income to predict the list with trian and test set.
