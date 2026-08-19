import pymysql

current_user_id = None

def show_menu():
    print("\n=== 校园二手市场 ===")
    print("1. 注册")
    print("2. 登录")
    print("3. 发布商品")
    print("4. 下单")
    print("5. 查看我的订单")
    print("0. 退出")
    print("======================")

def main():
    while True:
        show_menu()
        choice = input("请先选择功能(0-5):")
        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            if current_user_id is None:
                print("请先登录！")
            else:
                publish_product()

        elif choice == "4":
            if current_user_id is None:
                print("请先登录！")
            else:
                place_order()

        elif choice == "5":
            if current_user_id is None:
                print("请先登录！")
            else:
                view_orders()

        elif choice == "0":
            print("再见！")
            break

        else:
            print("请重新输入")

def register():
    print("\n--- 用户注册 ---")
    username = input("用户名：")
    password = input("密码：")
    email = input("邮箱：")
    phone = input("手机号：")

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Campus123!",
        database="campus_flea_market",
        charset="utf8mb4"
    )

    cursor = conn.cursor()
    sql = "INSERT INTO users (username,password,email,phone) VALUES (%s, %s, %s, %s);"
    data = (username, password, email, phone)
    try:
        cursor.execute(sql, data)
        conn.commit()
        print(f"注册成功！影响了 {cursor.rowcount} 行")
    except pymysql.err.IntegrityError:
        print("注册失败：用户名已存在")
    except Exception as e:
        print(f"注册失败：{e}")
    finally:
        cursor.close()
        conn.close()

def login():
    global current_user_id
    print("\n--- 用户登录 ---")
    username = input("用户名：")
    password = input("密码：")
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Campus123!",
        database="campus_flea_market",
        charset="utf8mb4"
    )

    cursor = conn.cursor()
    sql = "SELECT user_id, password FROM users WHERE username = %s;"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result is None:
        print("用户名不存在")
        return
    if password != result[1]:
        print("密码错误")
        return
    current_user_id = result[0]
    print(f"登录成功 用户ID：{current_user_id}")

def publish_product():
    global current_user_id
    print("\n--- 发布商品 ---")
    title = input("商品标题：")
    description = input("商品描述：")
    price = input("价格：")
    category = input("分类：")

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Campus123!",
        database="campus_flea_market",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = "INSERT INTO products (seller_id, title, description, price, category) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(sql, (current_user_id, title, description, price, category))
    conn.commit()

    print(f"发布成功 影响了 {cursor.rowcount} 行")
    cursor.close()
    conn.close()

def place_order():
    global current_user_id
    print("\n--- 下单 ---")
    product_id = input("请输入要购买的商品ID：")
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Campus123!",
        database="campus_flea_market",
        charset="utf8mb4"
    )
    cursor = conn.cursor()

    sql_product = "SELECT seller_id, price, status, title FROM products WHERE product_id = %s;"
    cursor.execute(sql_product, (product_id,))
    product = cursor.fetchone()

    if product is None:
        print("商品不存在")
        cursor.close()
        conn.close()
        return
    seller_id, price, status, title = product

    if status != 1:
        print("该商品已下架，无法购买")
        cursor.close()
        conn.close()
        return
    print(f"商品：{title}，价格：{price}元")

    quantity = int(input("数量："))
    total_price = float(price) * quantity
    sql_order = """
        INSERT INTO orders (buyer_id, product_id, seller_id, quantity, total_price)
        VALUES (%s, %s, %s, %s, %s);
    """

    cursor.execute(sql_order, (current_user_id, product_id, seller_id, quantity, total_price))
    conn.commit()
    print(f"下单成功 金额：{total_price}元")
    cursor.close()
    conn.close()

def view_orders():
    global current_user_id
    print("\n--- 我的订单 ---")
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Campus123!",
        database="campus_flea_market",
        charset="utf8mb4"
    )
    cursor = conn.cursor()
    sql = """
        SELECT
            o.order_id,
            p.title AS 商品名称,
            u.username AS 卖家,
            o.quantity AS 数量,
            o.total_price AS 总价,
            o.created_at AS 下单时间
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        JOIN users u ON o.seller_id = u.user_id
        WHERE o.buyer_id = %s
        ORDER BY o.created_at DESC;
    """
    cursor.execute(sql, (current_user_id,))
    orders = cursor.fetchall()

    if len(orders) == 0:
        print("你还没有订单")
    else:
        for row in orders:
            print(f"订单号：{row[0]} | 商品：{row[1]} | 卖家：{row[2]} | "
                  f"数量：{row[3]} | 总价：{row[4]} | 时间：{row[5]}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
