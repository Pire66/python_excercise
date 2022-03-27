-------------
анализ биржевых котировок.
Есть таблица StockQuotes(company TEXT, week INT, share_price INT). Строка в этой таблице говорит о том, что стоимость акции компании company в неделю номер week составляла share_price.
Назовём индексом в данную неделю среднее арифметическое роста стоимости одной акции по всем компаниям сравнительно с предыдущей неделей. То есть, если одна акция компании A подорожала на 100 единиц, а акция компании B подешевела на 50 единиц, то индекс равен 25.
Назовём компанию успешной на этой неделе, если изменение стоимости одной её акции было выше индекса. "Изменение D выше индекса I" означает "D > I" как вещественное число.
Если компания была успешной три недели подряд то будем говорить, что она сделала успешную серию. Успешные серии могут пересекаться. Так, если компания была успешной 5 недель подряд, то у неё было 3 успешных серии.
Вам нужно посчитать для каждой компании количество успешных серий и вывести в результат два столбца. В первом столбце с типом TEXT должно быть название компании, а во втором с типом BIGINT количество её успешных серий. Тип BIGINT, скорее всего, получится автоматически, но вы можете явно привести результат оператором ::BIGINT. При несоответствии типов ожидаемым  вам предложат проверить, нет ли в запросе синтаксических ошибок и возвращает ли он ровно то, что требуется. Это же сообщение может появиться и по другим поводам, например если у вас действительно есть синтаксические ошибки.
Компании, у которых не было успешных серий, выводить в результат не надо совсем.
    Все компании различные.
    Все цены положительные.
    Нумерация недель начинается с 0. На неделе номер 0, разумеется, не определены рост и индекс -- вы можете считать что они 0, NULL или просто игнорировать нулевую неделю тем или иным способом при расчёте успешных недель.
-------------
/*DROP TABLE IF EXISTS StockQuotes;
 
CREATE TABLE StockQuotes(
  company TEXT,
  week INT,
  share_price INT
  );
 
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  1,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  2,  15);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  3,  20);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  4,  25);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  5,  30);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  6,  35);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  7,  40);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  8,  45);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple',  9,  50);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 10,  60);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 11,  70);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 12,  80);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 13,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 14,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 15, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 16, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 17, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 18, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 19, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Apple', 20,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  1,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  2,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  3,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  4,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  5,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  6,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  7,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  8,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  9,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  10,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  11,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  12,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  13,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  14,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  15,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  16,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  17,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  18,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  19,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Oracle',  20,  10);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  1, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  2,  95);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  3,  95);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  4,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  5,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  6,  85);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  7,  80);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  8,  100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  9,  120);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  10, 150);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  11, 100);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  12,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  13,  90);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  14,  85);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  15,  80);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  16,  75);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  17,  70);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  18,  70);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  19,  65);
INSERT INTO StockQuotes (company, week, share_price) VALUES ('Microsoft',  20,  60);*/
WITH step1 AS (
	SELECT company, week, 
		share_price::NUMERIC - LAG(share_price,1,share_price) OVER (PARTITION BY company ORDER BY company,week )::NUMERIC AS grow
		FROM StockQuotes ORDER BY 1,2
	),
	step2 AS (
	SELECT company, week, grow, avg(grow) OVER (PARTITION BY week ) AS avg_grow  
		FROM step1  ORDER BY 1,2
		 ),
	step3 AS (
	SELECT company, week, COUNT(grow-avg_grow)   FILTER (WHERE (grow-avg_grow) > 0) 
		   OVER (PARTITION BY company ORDER BY company ROWS BETWEEN 2 PRECEDING AND CURRENT ROW ) AS index_plus FROM step2
	)
	SELECT company, COUNT(*) FROM step3 WHERE index_plus>=3 GROUP BY company 
