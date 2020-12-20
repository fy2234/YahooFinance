SELECT my_select.name,
         my_select.hourly_high,
        table1.ts,
        my_select.hour
FROM 
    (SELECT name,
        MAX(high) AS hourly_high,
        SUBSTRING(ts,
        12,
        2) AS hour
    FROM "stat9760_project3"
    GROUP BY  name,SUBSTRING(ts,12,2)
    ORDER BY  name,SUBSTRING(ts,12,2)) my_select, "stat9760_project3" AS table1
WHERE my_select.name=table1.name
        AND my_select.hourly_high=table1.high
        AND my_select.hour=SUBSTRING(table1.ts,12,2)
ORDER BY  name,ts