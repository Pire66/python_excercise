----L;DR: преобразуйте одним запросом дерево, представленное структурными метками ltree в дерево, представленное в виде вложенных множеств.
----У вас есть таблица KeywordLtree в которой записано небольшое дерево с помощью структурных меток.
----CREATE TABLE KeywordLtree(id INT PRIMARY KEY, value TEXT, path ltree);
----Его корневая вершина имеет идентификатор 0 и пустой путь. Соседние вершины упорядочены в порядке возрастания идентификаторов. Вы хотите ----написать один запрос, который сгенерирует вам представление этого же дерева в виде вложенных множеств.
CREATE EXTENSION IF NOT EXISTS ltree;

-- В таблице Keyword храним структурные метки ltree
CREATE TABLE KeywordLtree(
  id INT PRIMARY KEY,
  value TEXT,
  path ltree
);

-- Процедура вставляет новую вершину в дерево в таблице KeywordLtree
CREATE OR REPLACE FUNCTION InsertKeywordLtree(_id INT, _parent_id INT, _value TEXT)
RETURNS VOID AS $$
INSERT INTO KeywordLtree
SELECT _id AS id, _value AS value, K.path || text2ltree(_id::TEXT) AS path
FROM KeywordLtree K WHERE id = _parent_id;
$$ LANGUAGE sql;


-- Процедура генерирует случайное дерево из 50 вершин
CREATE OR REPLACE FUNCTION GenerateData()
RETURNS VOID AS $$
DECLARE
  _id INT;
  _parent_id INT;
  _value TEXT;
BEGIN
INSERT INTO KeywordLtree(id, value, path) VALUES (0, 'root', '');
FOR _id IN 1..49 LOOP
  _parent_id = floor((random()*_id));
  _value = md5(random()::TEXT);
  PERFORM InsertKeywordLtree(_id, _parent_id, _value);
END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT GenerateData();

WITH RECURSIVE 
	t1 AS (SELECT   *, string_to_array(ltree2text(path),'.') AS A FROM KeywordLtree),
	t2 AS (SELECT id, value, path,  a::INT[] AS pathint,  array_length(a,1) AS depth  FROM t1 ORDER BY pathint),
	t3 AS (SELECT *, CASE WHEN t2.depth>1 THEN  SUBLTREE(t2.path,0,t2.depth-1) ELSE null END AS parent FROM t2),
	t4 AS (SELECT DISTINCT  parent,   COUNT(*) OVER (PARTITION BY parent)  AS sumchild FROM t3 
		   UNION   SELECT path AS parent, (SELECT COUNT(*) FROM t2 WHERE depth=1 ) AS sumchild FROM t3 WHERE  depth IS NULL),
	t5 AS (SELECT  t3.id, t3.value, t3.path,  t3.pathint, t3.depth, t3. parent, t4.sumchild FROM t3 LEFT JOIN t4 ON t3.path = t4.parent ORDER BY t3.pathint),
	t6 AS (SELECT *, (SELECT COUNT(*) FROM t5 WHERE A1.pathint = t5.pathint[1:array_length(A1.pathint,1)]  )-1 AS allchild  FROM t5 A1 ORDER BY A1.pathint)
SELECT id, value,
		CASE WHEN depth IS NULL THEN 1 else (ROW_NUMBER() OVER (ORDER BY pathint))*2-(depth+1) END AS lgt, 
	    CASE WHEN depth IS NULL THEN (SELECT COUNT(*) FROM t6 )*2  else (ROW_NUMBER() OVER (ORDER BY pathint))*2-(depth+1) + allchild*2+1 END AS rgt FROM t6

