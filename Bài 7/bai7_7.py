def count_lines_in_file(fname):
    with open(fname, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        return num_lines
file_name = 'bao.txt' 
line_count = count_lines_in_file(file_name)
print(f"Số dòng trong tệp '{file_name}' là: {line_count}")
print("sinh vien: Đậu Văn Quốc Bảo")
print("Mssv: 235752020710014")