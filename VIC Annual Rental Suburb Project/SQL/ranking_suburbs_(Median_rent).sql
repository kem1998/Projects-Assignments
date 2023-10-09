SELECT suburb, month, median_rent,  ROW_NUMBER() OVER (ORDER BY median_rent DESC) AS Ranking
FROM all_properties
WHERE median_rent is not NULL
ORDER BY median_rent DESC