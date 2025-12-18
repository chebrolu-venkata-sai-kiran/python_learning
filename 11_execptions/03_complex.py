def serve_chai(flavour):

    try:
        print(f"preparing {flavour} chai..")
        if flavour =="unknown":
            raise ValueError("Invalid flavour")
    except ValueError as e:
        print(f"Error: {str(e)}")
    else:
        print("Chai preparation successful and",flavour,"chai served")
    finally:
        print("Next customer please")


serve_chai("green")
serve_chai("unknown")
