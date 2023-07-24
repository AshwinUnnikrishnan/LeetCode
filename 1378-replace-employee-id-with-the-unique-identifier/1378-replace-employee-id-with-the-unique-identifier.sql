# Write your MySQL query statement below
select
    EU.unique_id, E.name
from Employees E
LEFT join EmployeeUNI EU
    on EU.id = E.id
order by E.name;

