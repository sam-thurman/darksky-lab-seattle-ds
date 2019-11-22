
# Introduction

For today's section, we're going to work on a single big lab to apply what we've learned so far about APIs, databases and hypothesis testing! We will be making use of SQLite and MongoDB Atlas

### About This Lab

A quick note before getting started--this lab isn't like other labs you seen so far. This lab is meant to take the whole day to complete, so it's much longer and more challenging than the average labs you've seen so far. If you feel that you might be struggling a bit, don't fret--that's by design! With everything we've learned about statistics, APIs, and Databases, the best way to test our knowledge of it is to build something substantial!

# The Context

You have just started your new job on the data science team at ESPN. The team is very busy and on an extremely tight deadline. Your new boss has asked you to solve two problems on your first day:


### 1. Designing a Data Pipeline
Every year we need to move our raw data from a SQLite database, aggregate it, and store it in a MongoDB Atlas instance where all of our different analysts can have access to these statistics. In order to make this process as painless as possible you are charged with automating this once long and tedious process.

Create a function which will take the Season as an argument and execute the following:
```python
def pipeline(season):
    pass
```
* Aggregate match statistics from a SQLite database in the file `database.sqlite`
    * A data dictionary available [here](https://www.kaggle.com/laudanum/footballdelphi)
* Combine match information with weather data from the [DarkSky API](https://darksky.net/dev)
* Insert data into MongoDB Atlas where each record contains the following information:
   * Team Name
   * League (either English Premier League (E0) or Bundesliga (D1))
   * Season
   * Total number of goals scored by the team during the season
   * Total number of wins the team earned during the season
   * Team's win percentage on days where it was raining during games in the season

#### Getting the Weather Data

Note that for this last calculation, you'll need to figure out if it was raining or not during the game. The database itself does not contain this information, but it does contain the date on which the game was played. For this, you'll need to use the [DarkSky API](https://darksky.net/dev) to get the historical weather data for that day. Note that each game is played in a different location, and this information is not contained in our SQL database. However, the teams in this database are largely German, so go ahead and just use the weather in Berlin, Germany as a proxy for this information. If it was raining in Berlin on the day the game was played, count that as rain game--**_you do not need to try and figure out the actual weather at each game's location, because we don't have that information!_**

**NOTE: The DarkSky API is limited to 1000 free API calls a day, so be sure to test your model on very small samples. Otherwise, you'll hit the rate limit!**

### Rapid Prototyping and Refactoring

When experimenting with the DarkSky API for getting historical weather data, it makes sense to just write the code in the cells and rapidly iterate until you get it all working. However, once you get it working, you're not done--you should then **_Refactor_** your code into functions to make your code more modular, reusable, understandable, and maintainable!

In short--do what you need to do to get each separate piece of functionality working, and then refactor it into functions after you've figured it out!

### MongoDB Atlas

To set up your MongoDB Atlas instance follow these [directions](https://docs.google.com/document/d/1ghOi6jd0Nw4jOOOevuUpncuRAEOdEEC28NUI0pqUyFA/edit)

If you need a refresher on using MongoDB check out their docs [here.](https://api.mongodb.com/python/current/tutorial.html)

#### Deliverables
- A well documented `.py` file containing all of your code for the pipeline function
- Insert data from the 2016/17 and 2017/18 season from the SQLite database into your MongoDB Atlas instance

----------------------------------------------------------------------------------------------------

### 2. Hypothesis Testing
By the end of day today ESPN needs to make a decision about which European league broadcasting rights it wants to buy. The budget for the team only allows us to purchase the rights to either the English Premier League or the German Bundesliga. Your boss has decided that American audiences are more likely to tune into soccer games where there are a high number of goals scored and she has a hunch that the English Premier League has a higher goals per game. We need you to run an analysis of the two leagues to test her hunch:

__Does the English Premier League have more goals per game than in Bundesliga in the 2017/2018 season?__


#### Deliverable
The deliverable here is a well documented jupyter notebook detailing your process and provide a final recommendation to your boss regarding the broadcasting rights. Make sure that you define the null and alternative hypotheses, and describe which statistical test you used and why it is appropriate. All assumptions you are making should be made explicit.

### Some Final Advice

You haven't built anything this big or complex thus far, so you may not yet fully realize how much trial and error goes into it. If your code keeps breaking, resist the urge to get frustrated, and just keep working. Software development is an iterative process!  No one writes perfect code that works the first time for something this involved. You're going to run into _a lot_ of small errors in this project, right up until the point where it just works, and then you're done! However, you can reduce these errors by planning out your code, and thinking about how all of the pieces fit together before you begin coding. Once you have some basic understanding of how it all will work, then you'll know what you need to build, and then all that is left is to build it!

In short:

* Plan ahead--you'll thank yourself later!
* Errors and broken code aren't bad, they're normal. 
* Keep working, and stay confident--you can do this!

Good luck--we look forward to seeing your completed project!

# Summary

In this lab, we dug deep and used everything we've learned so far about Python programming, databases, HTTP requests and API calls to ETL data from a SQL database into a MongoDB Atlas instance!
