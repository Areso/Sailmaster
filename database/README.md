# Sailmaster's database  
This folder contains DDL and DML for references  
Please, keep in mind, that you need to import (execute) those files in this precise order, otherwise you will get errors on creating foreign constraint keys.  
Nota bene: one of the popular reasons to prevent creating FK (In MySQL ERROR 1215) is difference type or size of FK-PK columns (tinyint-smallint, 4 vs 6 lenght)
