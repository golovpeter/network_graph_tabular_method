import csv

from models import Row


def parse_file(file_name: str) -> (list[Row], int):
    table: list[Row] = []

    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if len(row) != 3:
                return -1

            try:
                int(row[0])
                int(row[1])
                int(row[2])
            except ValueError:
                return -1

            new_row = Row(
                int(row[0]),
                int(row[1]),
                int(row[2]),
            )

            table.append(new_row)

    return table


def calculate_early_start_and_early_end(table: list[Row]):
    for i in range(len(table)):
        if table[i].first_work == 1:
            table[i].early_end = table[i].time_work
            continue

        early_end_prev: list[int] = []

        for j in range(i + 1):
            if table[j].second_work == table[i].first_work:
                early_end_prev.append(table[j].early_end)

        table[i].early_start = max(early_end_prev)
        table[i].early_end = table[i].time_work + table[i].early_start


def calculate_later_start_and_later_end(table: list[Row]):
    last_work: int = table[len(table) - 1].second_work

    for i in range(len(table) - 1, -1, -1):
        if table[i].second_work == last_work:
            table[i].later_end = table[len(table) - 1].early_end
            table[i].later_start = table[i].later_end - table[i].time_work
            continue

        later_end_prev: list[int] = []

        for j in range(len(table) - 1, -1, -1):
            if table[j].first_work == table[i].second_work:
                later_end_prev.append(table[j].later_start)

        table[i].later_end = min(later_end_prev)
        table[i].later_start = table[i].later_end - table[i].time_work


def calculate_general_reserve(table: list[Row]):
    for i in range(len(table)):
        if table[i].time_work == 0:
            table[i].general_reserve = '-'
            continue

        table[i].general_reserve = table[i].later_end - table[i].early_end


def calculate_local_reserve(table: list[Row]):
    last_work: int = table[len(table) - 1].second_work

    for i in range(len(table)):
        if table[i].general_reserve == '-':
            table[i].local_reserve = table[i].general_reserve
            continue

        if table[i].second_work == last_work:
            table[i].local_reserve = table[i].general_reserve
            continue

        early_start_end: list[int] = []

        for j in range(len(table)):
            if table[j].first_work == table[i].second_work:
                early_start_end.append(table[j].early_start)

        table[i].local_reserve = max(early_start_end) - table[i].early_end


def main():
    table = parse_file("data.csv")

    if table == -1:
        print("Failed to parse file")
        return

    calculate_early_start_and_early_end(table)
    calculate_later_start_and_later_end(table)
    calculate_general_reserve(table)
    calculate_local_reserve(table)

    for row in table:
        row.show_row()


if __name__ == '__main__':
    main()
