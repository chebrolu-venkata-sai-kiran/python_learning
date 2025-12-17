# when we want our method can be used with out using the objects we can declare as a static method



class DrinkUtils:

    @staticmethod
    def clean_items(text):
        return [i.strip() for i in text.split(",")]
    
raw = "tea ,  coffee ,mojito,water       ,mocha"

cleaned_items = DrinkUtils.clean_items(raw)

print(cleaned_items)
print(DrinkUtils.clean_items(raw))