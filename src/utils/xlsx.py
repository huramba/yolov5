import openpyxl as px


def to_xlsx(stats: list, filename: str):
    wb = px.Workbook()
    ws = wb.create_sheet('Статистика')
    del wb['Sheet']

    for stat in stats:
        ws.append(stat)

    wb.save(filename)