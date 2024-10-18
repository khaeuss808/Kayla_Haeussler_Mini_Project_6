# Kayla_Haeussler_MiniProject_5

[![CI](https://github.com/nogibjj/Kayla_Haeussler_Mini_Project_5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Kayla_Haeussler_Mini_Project_5/actions/workflows/cicd.yml)

IDS 706: Mini Project 5
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




