CREATE DATABASE IF NOT EXISTS risk_db;

USE risk_db;

CREATE TABLE `risks` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `impact` VARCHAR(255),
    `title` VARCHAR(255),
    `description` TEXT,
    FULLTEXT(impact, title, description)
);


CREATE TABLE `user` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` blob NOT NULL,
  `fullname` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';


DELIMITER $$
--
-- Procedimientos
--
CREATE PROCEDURE `sp_addUser` (IN `pUsername` VARCHAR(20), IN `pPassword` VARCHAR(20), IN `pFullname` VARCHAR(50))  BEGIN
    INSERT INTO user (username, password, fullname)
    VALUES (pUsername, AES_ENCRYPT(pPassword, SHA2('B!1w8*NAt1T^%kvhUI*S^_', 512)), pFullname);
END$$

CREATE PROCEDURE `sp_verifyIdentity` (IN `pUsername` VARCHAR(20), IN `pPassword` VARCHAR(20))  BEGIN
	SELECT USER.id, USER.username, USER.fullname 
	FROM user USER 
    WHERE 1 = 1 
    AND USER.username = pUsername 
	AND CAST(AES_DECRYPT(USER.password, SHA2('B!1w8*NAt1T^%kvhUI*S^_', 512)) AS CHAR(30)) = pPassword;
END$$

DELIMITER ;



INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'user', 0x98fb67ca8f459f49841208bd4261bceb, 'user user');




INSERT INTO risks (impact, title, description) 
VALUES 
('High', 'Risk 1', 'Description of risk 1'),
('Medium', 'Risk 2', 'Description of risk 2'),
('Low', 'Risk 3', 'Description of risk 3'),
('High', 'Risk 4', 'Description of risk 4'),
('Medium', 'Risk 5', 'Description of risk 5'),
('Low', 'Risk 6', 'Description of risk 6'),
('High', 'Risk 7', 'Description of risk 7'),
('Medium', 'Risk 8', 'Description of risk 8'),
('Low', 'Risk 9', 'Description of risk 9'),
('High', 'Risk 10', 'Description of risk 10'),
('Medium', 'Risk 11', 'Description of risk 11'),
('Low', 'Risk 12', 'Description of risk 12'),
('High', 'Risk 13', 'Description of risk 13'),
('Medium', 'Risk 14', 'Description of risk 14'),
('Low', 'Risk 15', 'Description of risk 15'),
('High', 'Risk 16', 'Description of risk 16'),
('Medium', 'Risk 17', 'Description of risk 17'),
('Low', 'Risk 18', 'Description of risk 18'),
('High', 'Risk 19', 'Description of risk 19'),
('Medium', 'Risk 20', 'Description of risk 20');
