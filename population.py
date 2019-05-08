def population_growth(initial_pop, annual_growth_rate, target_pop):
    if annual_growth_rate <= 0:
        return "invalid growth rate"

    count: int = 0
    new_pop: int = 0

    while new_pop < target_pop:
        count += 1
        new_pop = initial_pop * (1 + annual_growth_rate) ** count
        print(new_pop)

    return count


if __name__ == "__main__":
    print('test')
    print(population_growth(5000, 0.1, 10000))
