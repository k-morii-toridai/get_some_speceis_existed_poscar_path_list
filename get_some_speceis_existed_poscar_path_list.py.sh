#!/bin/bash

#POSCARファイルが存在するパスの一覧を取得（：第2引数を環境ごとのcif/ディレクトリのパスに書き換える）
python3 get_poscar_existed_path_list.py /mnt/ssd_elecom_black_c2c_480G/cif
###### 取得したい元素種を，半角英字の大文字でコマンドライン引数として入力 ######

#元素種C, Oを含むPOSCARファイルが存在するパスを取得
python3 get_some_speceis_existed_poscar_path_list.py C O

#元素種N, H
# python3 get_some_speceis_existed_poscar_path_list.py N H

# 元素種Me,N
# python3 get_some_speceis_existed_poscar_path_list.py Me N
