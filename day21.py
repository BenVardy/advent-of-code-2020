from typing import Dict, List, Set, Tuple


class Food(object):
    def __init__(self, ingredients: List[str], allergens: List[str]) -> None:
        self.ingredients = ingredients
        self.allergens = allergens

    def __repr__(self) -> str:
        return '{} -> {}'.format(self.allergens, self.ingredients)

    def contains_ingredient(self, ingredient: str) -> bool:
        return ingredient in self.ingredients

    def contains_allergen(self, allergen: str) -> bool:
        return allergen in self.allergens

    def remove_ingredient(self, ingredient: str) -> None:
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)


def parse_input(lines: List[str]) -> Tuple[List[Food], List[str]]:
    all_ingredients: List[str] = []
    all_allergens_set: Set[str] = set()
    foods: List[Food] = []
    for line in lines:
        i_sec, a_sec = line.split(' (contains ')
        ingredients = i_sec.split(' ')
        all_ingredients += ingredients

        allergens = a_sec[:-1].split(', ')
        all_allergens_set |= set(allergens)

        foods.append(Food(ingredients, allergens))

    foods = sorted(foods, key=lambda x: len(x.allergens))
    return (foods, all_ingredients)


def find_invalid(foods: List[Food]) -> List[str]:
    invalid_ingredients: Dict[str, Set[str]] = {}
    for i, food in enumerate(foods):
        ingredients = food.ingredients
        allergens = food.allergens

        for ingredient in ingredients:
            if ingredient in invalid_ingredients:
                if invalid_ingredients[ingredient].issubset(allergens):
                    continue
            else:
                invalid_ingredients[ingredient] = set()
            valid = False
            for allergen in allergens:
                valid_for_allergen = True
                for j, other_food in enumerate(foods):
                    if i == j:
                        continue
                    if other_food.contains_allergen(allergen):
                        if not other_food.contains_ingredient(ingredient):
                            valid_for_allergen = False
                            break

                if valid_for_allergen:
                    valid = True
                    break

            if not valid:
                invalid_ingredients[ingredient] |= set(allergens)
            elif len(invalid_ingredients[ingredient]) != 0:
                invalid_ingredients[ingredient] = set()

    # Filter out empty ones as they're valid
    invalid_ingredients = {k: v for k, v in invalid_ingredients.items() if len(v) != 0}
    return list(invalid_ingredients.keys())


def part1(lines: List[str]):
    foods, all_ingredients = parse_input(lines)

    invalid_ingredients = find_invalid(foods)
    total = sum(all_ingredients.count(k) for k in invalid_ingredients)
    print(total)


def part2(lines: List[str]):
    foods, _ = parse_input(lines)

    invalid_ingredients = find_invalid(foods)
    for food in foods:
        for ingredient in invalid_ingredients:
            food.remove_ingredient(ingredient)

    valid_ingredients_sets: Dict[str, Set[str]] = {}
    for i, food in enumerate(foods):
        ingredients = food.ingredients
        allergens = food.allergens

        for ingredient in ingredients:
            if ingredient in valid_ingredients_sets:
                if set(allergens).issubset(valid_ingredients_sets[ingredient]):
                    continue
            else:
                valid_ingredients_sets[ingredient] = set()

            for allergen in allergens:
                valid_for_allergen = True
                for j, other_food in enumerate(foods):
                    if i != j and other_food.contains_allergen(allergen):
                        if not other_food.contains_ingredient(ingredient):
                            valid_for_allergen = False
                            break

                if valid_for_allergen:
                    valid_ingredients_sets[ingredient] |= set([allergen])

    valid_ingredients = [(k, list(v)) for k, v in valid_ingredients_sets.items()]
    valid_ingredients.sort(key=lambda x: len(x[1]))

    found: Dict[str, str] = {}
    while len(valid_ingredients) > 0:
        n_ingredient, n_allergens = valid_ingredients.pop(0)
        if len(n_allergens) != 1:
            raise Exception('We have a problem')

        n_allergen = n_allergens[0]
        found[n_ingredient] = n_allergen
        valid_ingredients = [(ingredient, [x for x in allergen if x != n_allergen]) for ingredient, allergen in valid_ingredients]
        valid_ingredients.sort(key=lambda x: len(x[1]))

    print(','.join(k for k, _ in sorted(found.items(), key=lambda x: x[1])))


def main():
    f = open('inputs/day21.txt')
    lines = f.read().strip().split('\n')

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
