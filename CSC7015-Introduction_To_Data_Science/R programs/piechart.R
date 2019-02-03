# Pie Chart with Percentages
slices <- c(10, 12, 4, 16, 8) 
lbls <- c("US", "UK", "Australia", "Germany", "France")
pct <- round(slices/sum(slices)*100)
lbls <- paste(lbls, pct,"%") # add percents to labels 
pie(slices,lbls, col=rainbow(length(lbls)),
    main="Pie Chart of Countries")
