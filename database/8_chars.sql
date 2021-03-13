USE sailmaster;
CREATE TABLE `chars` (
  `id_char` int(11) NOT NULL,
  `charname` varchar(24) NOT NULL,
  `id_acc` int(11) NOT NULL,
  `id_race` smallint(6) NOT NULL,
  `id_portrait` smallint(6) NOT NULL,
  `id_type_ship` smallint(6) DEFAULT NULL,
  `cur_hp` smallint(6) DEFAULT NULL,
  `cur_crew` smallint(6) DEFAULT NULL,
  `max_hp` smallint(6) DEFAULT NULL,
  `max_crew` smallint(6) DEFAULT NULL,
  `tutorial` tinyint(4) NOT NULL DEFAULT '0',
  `in_city` tinyint(1) NOT NULL DEFAULT '1',
  `money` int(11) NOT NULL DEFAULT '0',
  `id_guild` smallint(6) DEFAULT NULL,
  `loc_x` smallint(6) NOT NULL,
  `loc_y` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

ALTER TABLE `chars`
  ADD PRIMARY KEY (`id_char`),
  ADD UNIQUE KEY `charname` (`charname`),
  ADD CONSTRAINT `char_acc_id` FOREIGN KEY (`id_acc`) REFERENCES `accounts` (`id_acc`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `char_race_id` FOREIGN KEY (`id_race`) REFERENCES `races` (`id_race`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `char_portrait_id` FOREIGN KEY (`id_portrait`) REFERENCES `portraits` (`id_portrait`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `char_type_ship_id` FOREIGN KEY (`id_type_ship`) REFERENCES `ships` (`id_type_ship`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `char_guild_id` FOREIGN KEY (`id_guild`) REFERENCES `guilds` (`id_guild`) ON DELETE RESTRICT ON UPDATE CASCADE;


ALTER TABLE `chars`
  MODIFY `id_char` int(11) NOT NULL AUTO_INCREMENT;
