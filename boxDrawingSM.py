# Declare box drawing characters
a = '\u250c' # Top left corner
b = '\u2500' # Horizontal bar
c = '\u2510' # Top right corner
d = '\u2514' # Bottom left corner
e = '\u2518' # Bottom right corner
f = '\u2502' # Vertical bar

def boxDrawing(weight, height):
    if weight == 1 or height == 1:
        print('Invalid values: Weight and Height need to be larger than 1')
    else:
        # Build first row
        A = [a]
        for i in range(0,W-2):
            A.append(b)
        A.append(c)

        # Build middle rows
        for h in range(0,H-2):
            A.append(f)
            for w in range(0,W-2):
                A.append(' ')
            A.append(f)
    
        # Build last row 
        A.append(d)
        for i in range(0,W-2):
            A.append(b)
        A.append(e)
    
        # Print
        for i in range(0,H):
            print(*A[W*i:W*i+W])

# Test function for various W and H

W = 1
H = 1
print('Weight = ', W, ', Height = ',H, ':')
boxDrawing(W,H)

W = 4
H = 2
print('Weight = ', W, ', Height = ',H, ':')
boxDrawing(W,H)

W = 9
H = 9
print('Weight = ', W, ', Height = ',H, ':')
boxDrawing(W,H)

W = 25
H = 25
print('Weight = ', W, ', Height = ',H, ':')
boxDrawing(W,H)