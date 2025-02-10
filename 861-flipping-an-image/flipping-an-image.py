class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n):
                sp = n - j -1
                if j < sp:
                    image[i][j],image[i][sp] = image[i][sp],image[i][j]
                    if image[i][j] == 0:
                        image[i][j] = 1
                    else:
                        image[i][j] = 0

                    if image[i][sp] == 0:
                        image[i][sp] = 1
                    else:
                        image[i][sp] = 0
                elif j == sp:
                    if image[i][j] == 0:
                        image[i][j] = 1
                    else:
                        image[i][j] = 0

                else:
                    break
        return image

        
        