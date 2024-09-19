One of the most common crypto investment strategies is dollar cost averaging (DCA). DCA involves buying coins in small batches, regularly, as the prices trend down in the bear market. The purpose of DCA is to lower the portfolio’s average buying price as much as possible before the trend reverses.

Some crypto investors also categorize the coins in their portfolio on the following risk scales based on their analysis:

Very High Risk (1)
High risk (2)
Medium risk (3)
Low risk (4)
Investors use this scale to determine the percentage allocation of coins in their portfolio. Investors with limited capital have to continuously decide which coins, in their portfolio, they should prioritize every time they raise capital to invest.

This project assumes that the priority would be the coin with lowest risk and that will decrease the average buying price of the whole portfolio by the largest margin. The margin is simply the difference between the current portfolio average buying price (CPABP) and the final portfolio average buying price should the coin get purchased (current average bp – final average bp). The bigger this value (onwards referred to as Asset Deviation) the better. Factoring an investors risk analysis of the asset in the Asset Deviation provides a value (Priority Score) that an investor can use to prioritize the coins in their portfolio.

SCope
This project is a feature of portfolio management system and a not a full-fledged portfolio manager. The industry has so many free portfolio trackers but the major crypto portfolio management systems (for example cooinmarketcap.com, coingecko.com, coinstats.com) lack similar functionality.

Input and Output
This project takes a csv file path with the following headers:

name (the name of the coin)
risk score (the investors risk score 1, 2, 3, or 4 according to above categories)
balance (the number of coins bought)
investment (the amount of money used to buy the coins)
Calculations
Calculating Deviation
Asset value = current price * quantity Portfolio value = sum of asset values for the assets in the portfolio Asset weight = asset value / portfolio value CPABP = mean of (asset weights * buying prices) FPABP = mean of (asset weights * buying prices) after buying an asset Asset Deviation = CPABP – FPABP Asset Deviation = CPABP – FPABP Assuming that the amount of money to invest is constant, there is no need to calculate FPABP because we are not concerned with the exact value of FPABP, but how buying a certain asset will affects FPABP. This effect, therefore, is a factor of the asset weight in the portfolio and its average buying price in the portfolio. Therefore, Asset Deviation = CPABP – (asset weight * buying price)

Factoring the Risk Rssessment of the Investor
Given the scores for Low, Medium, High and Very high as 4, 3, 2, 1 respectively, a simple way to factor in the risk score is to multiply risk score with Deviation but that would create long values. Alternatively (risk score / 10) * Deviation generates more use friendly values for Priority Score.

Design Choices
The major design change made in this project was to use batch processing. The initial version calculated the DCA score for every asset and then compared the results for the assets. However, once API requests were integrated, it was clear that having requests for every coin would be slow. Also, calculating the scores in batches lead to fewer function calls although slightly longer functions.

A choice had to be made between letting a user enter the coins or submit a file. The argument for requiring a file path is sustain by the scope of the project as a feature that is to be integrated into a portfolio tracker and not a stand-alone system.

Modules
The project has four files:

project.py
test_project.py
reader.py
cmc_api.py Project.py has the main script that calls and runs reader.py and cmc_api.py. It also has three functions that complete the calculations that are the highlights of this project.
get_weight: returns the respective weights of the coins in the portfolio
get_deviation: returns a factor of deviation from the average weighted buying price of for each coin.
get_priority_scores: returns the final scores for the coins in the portfolio Reader.py has the function get_summary, that reads the .csv file that contains the coins and returns a summary in the form of a list of dictionaries as exemplified bellow. summary = [ {"name": "cardano", "risk score": 3, "balance": 200, "investment": 100}, {"name": "ethereum", "risk score": 4, "balance": 0.25, "investment": 500}, {"name": "solana", "risk score": 2, "balance": 20, "investment": 200}, ] Cmc_api.py handles the API requests. There are two API requests made in this file. The first request returns coin IDs from coinmarketcap.com. The second uses these IDs to get the current prices needed to process the coin weights in the main process. This is the recommended method according to coinmarketcap’s API documentations.
How to use the script
To use the script, run the project.py which should ask for a csv file path. Enter the file path and press enter to execute.
