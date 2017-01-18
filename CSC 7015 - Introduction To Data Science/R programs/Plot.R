library(ggplot2)
data <- read.csv("C:/Users/Dell780/Dropbox/Personal/MS in Computer Science(Ranu)/FSU/Assignments/Introduction to Data Science/House sales.csv", header=FALSE)
attach(data)
x<- V1
y<- V3
plot(x,y)
  