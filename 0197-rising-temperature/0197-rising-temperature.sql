# Write your MySQL query statement below
select W2.id
from Weather W2
inner join Weather W1
on DATEDIFF(W2.recordDate, W1.recordDate) = 1
AND W2.temperature > W1.temperature; 