import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from scipy.stats import norm


# Black Sholes Option Pricing Model

# Black-Scholes option pricing model
def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

# Streamlit app
def main():
    st.title("Option Pricing App")

    # Sidebar
    st.sidebar.header("User Input")
    S = st.sidebar.number_input("Current Stock Price (S)", value=100.0)
    K = st.sidebar.number_input("Option Strike Price (K)", value=100.0)
    T = st.sidebar.number_input("Time to Expiry (T) in years", value=1.0)
    r = st.sidebar.number_input("Risk-free Rate (r)", value=0.05)
    sigma = st.sidebar.number_input("Volatility (σ)", value=0.2)

    option_type = st.sidebar.radio("Option Type", ('call', 'put'))

    # Option Pricing
    option_price = black_scholes(S, K, T, r, sigma, option_type)

    # Display result
    st.write(f"**{option_type.capitalize()} Option Price:** ${round(option_price, 2)}")

if __name__ == "__main__":
    main()