description = ""
discount_codes = []

while True:
    print("\nHỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
    print("5. Thoát chương trình")

    choice = input("Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    if choice == "1":

        shop = input("Nhập tên shop: ")

        if shop.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        product = input("Nhập tên sản phẩm: ")

        description = input("Nhập mô tả sản phẩm: ")

        if description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        category = input("Nhập danh mục sản phẩm: ")
        keywords = input("Nhập từ khóa (cách nhau bởi dấu phẩy): ")

        print("\n===== BÁO CÁO =====")
        print("Tên shop:", shop.strip())
        print("Tên sản phẩm:", product.strip().title())
        print("Mô tả:", description.strip())
        print("Độ dài mô tả:", len(description.strip()))
        print("Danh mục:", category.strip().lower())

        keyword_list = keywords.split(",")

        print("Danh sách từ khóa:")
        for item in keyword_list:
            print(item.strip())

        print("Số lượng từ khóa:", len(keyword_list))
        print("Mô tả chữ thường:", description.lower())
        print("Mô tả chữ hoa:", description.upper())

    elif choice == "2":

        shop = input("Nhập tên shop: ")

        if shop.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        print("Tên shop ban đầu:", shop)

        shop = shop.strip().lower()
        shop = "-".join(shop.split())

        if not shop.startswith("shop-"):
            shop = "shop-" + shop

        print("Tên shop sau chuẩn hóa:", shop)

    elif choice == "3":

        code = input("Nhập mã giảm giá: ")

        if code == "":
            print("Mã giảm giá không được rỗng")

        elif " " in code:
            print("Mã giảm giá không được chứa khoảng trắng")

        elif len(code) < 6 or len(code) > 12:
            print("Mã giảm giá phải từ 6 đến 12 ký tự")

        elif code != code.upper():
            print("Mã giảm giá phải viết hoa toàn bộ")

        elif not code.isalnum():
            print("Mã giảm giá chỉ chứa chữ và số")

        elif not code.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")

        else:
            print("Mã giảm giá hợp lệ")
            discount_codes.append(code)

            print("Danh sách mã giảm giá:")
            for item in discount_codes:
                print(item)

    elif choice == "4":

        if description.strip() == "":
            print("Chưa có mô tả sản phẩm")
            continue

        find_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")

        count = description.count(find_word)

        if count == 0:
            print("Không tìm thấy từ khóa")
        else:
            description = description.replace(find_word, replace_word)

            print("Số lần xuất hiện:", count)
            print("Mô tả sau khi thay thế:")
            print(description)

    elif choice == "5":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")