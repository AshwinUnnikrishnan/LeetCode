# Write your MySQL query statement below




SELECT e.name AS Employee
FROM Employee e
WHERE e.id IN ( SELECT e2.id
                FROM Employee e2 
                LEFT JOIN Employee e3
                    ON e2.managerID = e3.id
                WHERE e2.salary > e3.salary);
