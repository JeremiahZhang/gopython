"""
The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda’s space station, 
and as a result the prison blocks have an unusual layout. 
They are stacked in a triangular shape, and the bunny prisoners 
are given numerical IDs starting from the corner, as follows:

| 7

| 4 8

| 2 5 9

| 1 3 6 10 

Each cell can be represented as points (x, y), 
with x being the distance from the vertical wall, 
and y being the height from the ground.

For example, the bunny prisoner at (1, 1) has ID 1, 
the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. 
This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

(5, 10) has ID 96


 4  5:(y+1)   6  7   8(x+y-1)
 | 7      12  18 25   33
 3  4:(y+1)  5   6   7(x+y-1) 
 | 4      8   13 19   26
 2  3:(y+1)  4   5   6(x+y-1)
 | 2      5   9  14   20
 1  2:(y+1)  3   4   5(x+y-1)    
 | 1      3   6  10   15   
                     x=5

solution:
line1(y=1)
	x=1: 3 - 1 = 2 == diff_x = diff_1 = (x+1); 
	x=2: 6 - 3 = 3 == diff_x = diff_2 = (x+1);
	x=3: 10 - 6= 4 == diff_x = diff_3 = (x+1); 
	x=4: diff_x = (x+1) = 5, (4, 1) has ID (3,1)+diff_x = 10+5 = 15
	x = n : diff_x = (n+1), (n, 1) has ID (n-1,1)+diff_n = (1,1) + sum(diff_1 + ... diff_n) 

line x column y:
	diff_x_y = x + y - 1
	diff_1_y = y

column 1(x=1)
	ID(1,y): (1, y) has ID : 1 + y(y-1)/2

(x, y) has ID:
    ID(1,y) + Sum(diff_2_y + ... diff_x_y) (x > 1, y > 1)
    ==
    (1 + y(y-1)/2) + [(y+1)+(x+y-1)](x-1)/2
"""

def solution(x, y):
	diff = y - 1
	diff_2_y = y + 1
	diff_x_y = x + diff
	result = (1 + y * diff / 2) + (diff_2_y + (diff_x_y)) * (x - 1) / 2

	return int(result)

def main():
	x = int(input('enter x:>'))
	y = int(input('enter y:>'))
	print(solution(x, y))


if __name__ == '__main__':
	main()
