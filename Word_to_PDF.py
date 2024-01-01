import os

from docx2pdf import convert


def file_convert_docx_pdf(dirs):
    file_in_dir = os.listdir(dirs)

    if not os.path.isdir(f'{dirs}\\convert_pdf'):
        os.mkdir(f'{dirs}\\convert_pdf')

    for file in file_in_dir:
        if file.endswith('.docx'):
            file_k = f'{file.split(".")[0].replace(".", "_")}.pdf'
            convert(f'{dirs}\\{file}', f'{dirs}\\convert_pdf\\{file_k}')
        else:
            continue

print ('Alfa: P4V_v061223')
print ('Программа переводит все файлы формата .docx в файлы формата PDF и сохраняет их в отдельную папку')
print ('Автоматизируем процессы! https://ispolnitelnaya.online')
def main():
    dirs = input('\nВведите путь к папке с файлами: ')
    file_convert_docx_pdf(dirs)
    print(f'\n[+] - Конвертация завершена.\n ')


if __name__ == "__main__":
    main()