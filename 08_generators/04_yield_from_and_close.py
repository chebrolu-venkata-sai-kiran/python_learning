def local_drink():
    yield "cold coffee"
    yield "coke"

def import_drink():
    yield "imported coffee"
    yield "imported coke"

def full_drinks():
    yield from local_drink()
    yield from import_drink()

for drink in full_drinks():
    print(drink)


def drink_stall():
    try:
        while True:
            order = yield "waiting for drink order"
    except:
        print("stall closed")

stall = drink_stall()

print(next(stall))
stall.close()