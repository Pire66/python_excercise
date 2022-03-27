
CREATE TABLE ConferenceEvent(id SERIAL PRIMARY KEY,	conference_id INT, -- REFERENCES Conference,year INT,UNIQUE(conference_id, year));
CREATE TABLE Paper( id INT PRIMARY KEY, event_id INT, -- REFERENCES ConferenceEvent,  title TEXT,  accepted BOOLEAN);
CREATE TABLE Reviewer( id INT PRIMARY KEY, email TEXT UNIQUE, name TEXT);
CREATE TABLE PaperReviewing( paper_id INT, -- REFERENCES Paper, reviewer_id INT, -- REFERENCES Reviewer, score INT,  UNIQUE(paper_id, reviewer_id));
INSERT INTO Conference(id, name) VALUES (1, 'SIGMOD'), (2, 'VLDB');
INSERT INTO ConferenceEvent(conference_id, year) VALUES (1, 2015), (1, 2016), (2, 2016);
INSERT INTO Reviewer(id, email, name) VALUES  (1, 'jennifer@stanford.edu', 'Jennifer Widom'),
  (2, 'donald@ethz.ch', 'Donald Kossmann'),  (3, 'jeffrey@stanford.edu', 'Jeffrey Ullman'),
  (4, 'jeff@google.com', 'Jeffrey Dean'),  (5, 'michael@mit.edu', 'Michael Stonebraker');
INSERT INTO Paper(id, event_id, title) VALUES  (1, 1, 'Paper1'),  (2, 2, 'Paper2'),  (3, 2, 'Paper3'),  (4, 3, 'Paper4');
INSERT INTO PaperReviewing(paper_id, reviewer_id) VALUES  (1, 1), (1, 4), (1, 5),  (2, 1), (2, 2), (2, 4),
  (3, 3), (3, 4), (3, 5),  (4, 2), (4, 3), (4, 4);
  CREATE OR REPLACE FUNCTION t() RETURNS text AS $$
  DECLARE 
  	_paper_id INTEGER := 2;
  	_reviewer_id INTEGER :=  3;
  	_score INTEGER := 2;
	kol_Reviewing INTEGER := 0;
	kol_marks INTEGER := 0;
	avarage_marks NUMERIC := 0;
	marks BOOLEAN := FALSE;
	acception BOOLEAN := FALSE;
BEGIN
  	IF (_score>0 AND _score<=7) THEN
        acception = (SELECT accepted  FROM Paper WHERE id = _paper_id);
        IF ((acception  IS NULL) OR NOT acception) THEN
            IF (SELECT COUNT(*) FROM PaperReviewing  GROUP BY paper_id,reviewer_id 
				HAVING (paper_id = _paper_id) AND (reviewer_id = _reviewer_id) ) > 0 THEN
  		        UPDATE  PaperReviewing SET score = _score WHERE (PaperReviewing.paper_id = _paper_id) AND (PaperReviewing.reviewer_id = _reviewer_id);
    	        kol_Reviewing = (SELECT COUNT(*) FROM PaperReviewing WHERE PaperReviewing.paper_id = _paper_id);
            	kol_marks = (SELECT COUNT(score) FROM PaperReviewing WHERE PaperReviewing.paper_id = _paper_id);
                IF kol_Reviewing = kol_marks THEN
		            avarage_marks = (SELECT SUM(score) FROM PaperReviewing WHERE PaperReviewing.paper_id = _paper_id) / kol_Reviewing;
		            IF avarage_marks > 4 THEN
			            marks = True;
                    ELSE
			            marks = False;
		            END IF;
		            UPDATE  Paper SET accepted = marks WHERE id = _paper_id ;          
                END IF;
            ELSE 
                RAISE SQLSTATE 'DB017';
            END IF;
        ELSE
		    RAISE SQLSTATE 'DB017';
	    END IF;
    ELSE
        RAISE SQLSTATE 'DB017';
	END IF;
END;
  $$ LANGUAGE plpgsql;


