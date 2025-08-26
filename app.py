import streamlit as st
import math


# This function calculates the total cost for one rebalancing cycle,
# including impermanent loss, swap fees, and a fixed gas fee.
def calculate_rebalancing_cost(
    total_lp_value_usd: float, range_percentage: float
) -> float:
    """
    Calculates the total cost for one rebalancing cycle.

    Args:
        total_lp_value_usd: The total value of the liquidity pool position in USD.
        range_percentage: The range as a percentage (e.g., 5 for 5%).

    Returns:
        The total cost in USD.
    """
    GAS_FEE = 1.50
    SWAP_FEE_TIER = 0.0030
    k = 1 + (range_percentage / 100)

    impermanent_loss_percent = abs((2 * math.sqrt(k) / (1 + k)) - 1)
    il_cost_usd = total_lp_value_usd * impermanent_loss_percent

    swap_value_usd = total_lp_value_usd / 2
    swap_fee_usd = swap_value_usd * SWAP_FEE_TIER

    total_cost_usd = il_cost_usd + swap_fee_usd + GAS_FEE

    return total_cost_usd


# This function calculates the range percentage on each side of the
# current price, assuming the current price is the arithmetic mean
# of the min and max prices.
def calculate_range_each_side(min_price: float, max_price: float) -> float:
    """
    Calculates the range percentage on each side.

    Args:
        min_price: The minimum price in the range.
        max_price: The maximum price in the range.

    Returns:
        The range percentage on each side.
    """
    current_price = (min_price + max_price) / 2
    range_size = max_price - current_price
    range_percent = (range_size / current_price) * 100

    return range_percent


# The Streamlit application UI
st.title("LP Rebalancing Cost Calculator")
st.subheader("Calculate the minimum fees needed to cover your rebalancing costs.")

# Assumptions for the calculator
with st.expander("Assumptions for this calculator"):
    st.markdown("""
        This calculator requires the following assumptions to be met:
        1. **Chain:** The calculation is based on fees and gas costs typical for the **Arbitrum** chain.
        2. **Liquidity Position:** You are adding liquidity with a **50/50** token split (equal value of both assets).
        3. **Rebalancing Trigger:** You remove liquidity when your position has a **0/100** token split (all value is in one of the assets).
        4. **Current Price:** The current price is assumed to be the **arithmetic average** of the minimum and maximum prices you input.
    """)

total_value = st.number_input(
    "Total LP Value in USD", min_value=100.0, value=1000.0, step=50.0
)

min_p = st.number_input(
    "Minimum Price", min_value=0.0, value=0.0394, format="%.4f", step=1e-4
)
max_p = st.number_input(
    "Maximum Price", min_value=0.0, value=0.0438, format="%.4f", step=1e-4
)


if st.button("Calculate Cost"):
    if max_p <= min_p:
        st.error("Maximum Price must be greater than Minimum Price.")
    else:
        range_percent = calculate_range_each_side(min_p, max_p)

        # Display the calculated range percentage
        st.info(f"Calculated Range Percentage: **{range_percent:.2f}%**")

        # Now calculate the cost with the derived range_percent
        cost = calculate_rebalancing_cost(total_value, range_percent)

        st.metric(label="Total Break-Even Cost", value=f"${cost:.2f}")
        st.write(
            "You must earn at least this amount in fees to cover the cost of one rebalancing."
        )
