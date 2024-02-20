# Write your MySQL query statement below

SELECT u.name as NAME, SUM(t.amount) as BALANCE
FROM Users u
LEFT JOIN Transactions t
ON u.account = t.account
GROUP BY u.name
HAVING SUM(t.amount) > 10000;

