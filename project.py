from statistics import mean
import reader
import cmc_api  # my  module for querying CMC APIs


def main():
    file_path = input("entre file path: ")
    try:
        summary = reader.get_summary(file_path)
    except Exception as e:
        print(e)
    else:
        print("......")
        current_prices = cmc_api.get_prices(summary)
        coin_weights = get_coin_weights(summary, current_prices)
        deviations = get_deviations(summary, coin_weights)
        priority_scores = get_priority_scores(summary, deviations)
        for key, value in priority_scores.items():
            print(f"{key}, {value}")


def get_coin_weights(summary, current_prices) -> "dict of coins and respective weights":
    # coin weight is the fraction of portfolio value account for by a coin
    portfolio_value = 0
    coin_values = {}
    coin_weights = {}

    # get the value of every coin
    for coin in summary:
        current_price = current_prices[coin['name']]
        coin_value = coin["balance"] * current_price
        portfolio_value += coin_value
        coin_values.update({coin["name"]: coin_value})

    # get the weight of every coin
    for coin in summary:
        coin_weight = coin_values[coin["name"]] / portfolio_value
        coin_weights.update({coin["name"]: round(coin_weight, 4)})

    return coin_weights


def get_deviations(summary, coin_weights) -> dict:
    portfolio_weighted_bps = []
    weighted_bps = {}
    deviations = {}

    # get the buying price of coins
    for coin in summary:
        buying_price = coin["investment"] / coin["balance"]
        coin_weighted_bp = coin_weights[coin["name"]] * buying_price
        weighted_bps.update({coin["name"]: coin_weighted_bp})
        portfolio_weighted_bps.append(coin_weighted_bp)

    # get coin buying price deviation from the portfolio's mean weighted buying price
    for coin in summary:
        deviation = mean(portfolio_weighted_bps) - weighted_bps[coin["name"]]
        deviations.update({coin["name"]: round(deviation, 4)})

    return deviations


def get_priority_scores(summary, deviations) -> "risk factored deviations sorted descending":
    # deviations = get_deviations(summary)
    scores = {}
    for coin in summary:
        risk_score = coin["risk score"]
        deviation = deviations[coin["name"]]
        score = risk_score / 10 * deviation
        scores.update({coin["name"]: round(score, 2)})

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    final_scores = {}
    for i in sorted_scores:
        final_scores.update({i[0]: i[1]})

    return final_scores


if __name__ == '__main__':
    main()
