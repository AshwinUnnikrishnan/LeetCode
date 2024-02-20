SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
INNER JOIN 
    Department d 
        ON e.departmentId = d.id
WHERE 
   NOT EXISTS (
        SELECT 1
        FROM Employee e2
        WHERE e2.departmentId = e.departmentId
        AND e2.salary > e.salary
        GROUP BY e2.departmentId
        HAVING COUNT(DISTINCT e2.salary) >= 3
    );