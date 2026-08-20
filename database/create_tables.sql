CREATE DATABASE IF NOT EXISTS campus_flea_market 
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE campus_flea_market;
UPDATE campus_flea_market.users SET password = '123456' WHERE user_id > 0;
SELECT * FROM users;

-- 用户表 users
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 商品表
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    seller_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    category VARCHAR(50),
    status TINYINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 订单表
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_id INT NOT NULL,
    product_id INT NOT NULL,
    seller_id INT NOT NULL,
    quantity INT DEFAULT 1,
    total_price DECIMAL(10,2),
    status TINYINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 评价表 reviews
CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    rating TINYINT NOT NULL,
    content TEXT,
    status TINYINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- users表测试数据
INSERT INTO users (username, email, phone, password) VALUES
('zhangsan', 'zs@school.edu', '13800138001','123456'),
('lisi', 'ls@school.edu', '13800138002','123456'),
('wangwu', 'ww@school.edu', '13800138003','123456'),
('zhaoliu', 'zl@school.edu', '13800138004','123456'),
('qianqi', 'qq@school.edu', '13800138005','123456'),
('sunba', 'sb@school.edu', '13800138006','123456'),
('zhoujiu', 'zj@school.edu', '13800138007','123456'),
('wushi', 'ws@school.edu', '13800138008','123456'),
('zhengshi', 'zs2@school.edu', '13800138009','123456'),
('dongfang', 'df@school.edu', '13800138010','123456'),
('ximen', 'xm@school.edu', '13800138011','123456'),
('nangong', 'ng@school.edu', '13800138012','123456'),
('beigong', 'bg@school.edu', '13800138013','123456'),
('guiguzi', 'ggz@school.edu', '13800138014','123456'),
('mozi', 'mz@school.edu', '13800138015','123456');

-- products表测试数据
INSERT INTO products (seller_id, title, description, price, category) VALUES
(1, '高等数学上册', '九成新，少量笔记', 25.00, '教材'),
(2, 'iPhone 13', '电池健康85%，无拆修', 2200.00, '手机'),
(3, '护眼台灯', '三档调光，宿舍必备', 18.00, '电器'),
(4, '联想笔记本', 'i5处理器，8G内存', 2200.00, '电脑'),
(5, 'C++ Primer', '经典教材，几乎全新', 45.00, '教材'),
(6, '蓝牙耳机', '降噪功能完好', 80.00, '数码'),
(7, '吉他', '入门款，送琴包', 150.00, '乐器'),
(8, '篮球', '斯伯丁正品', 60.00, '体育'),
(9, '英语四级真题', '2024版，做过两套', 10.00, '教材'),
(10, '小米充电宝', '20000毫安', 35.00, '数码'),
(11, '折叠桌', '床上用，稳固', 20.00, '家具'),
(12, '尤克里里', '23寸，音色准', 120.00, '乐器'),
(13, '路由器', 'TP-LINK，千兆', 50.00, '电器'),
(14, '考研数学全书', '李永乐版，最新版', 30.00, '教材'),
(15, '滑板', '双翘，专业板', 100.00, '体育');