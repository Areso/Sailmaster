CREATE TABLE `portraits` (
  `id_portrait` smallint(6) NOT NULL,
  `id_race` smallint(6) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `allowed_to_use` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_portrait`),
  FOREIGN KEY (`id_race`) REFERENCES `races`(`id_race`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf16;
