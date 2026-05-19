---
sources: ["raw/Mitre/CWE/CWE-787 Out-of-bounds Write (4.20).md", "raw/Mitre/CWE/CWE-416 Use After Free (4.20).md", "raw/Mitre/CWE/CWE-122 Heap-based Buffer Overflow (4.20).md"]
tags: ["security", "memory-safety", "c-cpp", "exploit", "mitigation"]
---

# Lỗ hổng an toàn bộ nhớ (Memory Safety Vulnerabilities)

**Lỗ hổng an toàn bộ nhớ** là một loại lỗi phần mềm xảy ra khi một chương trình thực hiện các thao tác truy cập bộ nhớ không hợp lệ. Đây là một trong những nguyên nhân phổ biến nhất dẫn đến các vụ tấn công mạng nghiêm trọng, đặc biệt là trong các ngôn ngữ quản lý bộ nhớ thủ công như C và C++.

## Các loại lỗ hổng phổ biến

### 1. Ghi ngoài phạm vi (Out-of-bounds Write - CWE-787)
Ứng dụng viết dữ liệu vượt quá giới hạn của bộ đệm (buffer) được chỉ định (có thể là ghi sau khi kết thúc hoặc ghi trước khi bắt đầu).
*   **Hệ quả**: Làm hỏng bộ nhớ, ghi đè các dữ liệu điều khiển quan trọng (như địa chỉ trả về - return addresses) để thực thi mã bất hợp pháp, hoặc gây treo chương trình (Crash).
*   **Ví dụ**: Một vòng lặp không kiểm tra biên của mảng, dẫn đến việc ghi vào vị trí `id_sequence[3]` khi mảng chỉ được cấp phát cho 3 phần tử (index 0 đến 2).

### 2. Sử dụng sau khi giải phóng (Use After Free - CWE-416)
Xảy ra khi chương trình tiếp tục sử dụng một con trỏ sau khi vùng bộ nhớ mà nó trỏ tới đã được giải phóng. Xem chi tiết tại: [[use-after-free|Lỗ hổng Sử dụng sau khi Giải phóng]].

### 3. Tràn bộ đệm (Buffer Overflow)
Xảy ra khi ứng dụng ghi dữ liệu vượt quá dung lượng của bộ nhớ đệm được cấp phát.
*   **Tràn bộ đệm vùng Stack (Stack-based)**: Xảy ra trên ngăn xếp, thường dùng để ghi đè địa chỉ trả về của hàm.
*   **Tràn bộ đệm vùng Heap (Heap-based - CWE-122)**: Xảy ra trên vùng nhớ Heap (thường được cấp phát bằng `malloc()` hoặc `new`).
    *   **Cơ chế**: Kẻ tấn công ghi đè lên các vùng nhớ lân cận trên Heap, có thể chứa các con trỏ hàm (function pointers), dữ liệu quản lý của bộ cấp phát bộ nhớ (metadata), hoặc các đối tượng C++.
    *   **Hệ quả**: Thực thi mã tùy ý bằng cách điều hướng con trỏ hàm đến mã độc, hoặc gây lỗi treo ứng dụng (DoS).

## Các biện pháp phòng vệ

### 1. Lựa chọn ngôn ngữ lập trình
Sử dụng các ngôn ngữ có cơ chế quản lý bộ nhớ tự động (Garbage Collection) hoặc an toàn bộ nhớ như **Rust**, **Java**, **Python**, **Go** giúp ngăn chặn phần lớn các lỗi này ngay từ đầu.

### 2. Làm cứng quá trình biên dịch (Build Hardening)
*   **FORTIFY_SOURCE**: Cơ chế của GCC/Clang giúp phát hiện một số lỗi tràn bộ đệm tại thời điểm chạy.
*   **Stack Canaries**: Chèn các giá trị "chim yến" vào trước địa chỉ trả về để phát hiện việc ghi đè bộ đệm.
*   **Sử dụng API an toàn**: Thay thế các hàm nguy hiểm (như `gets()`, `strcpy()`, `sprintf()`) bằng các phiên bản có kiểm tra biên (như `fgets()`, `strncpy()`, `snprintf()`).

### 3. Làm cứng môi trường (Environment Hardening)
*   **ASLR (Address Space Layout Randomization)**: Ngẫu nhiên hóa vị trí của các thành phần trong bộ nhớ (thư viện, stack, heap).
*   **PIE (Position Independent Executable)**: Cho phép nạp file thực thi vào bất kỳ vị trí nào trong bộ nhớ, hỗ trợ tối đa cho ASLR.
*   **DEP/NX (Data Execution Prevention / No-Execute)**: Ngăn chặn việc thực thi mã trong các vùng nhớ dữ liệu (như Stack hoặc Heap).

### 4. Công cụ kiểm tra
*   **AddressSanitizer (ASan)**: Công cụ phát hiện lỗi bộ nhớ trong thời gian chạy cho C/C++.
*   **Fuzz Testing**: Sử dụng các công cụ (như AFL, libFuzzer) để tạo ra các đầu vào ngẫu nhiên nhằm tìm kiếm các lỗi gây treo máy hoặc hỏng bộ nhớ.
*   **Phân tích tĩnh (Static Analysis)**: Sử dụng các công cụ để quét mã nguồn và tìm các mẫu truy cập bộ nhớ không an toàn.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[linux-hardening|Tăng cường bảo mật Linux]]
- [[operating-system-security|An ninh hệ điều hành]]
