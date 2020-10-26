CREATE TABLE `accounts` (
  `id_acc` int(11) NOT NULL,
  `login` varchar(128) DEFAULT NULL,
  `token` varchar(128) NOT NULL,
  `password` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `create_date` timestamp NULL DEFAULT NULL,
  `login_date` timestamp NULL DEFAULT NULL,
  `passupd_date` timestamp NULL DEFAULT NULL,
  `is_blocked` tinyint(1) NOT NULL DEFAULT '0',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id_acc`),
  ADD UNIQUE KEY `token` (`token`),
  ADD UNIQUE KEY `login` (`login`);

ALTER TABLE `accounts`
  MODIFY `id_acc` int(11) NOT NULL AUTO_INCREMENT;
