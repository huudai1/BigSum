# BigSum - String-based Addition Algorithm

Dự án này thực hiện thuật toán cộng hai số nguyên lớn được biểu diễn dưới dạng chuỗi (strings), mô phỏng cách tính toán cột dọc của học sinh Tiểu học.

## Tính năng
- Sử dụng lớp `MyBigNumber` với phương thức `sum`.
- Ghi lại từng bước thực hiện phép cộng (Logging/Printing).
- Cộng hai chuỗi ký số không giới hạn độ dài.
- Xử lý biến nhớ (carry) chính xác.
- Hỗ trợ các chuỗi có độ dài khác nhau.

## Yêu cầu hệ thống
- Python 3.6 trở lên.

## Hướng dẫn cài đặt và chạy
1. **Clone dự án**:
   Theo quy ước, bạn nên clone dự án về thư mục theo cấu trúc sau:
   - Windows: `D:\Projects\github.com\youraccount\BigSum`
   - MacOS/Linux: `~/Projects/github.com/youraccount/BigSum`

   ```bash
   git clone https://github.com/youraccount/BigSum.git
   cd BigSum
   ```

2. **Chạy chương trình demo**:
   ```bash
   python main.py
   ```

3. **Chạy Unit Test**:
   Dự án sử dụng module `unittest` có sẵn của Python. Để chạy các test case:
   ```bash
   python -m unittest tests/test_math_utils.py
   ```

## Cấu trúc thư mục
- `src/`: Chứa mã nguồn chính (`math_utils.py`).
- `tests/`: Chứa các kịch bản kiểm thử đơn vị.
- `main.py`: Chương trình demo ví dụ có cấu hình logging.

## Phiên bản
- Current version: **0.0.1** (Được đánh dấu bằng tag `v0.0.1`)

