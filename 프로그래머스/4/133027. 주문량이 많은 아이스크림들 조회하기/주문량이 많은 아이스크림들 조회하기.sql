SELECT FLAVOR 
FROM(
    SELECT F.FLAVOR, 
    ROW_NUMBER() OVER (ORDER BY SUM(F.TOTAL_ORDER+J.TOTAL_ORDER) DESC) AS RANK
    FROM FIRST_HALF F 
    JOIN JULY J ON F.FLAVOR=J.FLAVOR
    GROUP BY F.FLAVOR
)
WHERE RANK <=3;