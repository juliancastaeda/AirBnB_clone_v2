--
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
USE performance_schema;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
