"""d scheduler sends an external command to Nagios for downtime.

Usage:
  downtime-scheduler run <host> <start> <stop>
  downtime-scheduler (-h | --help)
  downtime-scheduler --version

Options:
  -h --help                 Show this screen.

downtime-scheduler.py run host start stop
downtime-scheduler.py run host 8 22

"""
import sys,os,json,logging, datetime, time
from logging import handlers
import ConfigParser
import datetime
from docopt import docopt

now = datetime.datetime.now()
config = ConfigParser.ConfigParser()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init():
    # Add rolling file appender (rotates each day at midnight)
    handler = logging.handlers.TimedRotatingFileHandler('/var/log/downtime-scheduler.log',when='midnight')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def runscheduler(host, startTime, stopTime):
    startTime = int(startTime)
    stopTime = int(stopTime)
    currentHour = int(now.hour)
    logging.info("current time: " + str(currentHour) + ", start time: " + str(startTime) + ", stopTime: " + str(stopTime
    os.system('curl -d "cmd_typ=55&cmd_mod=2&host=' + str(host) + '&com_author=TeamDev+Support&com_data=ddds&trigger=0&start_time=2017-11-20+' + str(startTime) + '%3A00%3A38&end_time=2017-11-20+' + str(stopTime) + '%3A10%3A25&fixed=1&hours=2&minutes=0&childoptions=0&btnSubmit=Commit" "https://nagios_server/nagios/cgi-bin/cmd.cgi" -u "[nagios_user]:[nagios_password]" --insecure')



if __name__ == "__main__":
    args = docopt(__doc__, version='AWS 1.0.1')
    init()
    runscheduler(args['<host>'], args['<start>'], args['<stop>'])

