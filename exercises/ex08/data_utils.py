"""Hi."""
from csv import DictReader
__author__ = "730558424"



def read_csv_rows(x_list: str) -> list[dict[str, str]]:
    """Hi."""
    result: list[dict[str, str]] = list()
    file_handle = open(x_list, "r", encoding="utf8")
    csv_reader = DictReader(x_list)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str)  -> list[str]:
    """Hi."""
    result: list[str] = []

    for row in table:
        result.append(row[header])


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)

    return result

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Hi."""
    result: dict[str, list[str]] = {}
    x = 0
    for key in table: 
        if(x < rows):
            result.append(table[key])
            x+=1

def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
