SELECT ap.suburb, ap.month, ap.no_properties AS max_no_properties
FROM all_properties ap join
	(SELECT suburb, MAX(no_properties) AS max_no_properties
	 FROM all_properties ap
	 GROUP BY suburb
	) ap2
ON ap.suburb = ap2.suburb AND ap.no_properties =  ap2.max_no_properties
GROUP BY ap.suburb, ap.month, ap.no_properties
ORDER BY ap.suburb, ap.month, ap.no_properties