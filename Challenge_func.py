from HW_Task_1_8 import dir_info as di
from HW_Task_1_8 import save_to_json as stj
from HW_Task_1_8 import save_to_csv as stcsv
from HW_Task_1_8 import save_to_picle as stp

JSON_FILENAME = "info.json"
CSV_FILENAME = "info.csv"
PICK_FILENAME = "info.pcl"

if __name__ == '__main__':
    print("Информация о каталоге: ")
    dir_info = di()  # сканируем текущий каталог
    print(dir_info)
    # Сохраняем в различные форматы
    print("Сохранение информации в файлы")
    stj(dir_info, JSON_FILENAME)
    stp(dir_info, PICK_FILENAME)
    stcsv(dir_info, CSV_FILENAME)

    print(f"Информация в файлах: {JSON_FILENAME}, {CSV_FILENAME}, {PICK_FILENAME}")
