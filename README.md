# Sailmaster  
Sailmaster is a client-server game.
Client is a single-page application (HTML5, Canvas, vanilla JavaScript), but could be changed at anytime.  
There are could be few clients.  
The server is a two-component application.  
Webserver handles endpoints, with whom the client is communicate.  
The webserver application is written in Python (Flask).  
Finally, there is a gameserver.  
The gameserver contains all gamelogic and written in Go (Golang).  
The game's RDBMS is MySQL for now (for fast prototyping, thanks for phpmyadmin).  
In the future it will be switched to PostgreSQL.  
There is RabbitMQ, not yet implemented, but planned to implement as soon as possible.  
It will be used for communication purposes between the webserver and the gameserver.
