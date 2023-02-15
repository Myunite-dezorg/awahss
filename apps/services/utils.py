import xlwt
from django.http import HttpResponse


def render_to_xls(data, filename):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')

    row_num = 0
    columns = []
    for item in data:
        row = []
        for key in item:
            if key not in columns:
                columns.append(key)
            row.append(item[key])
        row_num += 1
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, cell_value)

    for col_num, column_title in enumerate(columns):
        ws.write(0, col_num, column_title)

    wb.save(response)
    return response
