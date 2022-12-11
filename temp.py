''' In this program i am trying to compare the population, 
Forest Land and Total CO2 emissions of different countries 
with two different graphs line graph and bar graph '''

#importing the important modules that need for the program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''' This method creates two data frames one is countries as columns and in
another dataset years as columns '''
def return_df(fname):
    #reading data grom the csv file
    data = pd.read_csv(fname)
    #years as columns
    df = pd.DataFrame(data)
    #columns as columns
    dataT = pd.read_csv(fname,header=None,index_col=0).T
    dfT = pd.DataFrame(dataT)
    #renaming the column to year column
    dfT = dfT.rename(columns = {"Country Name" : "Year"})
    return df,dfT

#converting the data to numeric
def converttonumbers(df,years):
    df = df.replace(to_replace=".." , value="0")
    df[years] = df[years].apply(pd.to_numeric)
    return df

#generating bar plot using the pandas dataframe
def barplot_usingDF(df,countries,y,st):
    plt.figure()
    df = df.loc[df['Country Name'].isin(countries)]
    df.plot.bar("Country Name",y)
    plt.legend(y,loc = "upper right")
    plt.ylabel(st)
    plt.show()
    
#generating the list for the total world count
def totallist(df,year,li):
    for i in year:
        li.append(df[i].sum())
    return li

#generating a list of percentage increase/decrease from the previous year
def percentageincrease(li):
    increaselist = [0]
    for i in range(2,len(li)):
        increaselist.append((li[i]*100.0/li[i-1])-100)
    return increaselist

#geb erating the line plot using the data frame
def lineplot_usingDF(df,countries,st):
    plt.figure()
    df.plot("Year",countries)
    plt.ylabel(st)
    plt.legend(countries,loc = "upper right")
    plt.show()

#generating bar plot using matplotlib bar method using lists    
def barplot(years,li,st):
    plt.figure()
    plt.bar(years,li)
    plt.ylabel(st)
    plt.legend(loc = "upper right")
    plt.show()

#generating line plot using matplotlib plot method using lists
def lineplot(years,li,st):
    plt.figure()
    plt.plot(years,li)
    plt.legend(loc = "upper right")
    plt.xlabel("Years")
    plt.ylabel(st)
    plt.show()
    
#list of countries used for the plots
countries = ["India","China","Indonesia","Pakistan","United States"]
#file path for population csv file
fnamepopulation = "C:\\Users\\hp\\Desktop\\ads 2\\population.csv"
#file path for total green house emissions equals to CO2
fnameco2 = "C:\\Users\\hp\\Desktop\\ads 2\\Total greenhouse gas emissions (kt of CO2 equivalent).csv"
#file pathfor forest area csv file
fnameforest = "C:\\Users\\hp\\Desktop\\ads 2\\Forest area (sq. km).csv"
years = ["1990","2000","2012","2013","2014","2015","2016","2017","2018","2019"]
y = ["1990","2000","2012","2019"]
f = "Forest Area"
p = "Population"
c = "Total CO2 Emission"
#generating data frames
dfpopulation,dfpopulationT = return_df(fnamepopulation)
dfco2,dfco2T = return_df(fnameco2)
#converting the coluymns to numeric using the convertnumbers method
dfco2 = converttonumbers(dfco2,years)
dfco2T = converttonumbers(dfco2T,countries)
dfforest,dfforestT = return_df(fnameforest) 
dfforest = converttonumbers(dfforest,years)
dfforestT = converttonumbers(dfforestT,countries)
#bar plots for selected countries
barplot_usingDF(dfpopulation, countries,y,p)
barplot_usingDF(dfco2, countries,y,c)
barplot_usingDF(dfforest, countries,y,f)
#line plots for selected countries
lineplot_usingDF(dfpopulationT,countries,p)
lineplot_usingDF(dfco2T,countries,c)
lineplot_usingDF(dfforestT,countries,f)
#getting the total world count for each years of respective metrics
co2world = totallist(dfco2,years,["Total world CO2 Emiinssions"])
populationworld = totallist(dfpopulation,years,["Total World Population"])
forestworld = totallist(dfforest,years,["Total World Forest Area"])
tf = "Total World Forest Area"
tp = "Total World Population"
tc = "Total World CO2 Emission"
#generating bar plot for the whole world of respective metrics
barplot(years,populationworld[1:],tp)
barplot(years,co2world[1:],tc)
barplot(years,forestworld[1:],tf)
#line plots for respective metrics of whole world
lineplot(years,populationworld[1:],tp)
lineplot(years,forestworld[1:],tf)
lineplot(years,co2world[1:],tc)
reqdata = dict(zip([tc,tp,tf] , [percentageincrease(co2world),percentageincrease(populationworld),percentageincrease(forestworld)]))
reqdata.update({"Year" :years})
reqdata = pd.DataFrame(reqdata)
#line plot of respective metrics of the percentage increase / decrease of the world
lineplot_usingDF(reqdata, [tc,tp,tf],"Percentage Increase from previos year")
