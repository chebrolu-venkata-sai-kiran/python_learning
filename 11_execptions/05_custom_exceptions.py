def brew_drinks(flavour):
    # Check if the given flavour is valid
    if flavour not in ["cold", "medium", "large"]:
        raise ValueError("Invalid flavour")
    
brew_drinks("hot")