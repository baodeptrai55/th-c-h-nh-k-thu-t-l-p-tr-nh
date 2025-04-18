class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.chieu_dai = dai
        self.chieu_rong = rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

hcn = Hinhchunhat(5, 3)

print(hcn.dien_tich())
print("sinh vien: Đậu Văn Quốc Bảo")
print("Mssv: 235752020710014")