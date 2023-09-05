-- Task D.1 - List the total number of vaccines administered in each observation date for Afghanistan
SELECT date,
       daily_vaccinations
  FROM CountryVaccinations
 WHERE iso_code = (
                      SELECT iso_code
                        FROM Locations
                       WHERE location = "Afghanistan"
                  );
-- END: Task D.1

-- Task D.2 - Produce a dataset containing total number of COVID-19 doses administered by each country
SELECT (
	   SELECT location
		 FROM Locations
		WHERE iso_code = CountryVaccinations.iso_code
   )
   AS Country,
   MAX(NULLIF(total_vaccinations, "") ) AS [Total Vaccinations Administered]
FROM CountryVaccinations
WHERE total_vaccinations NOT NULL
GROUP BY Country
ORDER BY Country ASC;

-- END: Task D.2

-- Task D.3 - Produce a list of all countries with the type of vaccines administered
 SELECT (
           SELECT location
             FROM Locations
            WHERE iso_code = LocationVaccines.iso_code
       )
       AS Country,
       (
           SELECT name
             FROM Vaccines
            WHERE vaccine_id = LocationVaccines.vaccine_id
       )
       AS Vaccine
  FROM LocationVaccines
 ORDER BY Country ASC;
 
-- END: Task D.3

-- Task D.4 (WITH JOIN)- Produce report shoing the total number of vaccines administered according to each data source
-- NOTE: Combined Duplicates only when the data source website matched

 SELECT SourceName AS [Source Name],
       SUM(TOTAL) AS [Total Vaccines Administered]
  FROM (
           SELECT CountryVaccinations.iso_code,
                  MAX(NULLIF(CountryVaccinations.total_vaccinations, "") ) AS Total,
                  IFNULL(DataSource.source_name, "Unknown Source - Data Unavaliable") AS SourceName,
                  DataSource.source_website AS SourceWebsite
             FROM CountryVaccinations
                  LEFT JOIN
                  DataSource ON CountryVaccinations.iso_code = DataSource.iso_code
            GROUP BY CountryVaccinations.iso_code
       )
 GROUP BY SourceWebsite
 ORDER BY SourceName ASC;

-- END: Task D.4 (WITH JOIN)

-- Task D.5 - Produce a report that lists all the observation dates, and provides total number of
--             fully vaccinated in 4 countries (Australia, United States, France and Israel)

SELECT CountryDailyTotals.date,
       MAX(CASE WHEN CountryDailyTotals.iso_code = (
                                                       SELECT iso_code
                                                         FROM Locations
                                                        WHERE location = 'Australia'
                                                   )
           THEN CountryDailyTotals.people_fully_vaccinated END) AS Australia,
       MAX(CASE WHEN CountryDailyTotals.iso_code = (
                                                       SELECT iso_code
                                                         FROM Locations
                                                        WHERE location = 'United States'
                                                   )
           THEN CountryDailyTotals.people_fully_vaccinated END) AS [United States],
       MAX(CASE WHEN CountryDailyTotals.iso_code = (
                                                       SELECT iso_code
                                                         FROM Locations
                                                        WHERE location = 'France'
                                                   )
           THEN CountryDailyTotals.people_fully_vaccinated END) AS France,
       MAX(CASE WHEN CountryDailyTotals.iso_code = (
                                                       SELECT iso_code
                                                         FROM Locations
                                                        WHERE location = 'Israel'
                                                   )
           THEN CountryDailyTotals.people_fully_vaccinated END) AS Israel
  FROM CountryDailyTotals
 GROUP BY CountryDailyTotals.date
 ORDER BY CountryDailyTotals.date DESC;
 
-- END: Task D.5