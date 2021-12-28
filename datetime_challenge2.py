from datetime import datetime
import pytz

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

# print "utcmoment_naive: {0}".format(utcmoment_naive) # python 2
print("utcmoment_naive: {0}".format(utcmoment_naive))
print("utcmoment:       {0}".format(utcmoment))

localFormat = "%H:%M"

timezones = ['America/Los_Angeles', 'America/New_York', 'Europe/London']

for tz in timezones:
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    openTime = localDatetime.replace(hour=9, minute=0, second=0, microsecond=0)
    closeTime = localDatetime.replace(hour=17, minute=0, second=0, microsecond=0)

    print(tz + ": " + localDatetime.strftime(localFormat))

    if localDatetime >= openTime and localDatetime <= closeTime:
        print("Branch is Open\n")
    else:
        print("Branch is Closed\n")

            
