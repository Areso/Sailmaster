USE sailmaster;
CREATE TABLE `ships` (
  `id_type_ship` smallint(6) NOT NULL,
  `id_race` smallint(6) NOT NULL,
  `max_hp` smallint(6) NOT NULL,
  `max_crew` smallint(6) NOT NULL,
  PRIMARY KEY (`id_type_ship`),
  FOREIGN KEY `id_race` (`id_race`) REFERENCES `races`(`id_race`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf16;
