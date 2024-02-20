SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
INNER JOIN 
    Department d 
        ON e.departmentId = d.id
LEFT JOIN
    Employee e2 ON e.departmentId = e2.departmentId AND e.salary < e2.salary
GROUP BY
    e.id
HAVING 
    COUNT(DISTINCT e2.salary) < 3 OR COUNT(DISTINCT e2.salary) IS NULL;
