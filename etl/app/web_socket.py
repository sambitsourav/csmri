import time
from datetime import datetime
from utils import cst_string_to_timestamp
from websocket import create_connection
import simplejson as json
class WebSocket:
    def __init__(self,logger,url,repository):
        self.logger = logger
        self.logger.info('starting to establish web socket connection with {0}'.format(url))
        self.ws = create_connection(url)
        self.logger.info('connected : ws = {0}'.format(self.ws))
        self.schema = [('update_message_type','str'),('date','datetime'),('Nanoseconds','int'), \
            ('Ticker','str'),('Bid_Size','int'),('Bid_Price','int'),('Mid_Price','int'),('Ask_Price','int'),('Ask_Size','int'), \
            ('Last_Price','float'),('Last_Size','int'),('Halted','int'),('After_Hours','int'),('ISO','int'),('Oddlot','int'),('NMS_Rule','int')]
        self.repository = repository
        
        
    def _send(self,subscriber_payload):
        self.ws.send(json.dumps(subscriber_payload))
        while True:
            load_recieved = json.loads(self.ws.recv())
            self.logger.debug('type of object recieved is {0}'.format(type(load_recieved)))
              
            assert load_recieved['messageType'] in ['A','H','I']  , 'Message type not correct'
            try : 
                self.logger.info(load_recieved['data'])  
            except KeyError as e : 
                self.logger.info('skipping payload with message type '+str(load_recieved['messageType']))
                continue
            data = load_recieved['data']
            self.logger.debug('data is {0}'.format(data))
            self.logger.debug('type of data is {0}'.format(type(data)))
            if not len(data) == 16 :
                self.logger.info('skipping current pay load')
                continue
            parsed_data = {}
            for i in range(0,len(data)):
                if self.schema[i][1] == 'str' : 
                    try :
                        data[i] = str(data[i])
                    except :
                        pass
                elif self.schema[i][1] == 'int' :
                    try : 
                        data[i] = int(data[i])
                    except :
                        pass
                elif self.schema[i][1] == 'float' :
                    try :
                        data[i] = float(data[i])
                    except :
                        pass
                elif self.schema[i][1] == 'datetime' :
                    data[i] = cst_string_to_timestamp(data[i],self.logger)
                else :
                    self.logger.info('skipping current pay load')
                
                parsed_data[self.schema[i][0]] = data[i]
            parsed_data['update_time'] = parsed_data['date']
            del parsed_data['date']
            self.logger.debug('parsed data is {0}'.format(parsed_data))
            self.repository._insert_real_time_record(parsed_data)
            self.logger.info('completed processing payload')
            # time.sleep(2)