----Напишите запрос, считающий в дереве, хранимом в виде списков смежностей, для каждой вершины размер её поддерева.
----У вас есть таблица, в которой записано случайное дерево из 50 вершин в виде списков смежностей. 
CREATE TABLE Keyword(
  id INT PRIMARY KEY,
  value TEXT,
  parent_id INT REFERENCES Keyword DEFAULT NULL
);

CREATE OR REPLACE FUNCTION InsertKeyword(vertex_id INT, _parent_id INT, _value TEXT)
RETURNS INT AS $$
DECLARE _result INT;
BEGIN
INSERT INTO Keyword(id, value, parent_id) VALUES (vertex_id, _value, _parent_id) RETURNING id INTO _result;
RETURN _result;
END;
$$ LANGUAGE plpgsql;

-- Процедура генерирует случайное дерево из 50 вершин
CREATE OR REPLACE FUNCTION GenerateData()
RETURNS VOID AS $$
DECLARE
  _id INT;
  _parent_id INT;
  _value TEXT;
BEGIN
PERFORM InsertKeyword(0, NULL, 'root');
FOR _id IN 1..49 LOOP
  _parent_id = floor((random()*_id));
  _value = md5(random()::TEXT);
  PERFORM InsertKeyword(_id, _parent_id, _value);
END LOOP;
END;
$$ LANGUAGE plpgsql;
SELECT GenerateData();
WITH RECURSIVE t(id, value, parent_id, arr) AS (
    SELECT K.id, K.value, K.parent_id, ARRAY[0] FROM Keyword K WHERE K.id = 0
  UNION ALL
    (SELECT  K.id, K.value, K.parent_id,array_append(t.arr, K.id)	FROM Keyword K, t WHERE  K.parent_id = t.id ) ),
t1 AS (SELECT id, value, parent_id, arr FROM t LIMIT (SELECT COUNT(*) FROM Keyword)),
t2 AS (SELECT id, value, UNNEST(arr) AS unnest_arr FROM t1)
SELECT unnest_arr, COUNT(*) FROM t2 GROUP BY unnest_arr ORDER BY 1
