# 校园二手平台 · 后端

- 痛点：手工管理校园二手交易流程繁琐，易出错
- 方案：独立开发命令行版后端系统，支持注册/登录/发布/下单全链路
- 数据：覆盖 4 张核心表，15 条测试数据，支持事务回滚
- 演示：

---

## 技术栈
- Python 3.8
- MySQL 8.0 + pymysql
- 面向对象 + 事务控制 + 异常处理

---

## 数据库设计
- users 表：用户注册/登录（user_id, username, password, email, phone）
- products 表：商品发布（product_id, seller_id, title, price, category, status）
- orders 表：订单管理（order_id, buyer_id, product_id, total_price, status）
- reviews 表：评价系统（review_id, order_id, rating, content）

---

## 功能清单
- [x] 用户注册（含用户名唯一性校验 + IntegrityError 捕获）
- [x] 用户登录（密码校验 + 全局会话保持）
- [x] 商品发布（卖家身份验证）
- [x] 订单下单（事务控制：try/except/finally + commit/rollback）
- [x] 订单查询（多表 JOIN：orders + products + users）
- [x] 异常处理（通用 Exception 捕获 + 连接关闭保护）

---

## 核心代码亮点
1. 事务控制（订单支付场景）
   - 使用 try/except/finally 结构
   - 成功时 commit，异常时 rollback 保证数据一致性
   - finally 确保 `cursor` 和 `conn` 一定关闭
2. 多表 JOIN 查询（订单详情）
   - orders 表 JOIN products 表得到商品名称
   - JOIN users 表得到卖家用户名
   - WHERE 筛选出当前登录用户的订单
   - ORDER BY created_at DESC 按时间倒序排列

---

## 1.快速开始
```bash
git clone https://github.com/Yaocen-wq/campus-market-test-automation.git
cd campus-market-test-automation
```

## 2.初始化数据库
```
mysql -u root -p < database/create_tables.sql
```

## 3.运行后端
```
cd backend
python campus_market_cli.py
```

## 4.测试流程
```
注册新用户 → 登录 → 发布商品 → 输入商品ID下单 → 查看订单
```

## 联系方式
邮箱：huangjin130814@qq.com