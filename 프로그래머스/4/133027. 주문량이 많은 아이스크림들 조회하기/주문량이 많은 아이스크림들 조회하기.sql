-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF
LEFT JOIN (
    SELECT SUM(TOTAL_ORDER) JO, FLAVOR
    FROM JULY
    GROUP BY FLAVOR
) b
USING (FLAVOR)
ORDER BY TOTAL_ORDER+JO DESC
LIMIT 3