SELECT EE.name
FROM EMPLOYEE EE
WHERE EE.id IN (
    SELECT E.managerid
    FROM EMPLOYEE E
    GROUP BY E.managerid
    HAVING COUNT(E.managerid) >= 5
);
