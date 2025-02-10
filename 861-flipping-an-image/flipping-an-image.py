class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n):
                sp = n - j -1
                if j < sp:
                    image[i][j],image[i][sp] = image[i][sp],image[i][j]
                else:
                    break
        for i in range(n):
            for j in range(n):
                if image[i][j] == 0:
                        image[i][j] = 1
                else:
                    image[i][j] = 0

        return image

        
        