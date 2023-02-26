USE sailmaster;
ALTER TABLE `guilds`
    ADD CONSTRAINT `guild_char_id` FOREIGN KEY (`id_owner`) REFERENCES `chars` (`id_char`) ON DELETE RESTRICT ON UPDATE CASCADE;
