import datetime
import logging
import os

import azure.functions as func
from GoogleAdWords_V2 import apicall

#where you are reading from and writing to

def main(mytimer: func.TimerRequest) -> None:
    
    Customer_ID = os.getenv(customer_id)

    apicall(Customer_ID)

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


