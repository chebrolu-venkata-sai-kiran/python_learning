drink_type = "cold"

def serve_drink():
    
    def kitchen():
        global drink_type
        drink_type = "hot"

    kitchen()
serve_drink()
print(f"the final drink type",drink_type)