CREATE DATABASE IF NOT EXISTS risk_db;

USE risk_db;


---Crear tablas 

CREATE TABLE `risks` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `cod` VARCHAR(255) UNIQUE,
    `impact` VARCHAR(255),
    `title` VARCHAR(255),
    `description` TEXT,
    `resolved` TINYINT(1),
    FULLTEXT(cod, impact, title, description)
);


CREATE TABLE `user` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL UNIQUE,
  `password` blob NOT NULL,
  `fullname` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';


DELIMITER $$

-- Procedimientos

-- Agrega un nuevo usuario con su nombre de usuario, contraseña cifrada y nombre completo.
CREATE PROCEDURE `sp_addUser` (IN `pUsername` VARCHAR(20), IN `pPassword` VARCHAR(20), IN `pFullname` VARCHAR(50))  BEGIN
    INSERT INTO user (username, password, fullname)
    VALUES (pUsername, AES_ENCRYPT(pPassword, SHA2('B!1w8*NAt1T^%kvhUI*S^_', 512)), pFullname);
END$$

-- Verifica la identidad de un usuario comparando su nombre de usuario y contraseña cifrada.
CREATE PROCEDURE `sp_verifyIdentity` (IN `pUsername` VARCHAR(20), IN `pPassword` VARCHAR(20))  BEGIN
	SELECT USER.id, USER.username, USER.fullname 
	FROM user USER 
    WHERE 1 = 1 
    AND USER.username = pUsername 
	AND CAST(AES_DECRYPT(USER.password, SHA2('B!1w8*NAt1T^%kvhUI*S^_', 512)) AS CHAR(30)) = pPassword;
END$$


-- Obtiene todos los registros de la tabla de riesgos.
CREATE PROCEDURE `sp_getRisk` ()  
BEGIN
    SELECT * FROM risks;
END$$


-- Agrega un nuevo riesgo con su código, impacto, título, descripción y estado de resolución.
CREATE PROCEDURE `sp_addRisks` (
    IN `p_cod` VARCHAR(20),
    IN `p_impact` VARCHAR(20),
    IN `p_title` VARCHAR(50),
    IN `p_description` TEXT,
    IN `p_resolved` TINYINT(1)
)
BEGIN
    INSERT INTO risks (cod, impact, title, description, resolved)
    VALUES (p_cod, p_impact, p_title, p_description, p_resolved);

 
    SELECT LAST_INSERT_ID() AS new_id;
END $$

-- Busca riesgos en la base de datos filtrando por palabras clave y estado de resolución.
CREATE PROCEDURE `sp_searchRisks` (IN `pText` TEXT)
BEGIN
    DECLARE resolved_filter INT DEFAULT -1; 

    -- Verifica si el texto contiene "resuelto" o "no resuelto" y asigna el filtro
    IF LOWER(pText) LIKE '%no resuelto%' THEN
        SET resolved_filter = 0;
        SET pText = REPLACE(LOWER(pText), 'no resuelto', '');
    ELSEIF LOWER(pText) LIKE '%resuelto%' THEN
        SET resolved_filter = 1;
        SET pText = REPLACE(LOWER(pText), 'resuelto', '');
    END IF;

    -- Elimina espacios extra después de quitar "resuelto" o "no resuelto"
    SET pText = TRIM(pText);

    -- Consulta con el filtro de resolved si es aplicable
    SELECT id, cod, impact, title, description, resolved
    FROM risks
    WHERE (
        LOWER(impact) LIKE CONCAT('%', LOWER(pText), '%')
        OR LOWER(title) LIKE CONCAT('%', LOWER(pText), '%')
        OR LOWER(description) LIKE CONCAT('%', LOWER(pText), '%')
        OR LOWER(cod) LIKE CONCAT('%', LOWER(pText), '%')
    )
    AND (resolved_filter = -1 OR resolved = resolved_filter); 

END$$

-- Actualiza la información de un riesgo existente si el ID proporcionado es válido.
CREATE PROCEDURE `sp_updateRisks`(
    IN p_id INT,
    IN p_cod VARCHAR(255),
    IN p_impact VARCHAR(255),
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_resolved TINYINT(1)
)
BEGIN
    IF EXISTS (SELECT 1 FROM risks WHERE id = p_id) THEN
        UPDATE risks
        SET cod = p_cod,
            impact = p_impact,
            title = p_title,
            description = p_description,
            resolved = p_resolved
        WHERE id = p_id;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Risk ID not found';
    END IF;
END $$



DELIMITER ;


-- Inserta un usuario.
INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'user', 0x98fb67ca8f459f49841208bd4261bceb, 'user user');



-- Inserta múltiples registros en la tabla de riesgos.
INSERT INTO risks (cod, impact, title, description, resolved) 
VALUES 
('RISK001', 'High', 'Risk 1', 'Description of risk 1', 1),
('RISK002', 'Medium', 'Risk 2', 'Description of risk 2', 1),
('RISK003', 'Low', 'Risk 3', 'Description of risk 3', 0 ),
('RISK004', 'High', 'Risk 4', 'Description of risk 4', 0),
('RISK005', 'Medium', 'Risk 5', 'Description of risk 5', 0),
('RISK006', 'Low', 'Risk 6', 'Description of risk 6', 0 ),
('RISK007', 'High', 'Risk 7', 'Description of risk 7', 0),
('RISK008', 'Medium', 'Risk 8', 'Description of risk 8', 0),
('RISK009', 'Low', 'Risk 9', 'Description of risk 9', 0),
('RISK010', 'High', 'Risk 10', 'Description of risk 10', 1),
('RISK011', 'Medium', 'Risk 11', 'Description of risk 11', 0),
('RISK012', 'Low', 'Risk 12', 'Description of risk 12', 1),
('RISK013', 'High', 'Risk 13', 'Description of risk 13', 0),
('RISK014', 'Medium', 'Risk 14', 'Description of risk 14', 1),
('RISK015', 'Low', 'Risk 15', 'Description of risk 15', 1),
('RISK016', 'High', 'Risk 16', 'Description of risk 16', 0),
('RISK017', 'Medium', 'Risk 17', 'Description of risk 17', 0),
('RISK018', 'Low', 'Risk 18', 'Description of risk 18', 0),
('RISK019', 'High', 'Risk 19', 'Description of risk 19', 0),
('RISK020', 'Medium', 'Risk 20', 'Description of risk 20', 0);

