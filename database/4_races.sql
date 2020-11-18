USE sailmaster;
CREATE TABLE `races` (
  `id_race` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

ALTER TABLE `races`
  ADD PRIMARY KEY (`id_race`);
