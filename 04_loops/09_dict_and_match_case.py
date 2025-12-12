# getting disocunts based on the copoun code 

users = [
    {"name":"sai","total_amount": 1000,"coupon_code":"DISCOUNT10"},
    {"name":"kiran","total_amount": 2000,"coupon_code":"DISCOUNT20"},
    {"name":"chebrolu","total_amount": 3000,"coupon_code":"DISCOUNT30"},
    {"name":"venkata","total_amount": 4000,"coupon_code":"DISCOUNT40"},
    {"name":"venkat","total_amount": 900,"coupon_code":"DISCOUNT90"}

]

discounts = {
    "DISCOUNT10": (0.3,200),
    "DISCOUNT20": (0.2,500),
    "DISCOUNT30": (0.1,700),
    "DISCOUNT40": (0.5,1000),
    "DISCOUNT90": (0.5,10),

}

for user in users:
    percent,fixed = discounts.get(user["coupon_code"], (0,0))
    discounted_amount = user["total_amount"] * percent + fixed
    print(f"{user['name']}'s total amount after applying the coupon code {user['coupon_code']} is {discounted_amount} for the total amount {user['total_amount']} ")