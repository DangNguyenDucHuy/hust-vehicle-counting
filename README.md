# hust-vehicle-counting


## Setup IDE
+ Tạo môi trường ảo (khuyến khích)
+ `pip install -r requirements.txt`
+ Tạo file `.env` cùng cấp với `src/` (tham khảo mẫu ở file `.env.example`)


## Setup dataset
+ Tạo folder `data/` cùng cấp với `src/`
+ Trong folder `data/` tạo thư mục con `data/raw/`
+ Nhét các video quay được (file `.mp4`) vào `data/raw/`


## Usage
+ Chạy luồng chính:
```bash
python src/main.py
```
Note: Tùy vào vị trí folder hiện tại thì thay đổi đường dẫn, nói chung là chạy file `main.py`

