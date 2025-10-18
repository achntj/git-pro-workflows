from fuel_api import price_multiplier

def route_cost(base):
    return base * price_multiplier() * price_multiplier()

if __name__ == "__main__":
    print(route_cost(100))

# minor refactor
