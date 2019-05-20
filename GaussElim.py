def read_file():
    matrix = []
    with open("matrix.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            matrix.append([float(x) for x in line.split(",")])
        print(matrix)
        return matrix

#This function takes in a list of lists (matrix) and the solution list, and performs Gaussian elimination by comparing, swapping rows,
# and 
def gaussElimination(matrix, sol):
        
        M = matrix
        n = len(M)
        
        i = 0
        for y in M:
            y.append(sol[i])
            i += 1
            
        #swap rows if the lower row is farther from zero
        for k in range(n):
            for i in range(k,n):
                if abs(M[i][k]) > abs(M[k][k]):
                    M[k], M[i] = M[i], M[k]  
                else:
                    pass
            for row in M:
                print row
            print
        
            for j in range(k+1,n):
                quotient = float(M[j][k]) / M[k][k]
                for m in range(k, n+1):
                    temp = quotient * M[k][m] #divide row 
                    M[j][m] -=  temp
                
            for row in M:
                print row
            print
    
        x = [0 for i in range(n)]
            
        try:
            x[n-1] =float(M[n-1][n])/M[n-1][n-1]    #Test for dividing by zero
            
        except ZeroDivisionError:
            print "System did not produce a unique solution."
            return None
            
        for row in M:
            print row
        print
        
        #Solve by back-substitution
        for i in range (n-1,-1,-1):
            z = 0
            for j in range(i+1,n):
                z += float(M[i][j]) * x[j]
                x[i] = float(M[i][n] - z) / M[i][i]
            
        for i in range (len(x)):
            print "x", i," = ", x[i]
        
if __name__ == '__main__':
    
    s = [9, 54, 122, -44]
    matrix = read_file()
    gaussElimination(matrix, s)
        
                