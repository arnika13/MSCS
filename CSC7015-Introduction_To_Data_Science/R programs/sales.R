library(ggplot2)
library(lubridate)
library(corrgram)
library(corrplot)

HouseDataSet <- read.csv(file.choose(), header = TRUE)
View(HouseDataSet)  #display the complete data set
dim(HouseDataSet)   #OBS-21613 variables- 21

#DIPLAY THE OUTLINE OF THE DATA

summary(HouseDataSet)  #summary of dataset
str(HouseDataSet)      #structure of dataset
class(HouseDataSet)    #class of objects
head(HouseDataSet)     #display the first 6 objects
tail(HouseDataSet)     #display the last 6 objects

##DATA CLEANING

HouseDataSet$date <- as.Date(as.Date(as.character(HouseDataSet$date),"%Y%m%d"))

#sPLITTING THE DATA INTO TRAIN AND TEST DATA 

indexes = sample(1:nrow(HouseDataSet), size = 0.3*nrow(HouseDataSet))

Test_data = HouseDataSet[indexes,] #Test dataset 30%
dim(Test_data)                     # Obs-6483, variable- 21
str(Test_data)
Train_data = HouseDataSet[-indexes,] #Train dataset 70%
dim(Train_data)                      #Obs-15130,Variable-  21
str(Train_data)
table(is.na(Train_data)) # To check whether the data in train dataset is missing or not

#FINDING THE CORRELATION

Attribute_Corr <-cor(Train_data[3:21],method="pearson")
View(Attribute_Corr)

#PLOTTING THE CORRELATION

corrplot(Attribute_Corr,type="upper",method="color",addCoef.col = "black", title = "Correlation between the attributes", number.cex = 14/ncol(Train_data[3:21]), mar=c(1,1,1,1))

##Display the linearity between price and other independent variables

#Price ~ SqftLiving
scatter.smooth(x=Train_data$sqft_living, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ SqftLiving")
#Price ~ bedrooms
scatter.smooth(x=Train_data$bedrooms, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ bedrooms")
#Price ~ bathrooms
scatter.smooth(x=Train_data$bathrooms, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ bathrooms")
#Price ~ Sqf_lot
scatter.smooth(x=Train_data$sqft_lot, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ Sqf_lot")
#Price ~floors
scatter.smooth(x=Train_data$floors, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ floors")
#Price ~ waterfront
scatter.smooth(x=Train_data$waterfront, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ waterfront")
#Price ~ view
scatter.smooth(x=Train_data$view, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ view")
#Price ~ condition
scatter.smooth(x=Train_data$condition, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ condition")
#Price ~ grade
scatter.smooth(x=Train_data$grade, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ grade")
#Price ~ Sqft_above
scatter.smooth(x=Train_data$sqft_above, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ Sqft_above")
#Price ~ sqft_basement
scatter.smooth(x=Train_data$sqft_basement, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ sqft_basement")
#Price ~ yr_built
scatter.smooth(x=Train_data$yr_built, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ yr_built")
#Price ~ yr_renovated
scatter.smooth(x=Train_data$yr_renovated, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ yr_renovated")
#Price ~ zipcode
scatter.smooth(x=Train_data$zipcode, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ zipcode")
#Price ~ lat
scatter.smooth(x=Train_data$lat, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ lat")
#Price ~ long
scatter.smooth(x=Train_data$long, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ long")
#Price ~ SqftLiving15
scatter.smooth(x=Train_data$sqft_living15, y=Train_data$price,lpars =list(col = "red", lwd = 1, lty = 1), main = "Price ~ SqftLiving15")
#Price ~ Sqft_lot15
scatter.smooth(x=Train_data$sqft_lot15, y=Train_data$price,lpars=list(col = "red", lwd = 1, lty = 1), main = "Price ~ Sqft_lot15") 


#Creating a regression model
#all attributes

Housemodel_all <- lm(log(price) ~ bedrooms+bathrooms+sqft_living+sqft_lot+floors+waterfront+view+condition+grade+sqft_above+sqft_basement+yr_built+yr_renovated+lat+long+sqft_living15+ sqft_lot15, data = Train_data)
summary(Housemodel_all)
summary(Housemodel_all)$coefficients

# First model

Housemodel_1 <- lm(price ~ bedrooms+bathrooms+sqft_living+floors+waterfront+view+condition+grade+sqft_above+yr_built+yr_renovated+lat+long+sqft_living15+ sqft_lot15, data = Train_data)
summary(Housemodel_1)
summary(Housemodel_1)$coefficients ##Multiple R-squared:  0.6948

Housemodel_i1<- lm(log(price) ~ bedrooms+bathrooms+sqft_living+floors+waterfront+view+condition+grade+sqft_above+yr_built+yr_renovated+lat+long+sqft_living15+ sqft_lot15, data = Train_data)
summary(Housemodel_i1)# Multiple R-Squared : 0.7684

# Second model

Housemodel_2 <- lm(price ~ bedrooms+sqft_basement+bathrooms+waterfront+grade+yr_built, data = Train_data)
summary(Housemodel_2)
summary(Housemodel_2)$coefficients ##Multiple R-squared:  0.6003


# Third Model

Housemodel_3 <- lm(price ~ bedrooms+sqft_basement+bathrooms+waterfront+grade+yr_built+yr_renovated, data = Train_data)
summary(Housemodel_3)##Multiple R-squared:  0.6004
summary(Housemodel_3)$coefficients

#Fourth model
Housemodel_4 <- lm(price ~ bedrooms+bathrooms+sqft_living+sqft_lot+floors+waterfront+view+grade+sqft_above+sqft_basement+yr_renovated+lat+sqft_living15, data = Train_data)
summary(Housemodel_4)##Multiple R-squared:  0.6653
summary(Housemodel_4)$coefficients

#Fifth model
Housemodel_5 <- lm(price ~ +sqft_living+sqft_basement+sqft_lot+view+bedrooms+grade+waterfront, data = Train_data)
summary(Housemodel_5) ##Multiple R-squared:  0.5976

#Sixth Model
Housemodel_6 <- lm(price ~ bedrooms+bathrooms+sqft_living+floors+waterfront+view+condition+grade+sqft_above+yr_built+yr_renovated+sqft_living15+ sqft_lot15, data = Train_data)
summary(Housemodel_6) ##Multiple R-squared:  0.6537

#Seventh Model
Housemodel_7 <- lm(price ~ bedrooms+bathrooms+sqft_living+sqft_lot+floors+waterfront+view+condition+grade+sqft_above+sqft_basement+yr_built+yr_renovated+lat+long+sqft_living15+ sqft_lot15, data = Train_data)
summary(Housemodel_7) 

#bedrooms+bathrooms+sqft_living+sqft_lot+floors+waterfront+view+condition+grade+sqft_above+sqft_basement+yr_built+yr_renovated+lat+long+sqft_living15+ sqft_lot15
##Appliying the model to the Test data

pred <- predict(Housemodel_i1,Test_data)
summary(pred)

#View(predict.lm(Housemodel_1,Test_data))

View(pred)
View(cbind("ID"=Test_data$id,"Orginal Price"=Test_data$price,"New predicted price"=exp(pred))) ##display the original price and predicted price


  
