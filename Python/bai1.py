i = int(input("Nhập vào bảng cửu chương muốn hiển thị [1-10]}:"))
while i > 10 or i < 1:
    i = int(input("Nhập sai, Vui lòng nhập lại số từ 1-10:"))
    if 0 < i <= 10:
        break
for j in range(0,10):
    j = j + 1
    print(i ,"*", j, "=",i*j)