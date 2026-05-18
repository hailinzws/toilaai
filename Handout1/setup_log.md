1. Lỗi thực gặp (Issue)
Mô tả: Khi chạy lệnh kích hoạt môi trường ảo trên PowerShell, hệ thống báo lỗi đỏ với nội dung ngăn cản thực thi script.

Thông báo lỗi: ... cannot be loaded because running scripts is disabled on this system.

Mã lỗi: PSSecurityException hoặc UnauthorizedAccess.

Nguyên nhân: Do chính sách bảo mật mặc định của Windows PowerShell (Execution Policy) ngăn chặn việc chạy các script chưa được xác thực (bao gồm cả file activate.ps1 của venv).

2. Cách tìm giải pháp (Troubleshooting)
Tìm kiếm mã lỗi trên Google hoặc Stack Overflow với từ khóa: "PowerShell activate venv scripts disabled".

Sử dụng lệnh Get-ExecutionPolicy trong PowerShell để kiểm tra trạng thái bảo mật hiện tại của hệ thống.

Xác định rằng cần phải thay đổi quyền thực thi script cho người dùng hiện tại để cho phép môi trường ảo hoạt động.

3. Giải pháp khắc phục (Resolution)
Để khắc phục, cần mở PowerShell với quyền quản trị (Run as Administrator) và cấp quyền thực thi script bằng lệnh sau:

PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Sau khi chạy lệnh trên, có thể kích hoạt môi trường ảo bình thường bằng lệnh:

PowerShell
.venv\Scripts\Activate.ps1
4. Link nguồn tham khảo (References)
Microsoft Learn - About Execution Policies

Python Documentation - venv module

Stack Overflow - PSSecurityException when activating virtualenv