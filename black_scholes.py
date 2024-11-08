import math
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Black-Scholes price for European call or put options.

    Parameters:
    - S (float): Current stock price
    - K (float): Strike price of the option
    - T (float): Time to expiration in years
    - r (float): Risk-free interest rate
    - sigma (float): Volatility of the stock
    - option_type (str): "call" for Call option, "put" for Put option
    
    Returns:
    - price (float): Theoretical price of the option
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")

    return price
