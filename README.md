# Flight Delays in Four Major Airports in Three Major Cities

## Research Question

How does rain affect departure delay time in July and December, heavy travel months, from 2013 to 2018 in four major airports (John F. Kennedy, La Guardia, Miami, and Los Angeles) in New York, NY, Miami, FL, and Los Angeles, CA?

## Data
* [DarkSky API](https://darksky.net/dev)
    * Time period: July, December 2013-2018
    * Daily weather data for Los Angeles, CA, Miami, FL, and New York, NY
    * 930 data points


* [Bureau of Transportation Statistics](https://transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)
    * Time period: July, December 2013-2018
    * Flight data for all flights between Los Angeles, CA, Miami, FL, and New York, NY
    * 50,000+ data points

## Variables of Interest
* Weather Data
    * **precip_type:** precipitation type (no precipitation, rain, sleet, or snow)
        * for our purposes, we only looked at no precipitation and rain conditions

|             date |           origin |      precip_type |
| ---------------- | ---------------- | ---------------- |
|       2013-07-01 |  Los Angeles, CA | No Precipitation |
|       2013-07-01 |        Miami, FL |             rain |
|       2013-07-01 |     New York, NY |             rain |
|       2013-07-02 |  Los Angeles, CA | No Precipitation |
|       2013-07-02 |        Miami, FL |             rain |

|      precip_type | # of Flights Affected | Std. Dev. of Departure Delay |
| ---------------- | --------------------- | ---------------------------- |
| No Precipitation |                33,761 |                       42.922 |
|             rain |                17,793 |                       57.723 |
|            sleet |                    66 |                       19.241 |
|             snow |                   578 |                       42.383 |

* Flights Data
    * **origin:** airport from which flight is departing
    * **dep_delay:** departure delay time in minutes
    
|   flight_id |       date |     origin |  dep_delay |
| ----------- | ---------- | ---------- | ---------- |
|           1 | 2013-07-01 |        LAX |       -4.0 |
|           2 | 2013-07-01 |        LAX |      257.0 |
|           3 | 2013-07-01 |        LAX |      110.0 |
|           4 | 2013-07-01 |        LAX |       25.0 |
|           5 | 2013-07-01 |        LAX |       -1.0 |

|        origin | # of Flights | Std. Dev. of Departure Delay |
| ------------- | ------------ | ---------------------------- |
|           JFK |       16,396 |                       44.163 |
|           LAX |       15,945 |                       48.941 |
|           LGA |        6,456 |                       44.139 |
|           MIA |       13,401 |                       54.747 |

Looking at our data, it unsurprisingly, only snowed or sleeted in New York. As a result, we only looked at flights that left on days with no precipitation or when it was raining.

![](fig1_interaction_plot.jpg)

From this figure, we can see that mean departure delay time is greater when it is raining for every origin airport. But the difference in mean departure delay time between the rain vs. no precipitation conditions is greater for JFK and LGA.

## Statistical Tests
### Two-sided t-test

To examine the differences in departure delay time, we ran a two-sided, two-sample t-test to look at departure delay time (minutes) based on whether or not it was raining.

<img src="https://render.githubusercontent.com/render/math?math=H_0 :"> There is no difference in departure delay time between flights not affected by any precipitation and flights that were affected by rain. <img src="https://render.githubusercontent.com/render/math?math=(D_{\text{no rain}} = D_{\text{rain}})">

<img src="https://render.githubusercontent.com/render/math?math=H_a :"> We can reject the null hypothesis. There is a difference in departure delay time between flights not affected by any precipitation and flights that were affected by rain. <img src="https://render.githubusercontent.com/render/math?math=(D_{\text{no rain}} \neq D_{\text{rain}})">

### One-Way ANOVA (Departure Delay ~ Origin Airport)

To examine the differences in departure delay time, we ran a one-way ANOVA test with departure delay (minutes) as the dependent variable, and the origin variable as the independent variable. To further breakdown the results of the ANOVA test, we ran a Tukey HSD test.

<img src="https://render.githubusercontent.com/render/math?math=H_0 :"> There is no difference in departure delay time between flights departing from each of the airports. <img src="https://render.githubusercontent.com/render/math?math=(D_{JFK} = D_{LGA} = D_{LAX} = D_{MIA})">

<img src="https://render.githubusercontent.com/render/math?math=H_a :"> The null hypothesis is false. <img src="https://render.githubusercontent.com/render/math?math=(H_0 \text{ is false})">

### Two-Way ANOVA (Departure Delay ~ Origin Airport + Rain + Origin Airport:Rain)

To examine the differences in departure delay time, we hypothesized that origin airport and precipitation type may interact with one another. To test this hypothesis, we ran a two-way ANOVA test followed by post hoc analysis, which related back to our prior two statistical tests. In this case, the dependent variable is departure delay in minutes, and the independent variables are origin airport and whether or not it is raining.

<img src="https://render.githubusercontent.com/render/math?math=H_0 :"> There is no difference in departure delay time between flights departing from each of the airports. <img src="https://render.githubusercontent.com/render/math?math=(D_{JFK} = D_{LGA} = D_{LAX} = D_{MIA})">

<img src="https://render.githubusercontent.com/render/math?math=H_a :"> The null hypothesis is false. <img src="https://render.githubusercontent.com/render/math?math=(H_0 \text{ is false})">

<img src="https://render.githubusercontent.com/render/math?math=H_0 :"> There is no difference in departure delay time between flights not affected by any precipitation and flights that were affected by rain. <img src="https://render.githubusercontent.com/render/math?math=(D_{\text{no rain}} = D_{\text{rain}})">

<img src="https://render.githubusercontent.com/render/math?math=H_a :"> We can reject the null hypothesis. There is a difference in departure delay time between flights not affected by any precipitation and flights that were affected by rain. <img src="https://render.githubusercontent.com/render/math?math=(D_{\text{no rain}} \neq D_{\text{rain}})">

<img src="https://render.githubusercontent.com/render/math?math=H_0 :"> There is no interaction between origin airport and whether or not it is raining.

<img src="https://render.githubusercontent.com/render/math?math=H_a :"> We can reject the null hypothesis. <img src="https://render.githubusercontent.com/render/math?math=(H_0 \text{ is false})">
