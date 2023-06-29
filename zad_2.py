matrix=[[4,9,7,2],[30,0,1,4],[4,67,2,3]]
for i in matrix: # цикл по элементам внешнего списка
    print()
    for j in i:
        print (j, end=" ")
print()
n = len(matrix)
m = len(matrix[0])
column_products = []
for j in range(m):
    product = 1
    for i in range(n):
        product *= matrix[i][j]
    column_products.append(product)
column_indices = sorted(range(4), key=lambda j: column_products[j])
new_matrix = [[matrix[i][j] for j in column_indices] for i in range(n)]
for i in new_matrix:
    print()
    for j in i:
        print (j, end=" ")