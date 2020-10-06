import asyncio
import json
import logging
import websockets
import aiomysql

logging.basicConfig()

STATE = {"value": 0}
CHAT_MSG_ARR = []
USERS = set()


def state_event():
    return json.dumps({"type": "state", "msg": CHAT_MSG_ARR})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    print('path is '+path)
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            print(data)
            new_messsage = data["msg"]
            CHAT_MSG_ARR.append(new_messsage)
            await notify_state()
    #except:
    #    await unregister(websocket)
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
