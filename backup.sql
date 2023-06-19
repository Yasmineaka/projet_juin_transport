BEGIN TRANSACTION;
CREATE TABLE users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 password NOT NULL);
INSERT INTO "users" VALUES(1,'Dakota Young','12111991641','Pa$$w0rd!');
INSERT INTO "users" VALUES(2,'Courtney Kelly','+1 (252) 186-9059','s');
INSERT INTO "users" VALUES(3,'b','+1 (596) 728-7632','d');
INSERT INTO "users" VALUES(4,'b','+1 (217) 763-7782','3');
INSERT INTO "users" VALUES(5,'Megan Dawson','+1 (152) 169-2672','2');
INSERT INTO "users" VALUES(6,'Price Stevens','+1 (823) 339-1475','aa');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',6);
COMMIT;
