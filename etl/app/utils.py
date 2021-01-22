from datetime import datetime
def cst_string_to_timestamp(timestamp,logger):
    timestamp = timestamp.split('.')[0]
    datetime_timestamp = None
    try : 
        datetime_timestamp = datetime.strptime(timestamp,"%Y-%m-%dT%H:%M:%S")
    except :
        logger.debug('could not parse timestamp {0}'.format(timestamp))
        return None
    logger.debug('timestamp converted succesfully {0}'.format(datetime_timestamp))
    return datetime_timestamp