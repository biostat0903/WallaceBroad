#!/usr/bin/env Rscript

## @Wallace Wang, wavefancy@gmail.com
##
## Do multiple linear regression, output residuals.
## Read data with header from stdin, and output results to stdout.
## The first column is the dependent variable.
## From second to last, are independent variables.

# clotting <- data.frame(
#   u = c(0,0,0,0,0,1,1,1,1),
#   lot1 = c(118,58,42,35,27,25,21,19,18),
#   lot2 = c(69,35,26,21,18,16,13,12,12))

#dd = read.table("test.txt",header = T)
dd = read.table(file("stdin"),header = T)
# https://stackoverflow.com/questions/4951442/formula-with-dynamic-number-of-variables
# auto convert the colnames as formula.
form = sub('\\+','~',paste(colnames(dd), collapse = '+'))

# print(c("FORMULA:",form))
# print(form)
write(c("FORMULA:",form), stderr())

lr = lm(as.formula(form),data = dd)
write.table(resid(lr),"",row.names=F,col.names=F)
