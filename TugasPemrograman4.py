def matrix_chain(lst_matrix, dp, dp_string):
    for i in range(len(lst_matrix)):
        for j in range(i, len(lst_matrix)):
            temp_lst = lst_matrix[j - i:j + 1]
            result = float('inf')
            string_result = ""
            if i != 0:
                for k in range(len(temp_lst) - 1):
                    temp_result = (dp[j - i][j - i + k] + dp[j - i + k + 1][j] +
                                   lst_matrix[j - i][0] * lst_matrix[j - i + k][1] * lst_matrix[j][1])
                    temp_string = "(" + dp_string[j - i][j - i + k] + " " + dp_string[j - i + k + 1][j] + ")"
                    if result > temp_result:
                        result = temp_result
                        string_result = temp_string
                dp_string[j - i][j] = string_result
            else:
                result = 0
                dp_string[j - i][j] = f"A{j - i + 1}"
            dp[j - i][j] = result

def main():
    while True:
        try:
            input_matrix = input("Masukkan vektor ukuran matriks atau ketik EXIT): ")
            if input_matrix == "EXIT":
                break
            matrix_sizes = list(map(int, input_matrix.replace('<', '').replace('>', '').split(',')))

            n = len(matrix_sizes) - 1
            dp = [[0] * n for _ in range(n)]
            split_table = [[''] * n for _ in range(n)]

            for chain_length in range(2, n + 1):
                for i in range(n - chain_length + 1):
                    j = i + chain_length - 1
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        cost = dp[i][k] + dp[k+1][j] + matrix_sizes[i] * matrix_sizes[k+1] * matrix_sizes[j+1]
                        if cost < dp[i][j]:
                            dp[i][j] = cost
                            split_table[i][j] = k

            def print_parenthesis(s, i, j):
                if i == j:
                    print(f"A{i+1}", end="")
                else:
                    print("(", end="")
                    print_parenthesis(s, i, s[i][j])
                    print_parenthesis(s, s[i][j] + 1, j)
                    print(")", end="")

            print(dp[0][n - 1])
            print_parenthesis(split_table, 0, n - 1)
            print("\nTabel m")
            for row in dp:
                print(" ".join(str(x) for x in row))
            print("Tabel s")
            for row in split_table:
                print(" ".join(str(x+1) if x != '' else '-' for x in row))
        except ValueError:
            print("Input tidak valid. Mohon masukkan vektor ukuran matriks dalam format yang benar.")

if __name__ == "__main__":
    main()
