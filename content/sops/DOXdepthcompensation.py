# From El Nino profile
O2 = 0.4 # mg/L
depth = 1000 # dbars 

# Convert to uM
O2_uM = O2 * 1000 / 31.999

# Compute depth compensation in micromolar 
O2_c_uM = O2_uM * (1 + 0.032 * depth / 1000) 

# Convert to mg/L
O2_c = O2_c_uM * 31.999 / 1000

print(
    f"O2 = {O2}", 
    f"O2_c = {O2_c:.2f} at {depth} dbar"
)
