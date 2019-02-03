data <- read.csv("D:\\Dropbox\\Personal (2)\\MS in Computer Science(Ranu)\\FSU\\Assignments\\Introduction to Data Science\\Housesales.csv" , header=TRUE)
View(data)

head(data)
tail(data)

class(data)

dim(data)
str(data)
summary(data)
names(data)
library(dplyr)
glimpse(data)