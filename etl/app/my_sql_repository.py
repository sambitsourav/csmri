import mysql.connector
from config import conf
class MySQLRepository:
    def __init__(self,logger):
        self.db = mysql.connector.connect(
        host=conf['host'],
        user=conf['user'],
        password=conf['password'],
        database=conf['database']
        )
        self.cursor = self.db.cursor()
        self.logger = logger

    def _insert_real_time_record(self,data_dict):
        table = conf['real_time_record_table']
        sql = "INSERT INTO "+table+" (update_message_type, update_time, Nanoseconds, Ticker, Bid_Size, Bid_Price, Mid_Price, Ask_Price, Ask_Size, \
            Last_Price, Last_Size, Halted, After_Hours, ISO, Oddlot, NMS_Rule) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.logger.debug('sql query is {0}'.format(sql))
        insert_list = []
        for k,v in data_dict.items(): 
            insert_list.append(v)
        
        self.cursor.execute(sql, (data_dict['update_message_type'],data_dict['update_time'],data_dict['Nanoseconds'],data_dict['Ticker'], \
            data_dict['Bid_Size'],data_dict['Bid_Price'],data_dict['Mid_Price'],data_dict['Ask_Price'],data_dict['Ask_Size'],data_dict['Last_Price'], \
            data_dict['Last_Size'],data_dict['Halted'],data_dict['After_Hours'],data_dict['ISO'],data_dict['Oddlot'],data_dict['NMS_Rule']))
        self.db.commit()
        self.logger.debug(self.cursor.rowcount, "record inserted.")
        return True
