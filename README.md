# 💵 LP Rebalancing Cost Calculator

This Streamlit application provides a simple, intuitive tool for liquidity providers to estimate the break-even cost of rebalancing a concentrated liquidity position. It helps users determine the minimum fees they need to earn to cover the costs associated with moving their position.

## ⚙️ How It Works

The calculator takes three inputs from the user:

- **Total LP Value in USD:** The total value of your liquidity pool position.
- **Minimum Price:** The lower bound of your chosen price range.
- **Maximum Price:** The upper bound of your chosen price range.

Using these inputs, the application performs the following calculations to determine the total rebalancing cost for a single cycle:

1.  **Calculates the range percentage:** It first determines the price range percentage based on the minimum and maximum prices you provided. This is crucial for calculating impermanent loss.
2.  **Estimates Impermanent Loss (IL):** It calculates the percentage of impermanent loss that would occur when the price moves from the center of your range to one of the boundaries, where your position would be 100% in one asset.
3.  **Adds Swap Fees:** It accounts for the fees incurred when swapping the assets to re-establish a 50/50 position.
4.  **Includes a Fixed Gas Fee:** A fixed gas fee (assumed to be $1.50) is added to the total.

The final output is the **Total Break-Even Cost**, which represents the minimum amount of fees your position must generate to justify a rebalancing event.

## ⚠️ Key Assumptions

This calculator is based on several key assumptions:

1.  **Chain:** The gas fee is based on a typical transaction cost on the **Arbitrum** network.
2.  **Liquidity Position:** The calculation assumes an initial **50/50** token split (equal value of both assets).
3.  **Rebalancing Trigger:** It assumes rebalancing occurs when the position has a **0/100** token split, meaning the price has moved out of your range entirely.
4.  **Current Price:** The current price is assumed to be the arithmetic average of the minimum and maximum prices.

## 🚀 Getting Started

To run this application locally, you'll need Python and `pip`.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/weiweiyeih/il-calculator.git](https://github.com/weiweiyeih/il-calculator.git)
    cd il-calculator
    ```
2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    - **Note:** Your `requirements.txt` file should contain `streamlit`. You may have other dependencies as well.
4.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

The application will open in your default web browser.

## 🤝 Contributing

Feel free to open an issue or submit a pull request if you'd like to improve the calculator, add more features, or correct any assumptions.
