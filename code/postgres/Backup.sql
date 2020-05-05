/* ---- BACKUP ---- */

-- Code by Yash Dhayal

-- Change database names and file names as necessary.
-- Below, the database is named Project.

-- Creating dump file to restore DB up to dump file creation time
-- Change dump file name as desired
pg_dump Project > ProjectDB_dump.sql


-- Creating dump file for a table to restore:
-- dump file for CONTENT table
pg_dump -d Project -t Content > Content_dump.sql

-- dump file for Article table
pg_dump -d Project -t Article > Article_dump.sql

-- dump file for Multimedia table
pg_dump -d Project -t Multimedia > Multimedia_dump.sql

