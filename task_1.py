import csv

INPUT_FILE = "source__300 (задача 1).csv"
RESULT_FILE = "task1_result.csv"
NUMBER_OF_ROWS = 300
NUMBER_OF_COLUMNS = 300


def get_data(filename: str):
    with open(filename, 'r') as f_in:
        f_reader = csv.reader(f_in, delimiter="|")
        for row in f_reader:
            yield row


def make_matrix(filename: str, number_rows: int, number_columns: int) -> dict:
    try:
        matrix = [[0 for _ in range(number_columns)] for _ in range(number_rows)]
        for el in get_data(filename):
            ind = int(el[0]) - 1
            val = int(el[1])
            n_row = ind // number_rows
            n_col = ind % number_columns
            matrix[n_row][n_col] = val

        with open(RESULT_FILE, 'w') as f_out:
            f_writer = csv.writer(f_out)
            for row in matrix:
                f_writer.writerow(row)

        return RESULT_FILE, 200
    
    except Exception:
        return "Something went wrong", 400


if __name__ == "__main__":
    result, status = make_matrix(
        filename=INPUT_FILE,
        number_rows = NUMBER_OF_ROWS,
        number_columns = NUMBER_OF_COLUMNS
    )
    if status == 200:
        print(f'All done, file: {result}')
    else:
        print(result)