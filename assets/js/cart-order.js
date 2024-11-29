// Hộp chọn số lượng sản phẩm

// Lấy các phần tử
const decreaseButton = document.getElementById("decrease");
const increaseButton = document.getElementById("increase");
const quantityInput = document.getElementById("quantity");

// Xử lý khi nhấn nút tăng
increaseButton.addEventListener("click", function () {
  const max = parseInt(quantityInput.max) || Infinity; // Đọc giá trị max từ input
  const currentValue = parseInt(quantityInput.value) || 0;
  if (currentValue < max) {
    quantityInput.value = currentValue + 1;
  }
});

// Xử lý khi nhấn nút giảm
decreaseButton.addEventListener("click", function () {
  const min = parseInt(quantityInput.min) || 1; // Đọc giá trị min từ input
  const currentValue = parseInt(quantityInput.value) || 0;
  if (currentValue > min) {
    quantityInput.value = currentValue - 1;
  }
});

// Đảm bảo giá trị nhập tay vẫn nằm trong giới hạn
quantityInput.addEventListener("input", function () {
  const min = parseInt(quantityInput.min) || 1;
  const max = parseInt(quantityInput.max) || Infinity;
  const value = parseInt(quantityInput.value) || min;
  if (value < min) {
    quantityInput.value = min;
  } else if (value > max) {
    quantityInput.value = max;
  }
});
