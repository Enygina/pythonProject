from collections import namedtuple
from pathlib import Path
import logging
import argparse
import os
from os import walk

logging.basicConfig(filename='task_06.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extention, is_dir, parent_dir')


def pars():
    parser = argparse.ArgumentParser(prog='Задача №6 семинара 15',
                                     epilog='name - имя файла без расширения или название каталога | '
                                            'ext - расширение, если это файл | '
                                            'is_folder - флаг каталога | '
                                            'parent_folder - название родительского каталога',
                                     description='Данный модуль осуществляет запись информации '
                                                 'о содержимом каталога в файл hw1.log')

    parser.add_argument('-p', '--path', default=os.curdir, help='путь до директории на ПК')
    arg = parser.parse_args()
    return arg.path


def read_dir(path: Path) -> None:
    files_list = walk(path)
    for catalog in files_list:
        objects_path, folders, files = catalog
        if len(folders) != 0:
            for folder in folders:
                obj = File(folder, '', True, objects_path.split('\\')[-1])
                logger.info(obj)
        if len(files) != 0:
            for f in files:
                f_name, f_ext = f.split('.')
                obj = File(f_name, f_ext, False, objects_path.split('\\')[-1])
                logger.info(obj)
    print(f'> Информация о каталоге успешно записана в файл "task_06.log"')


if __name__ == '__main__':
    print(read_dir(pars()))
