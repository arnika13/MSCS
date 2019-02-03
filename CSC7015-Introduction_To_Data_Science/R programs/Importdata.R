library(ggplot2)
library(lubridate)
library(corrgram)
library(corrplot)

Housedata <- read.csv("C:\\Users\\Dell780\\Dropbox\\Personal\\MS in Computer Science(Ranu)\\FSU\\Assignments\\Introduction to Data Science\\Housesales.csv", header=TRUE)
View(Housedata)

# outline of the data

str(Housedata) 
class(Housedata)
summary(Housedata)
head(Housedata)
tail(Housedata)

# Cleaning the data

Housedata$date <- as.Date(as.Date(as.character(Housedata$date),"%Y%m%d"))




# Exploring the data-Basic exploratory plots of the data

#price

ggplot(Housedata,aes(Housedata$price)) + stat_bin(bins = 50, colour="black", fill="pink") +
  labs(x= "Price",y= "Frequency" , title = "Histogram of Price") + xlim(0,4000000)

 

#Bedrooms

ggplot(Housedata,aes(Housedata$bedrooms)) + stat_bin(bins = 13, colour="black", fill="pink") +
  labs(x= "Number of Bedrooms",y= "Frequency" , title = "Histogram of Number of Bedrooms") + xlim(0,10)  
  

#bathrooms

ggplot(Housedata,aes(Housedata$bathrooms)) + stat_bin(bins = 30, colour="black", fill="yellow") +
  labs(x= "Number of Bathrooms",y= "Frequency" , title = "Histogram of Number of Bathrooms") + xlim(0,7)

# Sqft_living

ggplot(Housedata,aes(Housedata$sqft_living)) + stat_bin(bins = 30, colour="black", fill="yellow") +
  labs(x= "Sqft_living",y= "Frequency" , title = "Histogram of Number of sqft_living") + xlim(0,7000) +ylim(0,5000)
 

# sqft_lot

ggplot(Housedata,aes(Housedata$sqft_lot)) + stat_bin(bins = 30, colour="black", fill="yellow") +
  labs(x= "Sqft_lot",y= "Frequency" , title = "Histogram of Number of sqft_lot") + xlim(0,120000)

# view

qplot(Housedata$view, main = "Plot of House View" , xlab = "View" , ylab = "Frequency" , binwidth=0.1,  fill= "pink")

# Condition

qplot(Housedata$condition , main = "Plot of House Condition" ,geom="histogram", xlab = "House Condition" , ylab = "Frequency",colour="black",fill="pink")

# sqft_above

ggplot(Housedata, aes(Housedata$sqft_above)) + stat_bin(bins = 30, colour="blue", fill="yellow") +
  labs(x= "Sqft Above",y= "Frequency" , title = "Histogram of Sqft Above") + xlim(0, 8000)

#yrbuilt

ggplot(Housedata, aes(Housedata$yr_built)) + stat_bin(bins = 100, colour="blue", fill="yellow") +
  labs(x= "yr_built",y= "Frequency" , title = "Histogram of Year Built") + xlim(0, 3000)


#Checking the correlation between the variables usding pearson method

Housecor<- cor(Housedata[3:15])
cor(Housedata[3:15],method="pearson")

cor.test(Housedata$price,Housedata$bedroom,method="pearson")
cor.test(Housedata$price,Housedata$waterfront,method="pearson")
cor.test(Housedata$price,Housedata$condition,method="pearson")

# plotting the correlation

corrgram(Housedata, order= TRUE ,lower.panel= panel.shade,upper.panel=NULL,text.panel=panel.txt )
corrplot(Housecor, type="upper", order="hclust", tl.col="black", tl.srt=45)

## Regression-Checking linearity

scatter.smooth(x=Housedata$price, y=Housedata$bedrooms, main="Price ~ Bedrooms")
scatter.smooth(x=Housedata$price, y=Housedata$bathrooms, main = "Price ~ Bathrooms")
scatter.smooth(x=Housedata$price, y=Housedata$sqft_living, main ="Price ~ Sqft Living")
scatter.smooth(x=Housedata$price, y=Housedata$floors, main = "Price ~ Floors")
scatter.smooth(x=Housedata$price, y=Housedata$condition, main = "Price ~ Condition")
scatter.smooth(x=Housedata$price, y=Housedata$grade, main = "Price ~ Grade")
scatter.smooth(x=Housedata$price, y=Housedata$sqft_above, main = "Price ~ Sqft Above")
scatter.smooth(x=Housedata$price, y=Housedata$sqft_basement, main = "Price ~ Sqft Basement")

#Linear Model on full data

lm.pr1 <- lm(price ~ sqft_living+bathrooms+bedrooms , data = Housedata)
lm.pr2 <- lm(price ~ bedrooms , data = Housedata)
print(lm.pr1$coefficients)
print(lm.pr2$coefficients)
summary(lm.pr1)
summary(lm.pr2)
