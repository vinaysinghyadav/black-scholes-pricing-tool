from black_scholes import black_scholes_price

# Sample parameters
S = 100   # Current stock price
K = 100   # Strike price
T = 1     # Time to expiration (1 year)
r = 0.05  # Risk-free interest rate (5%)
sigma = 0.2  # Volatility (20%)

# Calculate call and put option prices
call_price = black_scholes_price(S, K, T, r, sigma, option_type="call")
put_price = black_scholes_price(S, K, T, r, sigma, option_type="put")

print(f"Call Option Price: {call_price}")
print(f"Put Option Price: {put_price}")
