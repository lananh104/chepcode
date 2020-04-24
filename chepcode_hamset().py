#khai báo list a
a=[10,20,30,40,50,60,20,30]
#khởi tạo hàm set()
dup_items=set()
#khai báo list rỗng
uniq_items=[]
#vòng lặp for với biến x chạy trong list a
for x in a:
   #giá trị của x chỉ được truyền vào hàm set() một lần thì các câu lệnh trong if được thực hiện
    if x not in dup_items:
        #thêm một giá trị của x vào cuối list uniq_items
        uniq_items.append(x)
        #thêm một giá trị của x vào hàm set()
        dup_items.add(x)
print(uniq_items)
print(dup_items)
