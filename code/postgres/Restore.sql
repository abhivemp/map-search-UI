/* ---- Restore ---- */

-- Code by Yash Dhayal

-- For restoring the DB off of a dump:
-- 1. First create the new DB:
-- createdb ProjectBak

-- 2. Run the dumpfile:
psql ProjectBak < ProjectDB_dump.sql


-- For restoring a table off of a dump:
-- Restoring CONTENT table:
psql -d ProjectBak < Content_dump.sql

-- Restoring Article table:
psql -d ProjectBak < Article_dump.sql

-- Restoring Multimedia table:
psql -d ProjectBak < Multimedia_dump.sql
