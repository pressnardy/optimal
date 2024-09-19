import pytest
import project
import reader

summary = [
        {"name": "cardano", "risk score": 3, "balance": 200, "investment": 100},
        {"name": "ethereum", "risk score": 4, "balance": 0.25, "investment": 500},
        {"name": "solana", "risk score": 2, "balance": 20, "investment": 200},
    ]

current_prices = {"cardano": 0.2, "ethereum": 1600, "solana": 18}
coin_values = {"cardano": 40, "ethereum": 400, "solana": 360}
portfolio_value = 800
coin_weights = {"cardano": 0.05, "ethereum": 0.5, "solana": 0.45}
coin_weighted_bp = {"cardano": 0.025, "ethereum": 1000, "solana": 4.5}
portfolio_weighted_bp = 334.8416
coin_deviations = {"cardano": 334.8167, "ethereum": -665.1583, "solana": 330.3417}
dca_scores = {"cardano": 100.45, "solana": 66.07, "ethereum": -266.06}


def test_get_summary():
    with pytest.raises(FileNotFoundError):
        reader.get_summary("asr.png")


def test_coin_weights():
    global summary
    global current_prices
    assert project.get_coin_weights(summary, current_prices) == {
        "cardano": 0.05,
        "ethereum": 0.5,
        "solana": 0.45
    }


def test_deviations():
    global summary
    global coin_weights
    assert project.get_deviations(summary, coin_weights) == {
        "cardano": 334.8167,
        "ethereum": -665.1583,
        "solana": 330.3417
    }


def test_dca_scores():
    global summary
    global coin_deviations
    assert project.get_dca_scores(summary, coin_deviations) == {
        "cardano": 100.45,
        "ethereum": -266.06,
        "solana": 66.07
    }




