*CREATE TABLE Cities(
  id INT PRIMARY KEY,
  value TEXT
);
-- У вас есть таблица Cities, в которой записаны названия городов. 
-- Вам нужно упорядочить (под)множество этих городов так, чтобы каждый N+1 город начинался с буквы, с которой заканчивается N-й
-- Пример данных
INSERT INTO Cities(id, value) VALUES (1, 'Воркута'), (0, 'Джамбул'), (2, 'Львов');
INSERT INTO Cities(id, value) VALUES (3, 'Азов');
INSERT INTO Cities(id, value) VALUES (4, 'Женева');
INSERT INTO Cities(id, value) VALUES (5, 'Воронеж');
INSERT INTO Cities(id, value) VALUES (6, 'Саратов');
*/
WITH RECURSIVE t(id, value, num, arr) AS (
    SELECT C.id, C.value, 1::INTEGER, ARRAY[0] FROM Cities C WHERE C.id = 0
  UNION ALL
    (SELECT  c.id, c.value, t.num+1 ,  array_append(t.arr, c.id)
	FROM Cities C, t WHERE LOWER(RIGHT(t.value,1)) = LOWER(LEFT(C.value,1)) AND  array_position(t.arr,c.id) IS NULL    LIMIT 1)
)
SELECT id, value, num FROM t LIMIT (SELECT COUNT(*) FROM Cities);
