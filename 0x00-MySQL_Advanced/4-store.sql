-- Create or replace the trigger
CREATE TRIGGER decrease_q
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;