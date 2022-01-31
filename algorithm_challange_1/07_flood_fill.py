class Solution:
	def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:

		def flood_fill_dfs(img,sr,sc,newColor,oldValue):
			nonlocal visited
			nonlocal n
			nonlocal m

			img[sr][sc] = newColor
			cords = [(sr-1,sc),(sr+1,sc),(sr,sc-1),(sr,sc+1)]

			new_cords = [(a,b) for (a,b) in cords if a>=0 and b>=0 and a<n and b<m]

			for x,y in new_cords:
				if (x,y) not in visited and oldValue == image[x][y]:
					visited.append((x,y))
					flood_fill_dfs(img,x,y,newColor,oldValue)

		visited = list()
		n,m = len(image),len(image[0])

		flood_fill_dfs(image,sr,sc,newColor,image[sr][sc])

		return image


print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
