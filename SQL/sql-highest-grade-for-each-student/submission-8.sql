SELECT student_id, MIN(exam_id) as exam_id, score
FROM exam_results er
WHERE score = (
    SELECT MAX(score)
    FROM exam_results
    WHERE student_id = er.student_id
)
GROUP BY student_id, score
ORDER BY student_id ASC;