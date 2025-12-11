device_status = 'active'
temperature = 34

if device_status =='active':
    if temperature >35:
        print(f"device is warm")
    else:
        print(f"device is cool")
else:
    print(f"device is offline")
