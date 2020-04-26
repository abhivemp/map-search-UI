/* ---- BACKUP ---- */

-- Code by Yash Dhayal

-- Creating dump file to restore DB up to dump file creation time
pg_dump Project > ProjectDB_dump.sql


-- Creating dump file for a table to restore:
-- dump file for CONTENT table
pg_dump -d Project -t Content > Content_dump.sql

-- dump file for Article table
pg_dump -d Project -t Article > Article_dump.sql

-- dump file for Multimedia table
pg_dump -d Project -t Multimedia > Multimedia_dump.sql

