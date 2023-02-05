from datetime import datetime
import pytz

def get_current_utc_time():
    return datetime.utcnow()

def get_current_time_by_timezone(tz):
    tz_zone = pytz.timezone(tz)
    datetime_zone = datetime.now(tz_zone)
    return datetime_zone

def get_formatted_datetime_string(datetime_obj, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(datetime_obj, format)

def get_datetime_obj_from_string(datetime_str, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(datetime_str, format)
