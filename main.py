import argparse
import os
import pandas as pd
from require.csv_reader import read_csv
from require.file_writer import write_to_sct

def validate_and_format_coordinate(value, is_latitude=True):
    try:
        value = value.strip()
        if not value:
            return "N00.00.00.000" if is_latitude else "E000.00.00.000"

        parts = value.split(',')
        if len(parts) != 2:
            return "N00.00.00.000" if is_latitude else "E000.00.00.000"

        degree = int(parts[0][1:])
        minute = int(parts[1][:2])
        second = float(parts[1][2:].replace(',', '.'))

        if is_latitude:
            if not (-90 <= degree <= 90):
                return "N00.00.00.000"
            return f"N{degree:02d}.{minute:02d}.{second:02.0f}.000"
        else:
            if not (-180 <= degree <= 180):
                return "E000.00.00.000"
            return f"E{degree:03d}.{minute:02d}.{second:02.0f}.000"
    except ValueError:
        return "N00.00.00.000" if is_latitude else "E000.00.00.000"

def generate_vor_sct(vor_data, output_file):
    sct_lines = ['[VOR]']
    for index, row in vor_data.iterrows():
        code_id = row['CODE_ID']
        txt_name = row['TXT_NAME']
        val_freq = row['VAL_FREQ']
        geo_lat = row.get('GEO_LAT_ACCURACY', '0')
        geo_long = row.get('GEO_LONG_ACCURACY', '0')

        formatted_lat = validate_and_format_coordinate(geo_lat, is_latitude=True)
        formatted_long = validate_and_format_coordinate(geo_long, is_latitude=False)

        line1 = f"{code_id} {val_freq} {formatted_lat} {formatted_long}"
        line2 = f"{code_id}/{txt_name} {val_freq} {formatted_lat} {formatted_long}"

        sct_lines.append(line1)
        sct_lines.append(line2)
    write_to_sct(output_file, sct_lines, encoding='gbk')

def generate_ndb_sct(ndb_data, output_file):
    sct_lines = ['[NDB]']
    for index, row in ndb_data.iterrows():
        code_id = row['CODE_ID']
        txt_name = row['TXT_NAME']
        val_freq = row['VAL_FREQ']
        geo_lat = row.get('GEO_LAT_ACCURACY', '0')
        geo_long = row.get('GEO_LONG_ACCURACY', '0')

        formatted_lat = validate_and_format_coordinate(geo_lat, is_latitude=True)
        formatted_long = validate_and_format_coordinate(geo_long, is_latitude=False)

        line1 = f"{code_id} {val_freq} {formatted_lat} {formatted_long}"
        line2 = f"{code_id}/{txt_name} {val_freq} {formatted_lat} {formatted_long}"

        sct_lines.append(line1)
        sct_lines.append(line2)
    write_to_sct(output_file, sct_lines, encoding='gbk')

def generate_sct_by_fir(data, output_dir, file_type):
    grouped_data = data.groupby('CODE_FIR')

    for fir, group in grouped_data:
        output_file = os.path.join(output_dir, f"{fir}_{file_type}.sct")
        if file_type == 'VOR':
            generate_vor_sct(group, output_file)
        elif file_type == 'NDB':
            generate_ndb_sct(group, output_file)

def main():
    parser = argparse.ArgumentParser(description='Generate VOR and NDB SCT files.')
    parser.add_argument(
        '--mode', choices=['area', 'all'], required=True,
        help='运行模式：通过情报区生成 (area) 或全部生成 (all)'
    )
    args = parser.parse_args()

    input_vor_file = os.path.join('Datafiles', 'VOR.csv')
    input_ndb_file = os.path.join('Datafiles', 'NDB.csv')

    # 确保生成目录存在
    os.makedirs('generate', exist_ok=True)

    if args.mode == 'all':
        output_file_vor = os.path.join('generate', 'VOR.sct')
        output_file_ndb = os.path.join('generate', 'NDB.sct')

        # 读取VOR和NDB文件
        vor_data = read_csv(input_vor_file)
        ndb_data = read_csv(input_ndb_file)

        # 生成SCT文件
        generate_vor_sct(vor_data, output_file_vor)
        generate_ndb_sct(ndb_data, output_file_ndb)

        print(f"VOR.sct 文件和 NDB.sct 文件已成功生成到 'generate' 目录")

    elif args.mode == 'area':
        # 读取VOR和NDB文件
        vor_data = read_csv(input_vor_file)
        ndb_data = read_csv(input_ndb_file)

        # 生成按情报区分类的S文件
        generate_sct_by_fir(vor_data, 'generate', 'VOR')
        generate_sct_by_fir(ndb_data, 'generate', 'NDB')

        print("按情报区生成的VOR和NDB SCT文件已成功生成到 'generate' 目录")

if __name__ == '__main__':
    main()
