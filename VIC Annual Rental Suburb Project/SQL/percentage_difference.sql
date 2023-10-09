ALTER TABLE all_properties ALTER COLUMN month date not null

SELECT *
FROM all_properties

DROP TABLE #TempCorrelation
SELECT suburb, month, sum(no_properties) As number_of_properties, avg(median_rent) AS Median_rent, sum(no_properties) - avg(median_rent) AS difference
INTO #TempCorrelation
FROM all_properties
GROUP BY suburb, month
ORDER BY suburb asc

SELECT * 
FROM #TempCorrelation
ORDER BY suburb, month

DROP TABLE #Tempdiffpercentage
SELECT t.suburb, t.month,

(t.number_of_properties - tprev.number_of_properties) / tprev.number_of_properties AS no_Properties_diff,
(t.Median_rent - tprev.Median_rent) / tprev.Median_rent AS median_rent_diff

INTO #Tempdiffpercentage

from #TempCorrelation t INNER JOIN
     #TempCorrelation tprev
     on t.month = DATEADD(MONTH, 3, tprev.month) AND t.suburb = tprev.suburb
ORDER BY t.suburb, t.month

SELECT * 
FROM #Tempdiffpercentage
ORDER BY suburb, month