// tăng giảm số lượng (cart)

// Lấy tất cả các quantity selectors

document.addEventListener('DOMContentLoaded', function () {
  // Xử lý chọn số lượng sản phẩm
  const quantitySelectors = document.querySelectorAll(".quantity-selector");

  quantitySelectors.forEach((selector) => {
      const decreaseButton = selector.querySelector(".decrease");
      const increaseButton = selector.querySelector(".increase");
      const quantityInput = selector.querySelector(".quantity");

      // Xử lý khi nhấn nút tăng
      increaseButton.addEventListener("click", function () {
          const max = parseInt(quantityInput.max) || Infinity;
          const currentValue = parseInt(quantityInput.value) || 0;
          if (currentValue < max) {
              quantityInput.value = currentValue + 1;
          }
      });

      // Xử lý khi nhấn nút giảm
      decreaseButton.addEventListener("click", function () {
          const min = parseInt(quantityInput.min) || 1;
          const currentValue = parseInt(quantityInput.value) || 0;
          if (currentValue > min) {
              quantityInput.value = currentValue - 1;
          }
      });

      // Đảm bảo giá trị nhập tay nằm trong giới hạn
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
  });

  // Check tất cả (cart)
  const selectAllCheckbox = document.getElementById('selectAll');
  const optionCheckboxes = document.querySelectorAll('input[name="options"]');

  selectAllCheckbox.addEventListener('change', () => {
      optionCheckboxes.forEach(checkbox => {
          checkbox.checked = selectAllCheckbox.checked;
      });
  });

  optionCheckboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
          selectAllCheckbox.checked = [...optionCheckboxes].every(cb => cb.checked);
      });
  });

  // Thay đổi phân loại đơn hàng (order)
  function tatca(link) {
      const itemCards = document.getElementsByClassName("item-card");
      for (let i = 0; i < itemCards.length; i++) {
          itemCards[i].style.display = "block";
      }
      
      activeLink(link);
  }

  function dahuy(link) {
      const itemCard = document.getElementsByClassName("item-card");
      for (let i = 0; i < itemCard.length; i++) {
          itemCard[i].style.display = "none";
      }

      const itemCard2 = document.getElementsByClassName("item-card2");
      for (let i = 0; i < itemCard2.length; i++) {
          itemCard2[i].style.display = "block";
      }

      activeLink(link);
  }

  function other(link) {
      const itemCard = document.querySelectorAll('[class^="item-card"]');
      for (let i = 0; i < itemCard.length; i++) {
          itemCard[i].style.display = "none";
      }

      activeLink(link);
  }

  function activeLink(link) {
      // Lấy tất cả các liên kết
      const links = document.querySelectorAll('.filter-order');
  
      // Xóa kiểu dáng của tất cả các liên kết
      links.forEach(link => {
          link.style.borderBottom = '';
          link.style.borderWidth = '';
          link.style.paddingBottom = '';
      });
  
      // Thêm kiểu dáng cho liên kết vừa được click
      link.style.borderBottom = '1px solid #008DDC';
      link.style.borderWidth = 'thick';
      link.style.paddingBottom = '5px';
  }
});
