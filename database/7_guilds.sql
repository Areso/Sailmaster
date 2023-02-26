USE sailmaster;
CREATE TABLE `guilds` (
  `id_guild` smallint(6) NOT NULL,
  `id_owner` int(11) NOT NULL,
  `guild_name` varchar(64) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

ALTER TABLE `guilds`
  ADD PRIMARY KEY (`id_guild`);
