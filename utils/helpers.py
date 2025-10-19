import datetime

def format_ts(seconds):
    try:
        return str(datetime.timedelta(seconds=int(seconds)))
    except Exception:
        return "Unknown"
