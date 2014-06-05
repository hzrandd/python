from apscheduler.scheduler import Scheduler

schedudler = Scheduler(daemonic = False)

@schedudler.cron_schedule(second='*', day_of_week='0-4', hour='8-12,13-15')
def quote_send_sh_job():
    print 'a simple cron job start at', datetime.datetime.now()

schedudler.start()
