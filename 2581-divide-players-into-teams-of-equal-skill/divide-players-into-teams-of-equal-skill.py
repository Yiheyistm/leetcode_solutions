class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        sk = skill[0] + skill[-1]
        for i in range(len(skill) // 2):
            ch = skill[i] * skill[len(skill) -i -1]
            chemistry += ch
            if sk != skill[i] + skill[len(skill) -i -1]:
                chemistry = -1
                break
        return chemistry

