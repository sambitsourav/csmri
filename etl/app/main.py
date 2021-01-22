import logging as log
from config import conf
from web_socket import WebSocket
from my_sql_repository import MySQLRepository
log.basicConfig(level=log.DEBUG)

ticker_url = conf['ticker_url']
mySQLRepository = MySQLRepository(log)
webSocket = WebSocket(log,ticker_url,mySQLRepository)

def main():
    log.info('starting application')
    subscribe = {
            'eventName':'subscribe',
            'authorization':conf['ticker_auth'],
            'eventData': {
                'thresholdLevel': int(conf['ticker_subscribe_level'])
        }
    }
    webSocket._send(subscribe)


if __name__ == "__main__":
    main()



# ws = create_connection("wss://api.tiingo.com/iex")

# subscribe = {
#         'eventName':'subscribe',
#         'authorization':'e3d26c15fd97593eae2f35702cc6e3960f53e714',
#         'eventData': {
#             'thresholdLevel': 5
#     }
# }

# ws.send(json.dumps(subscribe))
# while True:
#     print(ws.recv())

# 