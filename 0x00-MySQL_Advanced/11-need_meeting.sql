-- Create or replace the view
CREATE VIEW need_meeting AS
SELECT
    s.name
FROM
    students s
LEFT JOIN
    meetings m ON s.id = m.student_id
WHERE
    s.score < 80
    AND (m.last_meeting_date IS NULL OR m.last_meeting_date < NOW() - INTERVAL 1 MONTH);