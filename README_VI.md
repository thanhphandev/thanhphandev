# Cấu trúc chuẩn cho dự án GitHub Profile

## 📋 Mô tả

Dự án này tạo ra một cấu trúc chuẩn cho GitHub profile với hệ thống CI/CD tự động cập nhật nội dung.

## 🏗️ Cấu trúc dự án

```
thanhphandev/
├── .github/workflows/          # Quy trình CI/CD
│   ├── update-readme.yml      # Cập nhật hàng ngày
│   └── stats-update.yml       # Cập nhật thống kê
├── scripts/                   # Scripts tự động hóa
│   ├── update_readme.py       # Script cập nhật README
│   └── setup.py              # Script thiết lập
├── assets/                    # Tài nguyên tĩnh
├── README.md                  # Trang profile chính
├── requirements.txt           # Dependencies Python
├── package.json               # Cấu hình Node.js
├── .gitignore                # Quy tắc Git ignore
├── LICENSE                   # Giấy phép MIT
└── PROFILE_CONFIG.md         # Tài liệu cấu hình
```

## ✨ Tính năng

### 🤖 Tự động hóa CI/CD
- **Cập nhật hàng ngày**: Tự động cập nhật thống kê và repositories mới nhất
- **GitHub Actions**: Sử dụng workflows để tự động hóa
- **Lên lịch linh hoạt**: Có thể chạy thủ công hoặc theo lịch

### 📊 Nội dung động
- **GitHub Stats**: Hiển thị thống kê GitHub realtime
- **Recent Projects**: Danh sách repositories mới nhất
- **Activity Graph**: Biểu đồ hoạt động GitHub
- **Trophy**: Thành tích và giải thưởng
- **Tech Stack**: Công nghệ và kỹ năng

### 🎨 Thiết kế chuyên nghiệp
- **Theme nhất quán**: Sử dụng Tokyo Night theme
- **Responsive**: Hiển thị tốt trên mọi thiết bị
- **Icons & Badges**: Sử dụng icons và badges chuyên nghiệp
- **Typography**: Font và layout đẹp mắt

## 🚀 Hướng dẫn sử dụng

### 1. Thiết lập ban đầu
```bash
# Clone repository
git clone https://github.com/thanhphandev/thanhphandev.git
cd thanhphandev

# Chạy script thiết lập
python3 scripts/setup.py
```

### 2. Tùy chỉnh thông tin cá nhân
- Cập nhật thông tin trong `README.md`
- Thay đổi links social media
- Cập nhật skills và technologies

### 3. Cấu hình CI/CD
- Workflows sẽ tự động chạy sau khi push lên GitHub
- Kiểm tra tab "Actions" để xem trạng thái

### 4. Tùy chỉnh nâng cao
- Chỉnh sửa `scripts/update_readme.py` để thay đổi logic cập nhật
- Cập nhật lịch chạy trong workflow files
- Thêm các sections mới vào README

## 🛠️ Công nghệ sử dụng

- **Python 3.8+**: Script automation
- **GitHub Actions**: CI/CD pipeline
- **GitHub API**: Lấy dữ liệu repositories
- **Markdown**: Format nội dung
- **YAML**: Cấu hình workflows

## 📅 Lịch cập nhật

- **Daily (00:00 UTC)**: Cập nhật toàn bộ profile
- **Every 6 hours**: Cập nhật GitHub stats
- **Manual trigger**: Có thể chạy thủ công qua GitHub Actions

## 🔧 Troubleshooting

### Lỗi API rate limit
- Đảm bảo `GITHUB_TOKEN` được cấu hình đúng
- API có giới hạn 5000 requests/hour cho authenticated users

### Workflow không chạy
- Kiểm tra permissions trong repository settings
- Đảm bảo GitHub Actions được enabled

### Cập nhật không thành công
- Kiểm tra logs trong GitHub Actions tab
- Verify syntax của các script files

## 📚 Tài liệu tham khảo

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Markdown Guide](https://www.markdownguide.org/)

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📄 License

Dự án này sử dụng [MIT License](LICENSE).

---

**🔄 Tự động cập nhật bởi GitHub Actions**