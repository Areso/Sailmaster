USE sailmaster;
CREATE TABLE `races` (
  `id_race` smallint(6) NOT NULL,
  `race_name` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO `races` (`id_race`, `race_name`) VALUES
(1, 'Humans'),
(2, 'Orcs');

ALTER TABLE `races`
  ADD PRIMARY KEY (`id_race`);
