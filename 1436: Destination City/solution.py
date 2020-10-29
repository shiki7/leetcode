class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            flg = True
            for j in range(len(paths)):
                if paths[i][1] == paths[j][0]:
                    flg = False
                    break
            if flg:
                return paths[i][1]
