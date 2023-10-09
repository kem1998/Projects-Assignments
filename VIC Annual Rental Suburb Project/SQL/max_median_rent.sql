SELECT ap.suburb, ap.month, ap.median_rent AS max_median_rent
FROM all_properties ap join
	(SELECT suburb, MAX(median_rent) AS max_median_rent
	 FROM all_properties ap
	 GROUP BY suburb
	) ap2
ON ap.suburb = ap2.suburb AND ap.median_rent =  ap2.max_median_rent
GROUP BY ap.suburb, ap.month, ap.median_rent
ORDER BY ap.suburb, ap.month, ap.median_rent

