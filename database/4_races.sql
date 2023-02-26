USE sailmaster;
CREATE TABLE `races` (
  `id_race` smallint(6) NOT NULL,
  `race_name` varchar(24) NOT NULL,
  `homeport_x` smallint(6) NOT NULL,
  `homeport_y` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO `races` (`id_race`, `race_name`, `homeport_x`, `homeport_y`) VALUES
(1, 'Humans', 0, 0),
(2, 'Orcs', 3, 1);

ALTER TABLE `races`
  ADD PRIMARY KEY (`id_race`);
