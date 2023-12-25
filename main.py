import os
import shutil
import configparser


settings = configparser.ConfigParser()
settings.read('config.ini', "utf8")


source_folder = settings.get('source_folder','source_folder')
destination_root = settings.get('destination_root','destination_root')
other_folder = settings.get('other_folder','other_folder')

templates = {i.title():settings['templates'][i] for i in settings['templates']}





# Цикл по всем файлам в исходной папке
for filename in os.listdir(source_folder):
    # Получаем полный путь к файлу
    source_file = os.path.join(source_folder, filename)
    print(source_file)
    # Получаем префикс имени файла
    prefix = filename[:3] + "_"


    # Если это файл
    if os.path.isfile(source_file):
        # Проверяем, соответствует ли имя файла шаблону
        if prefix in templates:
            # Если да, вырезаем файл из исходной папки
            destination_folder = os.path.join(destination_root, templates[prefix])


            # Получаем полный путь к файлу в целевой папке
            destination_file = os.path.join(destination_folder, filename)

            # Вырезаем файл из исходной папки
            shutil.move(source_file, destination_file)
            print(f"Вырезан файл '{filename}' из папки '{source_folder}' и вставлен в папку '{destination_folder}'")
        else:
            # Если нет, копируем файл в папку для нераспределенных файлов
            destination_folder = other_folder

            # Вырезаем файл из исходной папки
            shutil.move(source_file, other_folder)
            print(f"Перемещен файл '{filename}' в '{other_folder}'")

    # Если это папка
    else:
        # Получаем имя папки
        folder_name = os.path.basename( filename)
        # Копируем папку в целевую папку по шаблону
        destination_folder = os.path.join(destination_root, templates[prefix])

        # Получаем полный путь к папке в целевой папке
        destination_file = os.path.join(destination_folder, os.path.basename(folder_name))

        # Вырезаем папку из исходной папки
        shutil.move(source_file, destination_file)
        print(f"Вырезана папка '{source_folder}' в папку '{destination_folder}'")




