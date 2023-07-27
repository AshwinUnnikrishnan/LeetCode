


# Write your MySQL query statement below
SELECT s.student_id, s.student_name, su.subject_name, count(e.subject_name) as attended_exams
FROM students s
CROSS JOIN subjects su
LEFT JOIN examinations e
USING (student_id, subject_name)
group by student_id, student_name, su.subject_name
order by student_id, subject_name;