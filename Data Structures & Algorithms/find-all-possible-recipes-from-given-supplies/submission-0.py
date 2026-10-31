class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        s = set(supplies)
        res = []
        while True:
            changed = False
            for i in range(len(ingredients)):
                if recipes[i] in s:
                    continue
                test = True
                for ii in ingredients[i]:
                    if ii not in s:
                        test = False
                if test:
                    # can make i
                    res.append(recipes[i])
                    s.add(recipes[i])
                    change = True
                test = True
            if not changed:
                break
            
        return res