# Kayla_Haeussler_MiniProject_6

[![CI](https://github.com/nogibjj/Kayla_Haeussler_Mini_Project_5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Kayla_Haeussler_Mini_Project_5/actions/workflows/cicd.yml)

IDS 706: Mini Project 6
Complex SQL Query for a MySQL Database (Databricks)
Kayla Haeussler  

```
Kayla_Haeussler_Mini_Project_5/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── data/
│   └── candy_data.csv
├── mylib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── .gitignore
├── Candy_DB.db
├── Dockerfile
├── LICENSE
├── main.py
├── Makefile
├── README.md
├── requirements.txt
├── setup.sh
└── test_main.py
```
## Assignment Requirements
* Design a comlpex SQL query involving joins, aggregation and sorting
* Provide an explanation for what the query is doing and the expected results

## Data Set
The data set used in this project comes from the ```fivethirtyeight``` repository, called candy-data.csv, that contains candy power ranking data. 
https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking

## Complex Query
```
WITH avg_winpercent AS ( 
SELECT  
chocolate, 
AVG(winpercent) AS choc_nonchoc_win_perc 
FROM  default.keh119_candy 
GROUP BY  chocolate 
) 

SELECT  
keh.competitorname, 
keh.winpercent, 
avg_winpercent.choc_nonchoc_win_perc 
FROM default.keh119_candy as keh 
JOIN avg_winpercent 
ON keh.chocolate = avg_winpercent.chocolate 
ORDER BY keh.winpercent DESC; 
```

The assignment required us to utilize joins, aggregation and sorting in our query. I wanted to continue using the candy-data.csv I had been using in my previous mini projects, but did not have access to another candy data set that I could logically merge with this one. To solve this issue and successfully fulfill this project's requirements, I created a new data set from candy-data, and called it **avg_winpercent**. This new data set takes two columns from candy-data, **chocolate** and the average of **winpercent**. However by using **GROUP BY**, we tell our query to calculate the average **winpercent** for each level of **chocolate**, the levels being 1 or 0, corresponding to the candy having or not having chocolate. After this part of the query is run we have a 2 row 2 column data set that would look something like this:
| chocolate           | choc_nonchoc_win_perc  |
|------------------|---------------------|
| 1    | 60.753468407524956          |
| 0     | 42.14225701491038        | 

The query then joins the columns **competitor name and win percent** from the original candy-data dataset with **choc_nonchoc_win_perc** on the shared column of chocolate, which then joins the corresponding average win percentage of whether or not the candy contains chocolate. We then sort the merged dataset on the original winpercents of each candy from the candy-data data set, in descending order, the first 5 rows of the final result of the query would look like this: 

| competitorname    |winpercent     | choc_nonchoc_win_perc      |
|------------------|---------------------|---------------------|
|Reese's Peanut Butter cup|	84.18029022216797|	60.753468407524956
|Reese's Miniatures	|81.86625671386719|	60.753468407524956
|Twix	|81.64291381835938|	60.753468407524956
|Kit Kat	|76.76860046386719	|60.753468407524956
|Snickers|	76.67378234863281	|60.753468407524956