#add import
from question_d import Stock

microsoft = Stock("MSFT", "Microsoft")

print("Company Symbol:", microsoft.get_symbol())
print("Company Name:", microsoft.get_company_name())