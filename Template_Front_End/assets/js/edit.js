document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const fullNameInput = document.getElementById("fullName");
    const phoneInput = document.getElementById("phone");
    const birthDateInput = document.getElementById("birthDate");
  
    // Kiểm tra thông tin khi gửi form
    form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const fullName = fullNameInput.value.trim();
      const phone = phoneInput.value.trim();
      const birthDate = birthDateInput.value;
  
      if (!fullName) {
        alert("Họ và tên không được để trống!");
        return;
      }
  
      if (!/^\d{10}$/.test(phone)) {
        alert("Số điện thoại phải là 10 chữ số!");
        return;
      }
  
      if (!birthDate) {
        alert("Vui lòng chọn ngày sinh!");
        return;
      }
  
      // Hiển thị thông báo khi tất cả dữ liệu hợp lệ
      alert("Cập nhật thông tin thành công!");
    });
  });
  