def vat_calculation(amount, tax_rate):
    return amount * (1 + tax_rate)

print(f"the final amount after adding VAT is:",vat_calculation(120, 0.08))

prices =[100,200,300]

for i in prices:
    print(f"original price is {i} and the final amount after adding VAT is:",vat_calculation(i, 0.1))