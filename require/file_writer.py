def write_to_sct(output_path, data, encoding='gbk'):
    with open(output_path, 'w', encoding=encoding) as sct_file:
        for line in data:
            sct_file.write(line + '\n')
