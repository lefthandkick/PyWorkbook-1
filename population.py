def population_growth(initial_pop, annual_growth_rate, target_pop) -> int:
    if annual_growth_rate <= 0:
        print('invalid growth rate - start over')
        return -1

    count:   int = 0
    new_pop: float = 0

    def exponent(value: float, times: int) -> float:
        ret_val: float = 1
        for i in range(times):
            ret_val = ret_val * value

        return ret_val

    while new_pop < target_pop:
        count += 1

        new_pop = exponent(float((1 + annual_growth_rate)), count)
        new_pop = initial_pop * new_pop

    return count


def main():
    pop_today:   float = 5000.0
    growth_rate: float = 0.1
    target_pop:  float = 10000.0

    print(f'\n It will take {population_growth(pop_today, growth_rate, target_pop)} years.')
    print(f'\n to get to a population of {int(target_pop)} ')


main()

