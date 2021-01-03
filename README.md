# Sailmaster  
## Technologies and architecture
Sailmaster is turn-based MMORPG.  
The client is a single-page application (HTML5, Canvas, vanilla JavaScript), but it could be changed at anytime.  
There are could be few clients, thanks to open API of the backend.  
The server is a two-component application.  
Webserver handles endpoints, with whom the client is communicate.  
The webserver application is written in Python (Flask for http calls, asyncio for websockets).  
Finally, there is a gameserver.  
The gameserver contains all gamelogic and written in Go (Golang).  
There is a RabbitMQ as communication middleware between webserver and gameserver.  
The game's RDBMS is MySQL for now (for fast prototyping, thanks for phpmyadmin).  
In the future it will be switched to PostgreSQL.  
  
## The game
The game's has core loop:  
1) all players interacts with NPC and their ships (sends orders) within the timeframe (30 sec for now);  
2) the server calculates all orders, battles, movements;  
3) all players, who currently online, got results from server and the client draws animation;  
4) when animation is done, all players get control on their's characters and could issue new orders once again.  
  
Usually, when a player logged off, the player's character placed in somewhat 'stasis' and disappear from the game. And appears back only when the player is logging in.  
In this game, the character is always in the game, disregarding the online/offline state of the player itself.  
So, without the player attending, the player character becomes somewhat NPC-like, which could do some pre-written actions and somehow react to external stimuli, based on the scenarios which were written by the player.  
  
It is Race-vs-Race game. 5 races, 6 fractions.  
Humans, Elves, Orcs, Undead, Dwarves, Renegades.  
While all fractions are playable, a player of any race could become a renegade only playing the role.  
  
## LICENSE
The source code and the documentation is licensed under Apahce License 2.0 for now  
All assets, including graphic, sound, animation are under a proprietary license  
Author is Gladyshev Anton, 2020  

## RUNNING
Install mysql  
Create user, database  
Install RabbitMQ
        sudo docker run -d --hostname rabbitmq1 --name rabbitmq1 -p 5672:5672 -p 15672:15672 rabbitmq:3-management  
Run RabbitMQ
        docker start rabbitmq1  
Run webserver
        webserver$ python3 webserver_auth.py  
Compile and Run gameserver
        gameserver$ go build  
        gameserver$ ./gameserver  
