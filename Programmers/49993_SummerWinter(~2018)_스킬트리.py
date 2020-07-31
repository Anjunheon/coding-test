def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        idx = -1
        for j in range(len(skill_trees[i])):
            if (skill_trees[i][j] in skill):
                if idx + 1 == skill.index(skill_trees[i][j]):
                    idx = skill.index(skill_trees[i][j])
                else:
                    break

            if j == len(skill_trees[i]) - 1:
                answer += 1

    return answer