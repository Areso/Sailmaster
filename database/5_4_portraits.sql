USE sailmaster;
CREATE TABLE `portraits` (
  `id_portrait` smallint(6) NOT NULL,
  `id_race` smallint(6) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `allowed_to_use` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_portrait`),
  FOREIGN KEY (`id_race`) REFERENCES `races`(`id_race`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO `portraits` (`id_portrait`, `id_race`, `gender`, `allowed_to_use`) VALUES
(1001, 1, 1, 1),
(1002, 1, 0, 1),
(1003, 1, 1, 0),
(2001, 2, 1, 1),
(2002, 2, 0, 1);

