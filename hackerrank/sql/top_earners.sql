-- Problem description: https://www.hackerrank.com/challenges/earnings-of-employees/problem
SELECT total_salary, COUNT(*) AS cnt
FROM (
    SELECT (salary * months) AS total_salary
    FROM employee
) AS sub
GROUP BY total_salary ORDER BY total_salary
DESC LIMIT 1;
