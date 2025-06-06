-- 코드를 입력하세요
SELECT P.MEMBER_NAME,R.REVIEW_TEXT,TO_CHAR(R.REVIEW_DATE,'YYYY-MM-DD') AS REVIEW_DATE
FROM MEMBER_PROFILE P 
    JOIN REST_REVIEW R ON P.MEMBER_ID = R.MEMBER_ID
WHERE R.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM (
        SELECT MEMBER_ID,
            ROW_NUMBER() OVER(ORDER BY SUM(REVIEW_SCORE) DESC) AS RANK
        FROM REST_REVIEW 
        GROUP BY MEMBER_ID
    ) 
    WHERE RANK =1 
)
ORDER BY REVIEW_DATE, R.REVIEW_TEXT