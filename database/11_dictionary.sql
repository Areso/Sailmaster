CREATE TABLE `dictionary` (
  `id_word` smallint(6) NOT NULL,
  `id_race` smallint(6) NOT NULL,
  `id_type_of_word` tinyint(4) NOT NULL,
  `gender` smallint(1) NOT NULL,
  `word` varchar(16) NOT NULL,
  `stop_list` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO `dictionary` (`id_word`, `id_race`, `id_type_of_word`, `gender`, `word`, `stop_list`) VALUES
(0, 1, 0, 1, 'Eric', NULL),
(1, 1, 0, 0, 'Erica', NULL),
(2, 1, 0, 1, 'Max', NULL),
(3, 1, 0, 0, 'Anna', NULL),
(4, 1, 0, 0, 'Bella', NULL),
(5, 1, 0, 0, 'Helen', NULL),
(6, 1, 0, 0, 'Victoria', NULL),
(7, 1, 0, 1, 'Victor', NULL),
(8, 1, 1, 3, 'Mad', NULL),
(9, 1, 1, 3, 'Crazy', NULL),
(10, 1, 1, 3, 'Bloody', NULL),
(11, 1, 1, 0, 'Fair', NULL),
(12, 1, 1, 3, 'Honest', NULL),
(13, 1, 1, 3, 'Red', NULL),
(14, 2, 0, 1, 'Azok', NULL),
(15, 2, 0, 1, 'Borg', NULL),
(16, 2, 0, 1, 'Golfembul', NULL),
(17, 2, 0, 1, 'Gorbug', NULL),
(18, 2, 0, 1, 'Aknakh', NULL),
(19, 2, 0, 1, 'Shagrad', NULL),
(20, 2, 0, 1, 'Uglyuk', NULL),
(21, 2, 0, 0, 'Issa', NULL),
(22, 2, 0, 0, 'Sharn', NULL),
(23, 2, 1, 3, 'Crazy', NULL),
(24, 2, 1, 3, 'Cruel', NULL);

ALTER TABLE `dictionary`
  ADD PRIMARY KEY (`id_word`);
