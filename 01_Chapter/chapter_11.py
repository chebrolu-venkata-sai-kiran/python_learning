import arrow

time = arrow.utcnow()

print(f"Current date and time in UTC: {time.format('YYYY-MM-DD HH:mm:ss')}")