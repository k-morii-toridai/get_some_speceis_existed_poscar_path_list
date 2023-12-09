import os
import sys
from pathlib import Path
from multiprocessing import Pool, cpu_count


import numpy as np
from tqdm import tqdm

# poscar_abs_path_listをload
poscar_abs_path_list_loaded = np.load('poscar_existed_file_path_list.npy', allow_pickle=True)
print(f"len(poscar_abs_path_list_loaded): {len(poscar_abs_path_list_loaded)}")

# 抽出したい元素種をコマンドラインから受け取る
args = sys.argv


def return_some_species_exist(poscar_path, species=args[1:]):
    def get_species_from_poscar(poscar_path):
        # POSCARファイルから元素種の行から元素種を取り出す
        with open(poscar_path, mode='r') as f:
            poscar_line_list = f.readlines()
            # poscarからspeciesをリストで取得
            species_list = set(poscar_line_list[5][:-1].split(' '))
            species_list.discard('')
            return species_list

    # return set(['C', 'O']) <= set(get_species_from_poscar(poscar_path))
    return set(species) <= set(get_species_from_poscar(poscar_path))


# return_some_species_exist()を並列化して実行
p = Pool(cpu_count() - 1)
bool_some_species_exist_list = list(tqdm(p.imap(return_some_species_exist, poscar_abs_path_list_loaded), total=len(poscar_abs_path_list_loaded)))
p.close()
p.join()

# CとOを含むPOSCARファイルを抽出し，そのリストを.npy形式で保存
some_species_existed_poscar_file_path_list = poscar_abs_path_list_loaded[bool_some_species_exist_list]
file_head_str = '_'.join(args[1:])
print(f"len({file_head_str}_existed_poscar_file_path_list): {len(some_species_existed_poscar_file_path_list)}")
np.save(f'{file_head_str}_existed_poscar_file_path_list.npy', some_species_existed_poscar_file_path_list)
# CとOを含むPOSCARファイルのフォルダのリストを.npy形式で保存
some_species_existed_poscar_folder_path_list = [Path(os.path.split(p)[0]) for p in some_species_existed_poscar_file_path_list]
np.save(f'{file_head_str}_existed_poscar_folder_path_list.npy', some_species_existed_poscar_folder_path_list)
print(f"{file_head_str}_existed-poscar file, and folder path list were saved as .npy!!!")
