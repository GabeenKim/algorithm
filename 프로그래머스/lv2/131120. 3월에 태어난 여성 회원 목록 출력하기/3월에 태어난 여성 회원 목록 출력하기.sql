-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER,  DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE DATE_FORMAT(DATE_OF_BIRTH, '%m') = '03' 
    and TLNO is not NULL
    and gender = 'W'
    order by MEMBER_ID
    