USE sailmaster;
CREATE TABLE `settings` (
  `id_setting` smallint(6) NOT NULL,
  `setting_name` varchar(128) NOT NULL,
  `value` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO `settings` (`id_setting`, `setting_name`, `value`) VALUES
(0, 'allow_custom_charnames', 1),
(1, 'rename_level_req', 3),
(2, 'shadow_char_naming', 0);

ALTER TABLE `settings`
  ADD PRIMARY KEY (`id_setting`);

