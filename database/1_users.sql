USE sailmaster;
CREATE USER IF NOT EXISTS 'sailmaster_user'@'localhost' IDENTIFIED BY 'password';
--MySQL 5.7.6 or less
--GRANT ALL ON `sailmaster`.* TO 'sailmaster_user'@'localhost' IDENTIFIED BY 'password';
GRANT USAGE ON *.* TO 'sailmaster_user'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_P$
GRANT ALL PRIVILEGES ON `sailmaster`.* TO 'sailmaster_user'@'localhost';
