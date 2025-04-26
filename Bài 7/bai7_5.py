def file_append_and_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("2 nguyenducdat\n")
        myfile.write("19032005\n")
    with open(fname, "r") as txt:
        print(txt.read())
file_append_and_read('baodeptai.txt')
print("sinh vien: Đậu Văn Quốc Bảo")
print("Mssv: 235752020710014")