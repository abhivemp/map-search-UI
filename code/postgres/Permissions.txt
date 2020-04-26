
-- Permissions
-- Code by Yash Dhayal

/* ---- PERMISSIONS ---- */

-- clearing permissions to the 3 tables from anyone
REVOKE UPDATE, TRUNCATE, INSERT, CREATE, TRIGGER
ON CONTENT, ARTICLE, MM 
FROM PUBLIC;

/* only allowing UPDATE to OSC (admin). Not allowing Content_id to be 
changed by anyone, since it is a primary key */
GRANT UPDATE (Author, Title, Posting_date, Location, Category, Data)
ON CONTENT, ARTICLE, MM 
TO OSC;

-- giving back the remaining permissions only to OSC
GRANT TRUNCATE, INSERT, CREATE, TRIGGER
ON CONTENT, ARTICLE, MM 
TO OSC;

