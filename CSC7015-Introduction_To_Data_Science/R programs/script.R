#load file
home <- read.csv("../input/kc_house_data.csv", header = T)

#load libraries
library(dplyr)
library(plyr)
library(Hmisc)
library(ggplot2)
library(lubridate)
library(corrplot)

#get the outline of data
str(home)
describe(home)
head(home)
tail(home)

#CLEANING THE DATA.
#convert date from factor to date class.
home$date <- as.Date(as.Date(as.character(home$date), "%Y%m%d"))

#with use of lubridate we split the data date by year, week and day of the year.
home$Year <- year(home$date)
home$week <- week(home$date)
home$Day <- yday(home$date)
home$month <- month(home$date)

#Exploring the data - Basic Exploratory plots of the data
#price
ggplot(home, aes(home$price)) + stat_bin(bins = 100, colour="black", fill="green") +
  labs(x= "Price",y= "Frequency" , title = "Histogram of Price") + xlim(0,4000000) +
  scale_fill_discrete()
#bedrooms
ggplot(home, aes(home$bedrooms)) + stat_bin(bins = 13, colour="black", fill="green") +
  labs(x= "Number of Bedrooms",y= "Frequency" , title = "Histogram of Number of Bedrooms") + xlim(0,10)  +
  scale_fill_discrete()
#bathrooms
ggplot(home, aes(home$bathrooms)) + stat_bin(bins = 30, colour="black", fill="green") +
  labs(x= "Number of Bathrooms",y= "Frequency" , title = "Histogram of Number of Bathrooms") + xlim(0,7) +
  scale_fill_discrete()
#view
qplot(home$view, main = "Plot of House View" , xlab = "View" , ylab = "Frequency")
#sqft_lot
ggplot(home, aes(home$sqft_lot)) + stat_bin(bins = 30, colour="black", fill="green") +
  labs(x= "Sqft Lot",y= "Frequency" , title = "Histogram of Sqft Lot") + xlim(0, 120000) +
   scale_fill_discrete()
#sqft_above
ggplot(home, aes(home$sqft_above)) + stat_bin(bins = 30, colour="black", fill="green") +
  labs(x= "Sqft Above",y= "Frequency" , title = "Histogram of Sqft Above") + xlim(0, 8000) +
  scale_fill_discrete()
#condition
qplot(home$condition , main = "Plot of House Condition" , xlab = "House Condition" , ylab = "Frequency")

#checking correlation between variables
homecor <- cor(home[3:14])
#plotting correlation
corrplot(homecor, type="upper", order="hclust", tl.col="black", tl.srt=45)

#from correlation plot we identify that there is a strong relationship between price and sqft_living , grade and sqft_above.

#Regression
#Checking Linearity
scatter.smooth(x=home$price, y=home$bedrooms, main="Price ~ Bedrooms")
scatter.smooth(x=home$price, y=home$bathrooms, main = "Price ~ Bathrooms")
scatter.smooth(x=home$price, y=home$sqft_living, main ="Price ~ Sqft Living")
scatter.smooth(x=home$price, y=home$floors, main = "Price ~ Floors")
scatter.smooth(x=home$price, y=home$condition, main = "Price ~ Condition")
scatter.smooth(x=home$price, y=home$grade, main = "Price ~ Grade")
scatter.smooth(x=home$price, y=home$sqft_above, main = "Price ~ Sqft Above")
scatter.smooth(x=home$price, y=home$sqft_basement, main = "Price ~ Sqft Basement")

#Building a linear model on full data.
lm.pr1 <- lm(price ~ sqft_living , data = home)
#get the coefficients
print(lm.pr1$coefficients)
#from the summary we can assume that price = -43580.7 + 280.6*sqft_living
summary(lm.pr1)
plot(lm.pr1)

#assesing the model performance. Calculating RMSE.
price_est <- predict(lm.pr1)
pres <- home$price - price_est
rmse <- sqrt(mean(pres^2))
rmse
#RMSE appears to be 261440.8$
#MAE
mae <- mean(abs(home$price - price_est))
mae
#MAE appears to be 173688.3
#R squared
summary(lm.pr1)$r.squared
#R squared is 0.49


#Predicting a linear model

#splitting data. 70% train - 30% test.
set.seed(100)
trainingRowIndex <- sample(1:nrow(home), 0.7*nrow(home))
train <- home[trainingRowIndex, ]
test <- home[-trainingRowIndex,]

#Developing the model on test data.
lm.prtest <- lm(price ~ sqft_living , data = train)
pricepred <- predict(lm.prtest , test)
summary(lm.prtest)

#from summary we see that we have a significant model since p is less than significance level. Also , R squared and Adjusted R
#Squared are close to the values that we got from the model we built on full data.

#Calculate prediction accuracy and error rates
actuals_preds <- data.frame(cbind(actuals=test$price, predicteds=pricepred))
correlation_accuracy <- cor(actuals_preds) #70% accuracy
head(correlation_accuracy)
#min max accuracy
min_max_accuracy <- mean(apply(actuals_preds, 1, min) / apply(actuals_preds, 1, max))  #74% min max accuracy



#Multivariable regression
#Building a regression based on sqft_living , grade and sqft_above. First with full data. Then with test data and then test 
#the model with test set.
lm.multi <- lm(price ~ sqft_living + grade + sqft_above , data = train)
summary(lm.multi)
plot(lm.multi)
#all variables are significant since p is smaller than 0.05. 
#Multiple R squared and R squared are both 0.54 

mult.pred <- predict(lm.multi, test)
#RMSE
RMSE.lin.reg <- sqrt(mean((mult.pred-test$price)^2))
RMSE.lin.reg
#RMSE is 247786.8

#MAE
MAE.lin.reg <- mean(abs(mult.pred-test$price))
MAE.lin.reg
#MAE is 160692.9




