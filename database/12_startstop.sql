USE sailmaster;
CREATE TABLE `startstop` (
  `id` tinyint(4) NOT NULL,
  `load_counter` mediumint(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

ALTER TABLE `startstop` ADD PRIMARY KEY(`id`);
INSERT INTO `startstop` (`id`, `load_counter`) VALUES ('1', '0');
