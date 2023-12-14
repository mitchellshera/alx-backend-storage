-- Create or replace the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE num_corrections INT;

    -- Calculate the total score and the number of corrections
    SELECT SUM(score), COUNT(*) INTO total_score, num_corrections
    FROM corrections
    WHERE user_id = p_user_id;

    -- Calculate the average score
    IF num_corrections > 0 THEN
        UPDATE users
        SET average_score = total_score / num_corrections
        WHERE id = p_user_id;
    ELSE
        -- Handle the case when there are no corrections
        UPDATE users
        SET average_score = 0
        WHERE id = p_user_id;
    END IF;
END;
//
DELIMITER ;