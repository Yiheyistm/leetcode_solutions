class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = deque((supplies))
        prerequesite = defaultdict(list)
        no_supply_needed = defaultdict(int)
        for recipe, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                prerequesite[ing].append(recipe)
                no_supply_needed[recipe] += 1
        newRecipe = []
        while supplies:
            ing = supplies.popleft()
            if ing in recipes:
                newRecipe.append(ing)
            for rec in prerequesite[ing]:
                no_supply_needed[rec] -= 1
                if not no_supply_needed[rec]:
                    supplies.append(rec)
        return newRecipe

                    
        
        

        