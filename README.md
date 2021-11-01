# Surfs_up
## Overview of the statistical analysis
I want to open a surf shop in Hawaii and looking for the investment from W.Avy. He has a concern about the impact of the weather on surf shop's business.
- Purpose: Analyze the weather data W.Avy provided on temperature trend to determine whether the surf and ice cream shop business is sustainable year-round. 

## Results
- Key differences in weather between *June* and *December*

  ![June temperature](https://github.com/xueying-lin/surfs_up/blob/9c6682e6ab5de079c1d159346811b195dadcd549/Resources/June.PNG)
  
  ![December temperature](https://github.com/xueying-lin/surfs_up/blob/9c6682e6ab5de079c1d159346811b195dadcd549/Resources/December.PNG)
  
   - As the above picture shown, the **minimum temperature** of December (56) is much lower than the ones of June (64)
   - the **25th percentile** of December(69) is much lower than the ones of June (73)
   - the **variance** of December (3.75) is larger than the ones of June (3.26)

## Summary
From the analysis, it seems that the overall weather of Hawaii in December is lower and more variable than weather of Hawaii in June, though the mean and maximum weather is really close.
1. Since the weather will change annually, it is better to check the weather between June and December within the past one year as follow query:
```
session.query(Measurement.date, Measurement.tobs).filter(extract("month", Measurement.date) == "06", extract("year", Measurement.date) >= "2016").all()

session.query(Measurement.date, Measurement.tobs).filter(extract("month", Measurement.date) == "12", extract("year", Measurement.date) >= "2016").all()

```

2. Whether the low temperature is associated with high frequency of raining this year? The query will as follow:
```
session.query(Measurement.date, Measurement.prcp).filter(extract("month", Measurement.date) == "06", extract("year", Measurement.date) >= "2016").all()

session.query(Measurement.date, Measurement.prcp).filter(extract("month", Measurement.date) == "12", extract("year", Measurement.date) >= "2016").all()

```
