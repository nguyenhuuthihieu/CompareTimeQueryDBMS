# CompareTimeQueryDBMS

[CompareTimeQueryDBMS](https://github.com/nguyenhuuthihieu/CompareTimeQueryDBMS) so sanh thoi gian xu ly giua Mysql va ArangoDB

So sanh thoi gian xu ly cac truy van:
- Đọc bản ghi/documents có điều kiện, có index 
- Đọc bản ghi/documents có điều kiện, không index
- Đọc bản ghi/documents và sắp xếp
- Chỉnh sửa bản ghi/documents
- Xóa một bản ghi/documnent
- Join nhiều bảng/collections



## Run CompareTimeQueryDBMS with Mysql and ArangoDB

### 1. Get the code
    git clone https://github.com/nguyenhuuthihieu/CompareTimeQueryDBMS
    cd CompareTimeQueryDBMS

### 2. Install requirements 
    pip install -r requirements.txt

### 3. Set the arguments to access the databases
    open Mysql/MysqlConnect.py 
    and replace the host, user, passwd, database.
    
    open ArangoDB/ArangoDBConnect.py 
    in the function arangoDBConnect()
    replace the '_system' with your database name
    replace the username, password
### 4. Run the application
    python app.py

### 5. Go to http://localhost:5000/
