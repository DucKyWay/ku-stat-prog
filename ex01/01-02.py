import numpy as np

income = ["20K", "3M", "12K", "0.04M", "0.023K", "-", "16K", "740K", "15K", "40K",
         "-", "17K", "-", "120K", "56K", "-", "42K", "2M", "0.14M", "60K"]
eval("2*1000")
income_number = np.array([])

# Code
for value in income:
    if value == "-":
        income_number = np.append(income_number, np.nan) 
    elif "K" in value:
        income_number = np.append(income_number, float(value.replace("K", "")) * 1000)
    elif "M" in value:
        income_number = np.append(income_number, float(value.replace("M", "")) * 1000000)
    else:
        income_number = np.append(income_number, float(value))
# np.set_printoptions(precision=1, suppress=False, threshold=np.inf, linewidth=80)
formatted_income_number = [f"{x:.1e}" if not np.isnan(x) else "nan" for x in income_number]
# is that good wa

print(f"array({formatted_income_number})")
print(type(income_number).__name__)
print(f"dtype('{income_number.dtype}')")
print(np.nanmean(income_number))
print(np.nanmedian(income_number))