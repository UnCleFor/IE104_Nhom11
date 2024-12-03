//1. Phân trang các sản phẩm 

// Lắng nghe sự kiện click trên các phần tử có class "nextbtn"
let current = 1;
let max = 3;
document.addEventListener("click", function (event) {
    // Kiểm tra nếu phần tử được click có class "nextbtn"
    if (event.target.classList.contains("nextbtn")) {
        let cardsprev = document.getElementsByClassName(`card${current}`);

        // Lặp qua từng phần tử và xóa class "activated"
        for (let card of cardsprev) {
            card.classList.remove("activated");
        }
        current < max ? (current += 1) : (current = max);
        const cards = document.getElementsByClassName(`card${current}`);

        // Lặp qua từng phần tử và thêm class "activated"
        for (let card of cards) {
            card.classList.add("activated");
        }
    }
    if (event.target.classList.contains("prevbtn")) {
        // Thêm class "activated" vào phần tử đó
        let cardsprev = document.getElementsByClassName(`card${current}`);

        // Lặp qua từng phần tử và xóa class "activated"
        for (let card of cardsprev) {
            card.classList.remove("activated");
        }
        //set lại current
        current > 1 ? (current -= 1) : (current = 1);

        const cardsnow = document.getElementsByClassName(`card${current}`);

        // Lặp qua từng phần tử và thêm class "activated"
        for (let card of cardsnow) {
            card.classList.add("activated");
        }
    }
    if (event.target.classList.contains("page_btn")) {

        const value = parseInt(event.target.getAttribute("value"));
        if (value) {
            let cardsprev = document.getElementsByClassName(`card${current}`);
            for (let card of cardsprev) {
                card.classList.remove("activated");
            }


            current = value;

            const cardsnow = document.getElementsByClassName(`card${current}`);
            for (let card of cardsnow) {
                card.classList.add("activated");
            }
        }
    }
});

// 2. Carousel cho ảnh sản phẩm

document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('#carouselExampleIndicators');
    const thumbnails = document.querySelectorAll('.carousel-thumbnails img');
    const thumbnailsWrapper = document.querySelector('.carousel-thumbnails');
    const thumbPrev = document.querySelector('#thumbPrev');
    const thumbNext = document.querySelector('#thumbNext');
    
    const maxVisibleThumbnails = 4; // Số lượng thumbnails tối đa hiển thị mỗi lần
    const totalThumbnails = thumbnails.length; // Tổng số ảnh thumbnail
    let startIndex = 0; // Vị trí bắt đầu của thumbnails đang hiển thị
    let activeIndex = 0; // Vị trí của ảnh đang active trên carousel
    
    const updateThumbnailVisibility = () => {
        // Kiểm tra nút Prev
        if (startIndex === 0) {
            thumbPrev.classList.add('d-none'); // Ẩn nếu đang ở vị trí đầu tiên
        } else {
            thumbPrev.classList.remove('d-none'); // Hiện nếu không ở vị trí đầu tiên
        }
    
        // Kiểm tra nút Next
        if (startIndex + maxVisibleThumbnails >= totalThumbnails) {
            thumbNext.classList.add('d-none'); // Ẩn nếu ở vị trí cuối cùng
        } else {
            thumbNext.classList.remove('d-none'); // Hiện nếu còn ảnh phía sau
        }
    
        // Dịch chuyển thumbnails (Hiện 4 ảnh mỗi lần)
        const offset = -startIndex * (60 + 10); // 60px là chiều rộng mỗi ảnh, 10px là khoảng cách giữa các ảnh
        thumbnailsWrapper.style.transform = `translateX(${offset}px)`;
    };

    // Cập nhật lại ảnh active cho các thumbnail
    const updateActiveThumbnail = () => {
        thumbnails.forEach((thumbnail, index) => {
            if (index === activeIndex) {
                thumbnail.classList.add('active-thumbnail');
            } else {
                thumbnail.classList.remove('active-thumbnail');
            }
        });
    };
  
    // Sự kiện bấm nút Prev
    thumbPrev.addEventListener('click', (e) => {
        e.preventDefault(); // Ngừng hành động mặc định của nút Prev
        if (startIndex > 0) {
            startIndex -= maxVisibleThumbnails; // Di chuyển 4 ảnh về phía trước
            activeIndex -= maxVisibleThumbnails; // Di chuyển 4 ảnh về phía trước trong carousel
            if (startIndex < 0) startIndex = 0; // Đảm bảo không bị tràn quá ảnh đầu tiên
            updateThumbnailVisibility();
            
            // Đặt lại activeIndex thành ảnh đầu tiên của nhóm thumbnail mới
            activeIndex = startIndex;
            updateActiveThumbnail();
            
            // Chuyển đến ảnh đầu tiên của nhóm thumbnail hiện tại
            const carouselInstance = bootstrap.Carousel.getInstance(carousel);
            carouselInstance.to(activeIndex); // Chuyển đến slide tương ứng
        }
    });
    
    // Sự kiện bấm nút Next
    thumbNext.addEventListener('click', (e) => {
        e.preventDefault(); // Ngừng hành động mặc định của nút Next
        if (startIndex + maxVisibleThumbnails < totalThumbnails) {
            startIndex += maxVisibleThumbnails; // Di chuyển 4 ảnh về phía sau
            activeIndex += maxVisibleThumbnails; // Di chuyển 4 ảnh tiếp theo trong carousel
            updateThumbnailVisibility();
            
            // Đặt lại activeIndex thành ảnh đầu tiên của nhóm thumbnail mới
            activeIndex = startIndex;
            updateActiveThumbnail();
            
            // Chuyển đến ảnh đầu tiên của nhóm thumbnail mới
            const carouselInstance = bootstrap.Carousel.getInstance(carousel);
            carouselInstance.to(activeIndex); // Chuyển đến slide tương ứng
        }
    });
    
    // Đồng bộ trạng thái thumbnails khi carousel thay đổi slide
    carousel.addEventListener('slide.bs.carousel', function (e) {
        activeIndex = parseInt(e.relatedTarget.dataset.bsSlideTo);
        
        // Kiểm tra và đặt lại startIndex sao cho luôn bắt đầu từ ảnh đầu tiên của nhóm
        if (activeIndex % maxVisibleThumbnails === 0 || activeIndex === 0) {
            startIndex = activeIndex; // Đặt lại startIndex về ảnh đầu tiên của nhóm
        } else if (activeIndex % maxVisibleThumbnails !== 0 && activeIndex > startIndex + maxVisibleThumbnails - 1) {
            startIndex = activeIndex - (activeIndex % maxVisibleThumbnails); // Điều chỉnh startIndex về ảnh đầu tiên trong nhóm
        }
        
        // Đặt lại active thumbnail
        updateActiveThumbnail();
        updateThumbnailVisibility(); // Cập nhật lại vị trí của các thumbnails
    });
  
    // Khởi tạo trạng thái ban đầu
    updateThumbnailVisibility();
    updateActiveThumbnail();
});

// 3. Hộp chọn số lượng sản phẩm

// Lấy tất cả các quantity selectors
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

/* Nút like */

const likeButton = document.getElementById("likeButton");
const likeIcon = document.getElementById("likeIcon");

// Xử lý sự kiện click
likeButton.addEventListener("click", () => {
  // Toggle class "liked" khi nhấn
  likeButton.classList.toggle("liked");

  // Kiểm tra trạng thái "liked"
  if (likeButton.classList.contains("liked")) {
    likeIcon.classList.remove("fa-regular", "fa-heart");
    likeIcon.classList.add("fa-solid", "fa-heart"); // Đổi thành trái tim xám khi liked
  } else {
    likeIcon.classList.remove("fa-solid", "fa-heart");
    likeIcon.classList.add("fa-regular", "fa-heart"); // Đổi về trái tim trống khi bỏ liked
  }
});

// Lặp lại 12 sản phẩm kiểu 1

// document.addEventListener("DOMContentLoaded", () => {
//     const products = [
//         {
//             img: './assets/img/product/paracetalmol.jpg',
//             title: 'Paracetamol thuốc bổ giảm giá săn sele sập sàn siêu deal siêu hot',
//             oldPrice: '120.000 đ',
//             newPrice: '100.000 đ/Hộp',
//             likes: '35.1k',
//             sold: '6.5k'
//         },
       
//     ];

    
//     while (products.length < 12) {
//         products.push(products[0]);
//     }

//     const grid = document.querySelector('.grid');

//     products.forEach(product => {
//         const card = document.createElement('div');
//         card.className = 'card';

//         card.innerHTML = `
//             <img src="${product.img}" class="card-img-top" alt="">
//             <div class="card-body">
//                 <h5 class="card-title line-clamp">${product.title}</h5>
//                 <p class="price"><del>${product.oldPrice}</del></p>
//                 <div class="product-info">
//                     <p class="price">${product.newPrice}</p>
//                     <div class="rate-and-sold">
//                         <p class="rate"><i class="fa-solid fa-heart"></i>${product.likes}</p>
//                         <p class="vertical-line">|</p>
//                         <p class="sold">Đã bán ${product.sold}</p>
//                     </div>
//                 </div>
//                 <button>CHỌN MUA</button>
//             </div>
//         `;

//         grid.appendChild(card);
//     });
// });

//Lặp lại 12 sản phẩm kiểu 2


// const products = Array(12).fill({
//     imgSrc: './assets/img/product/paracetalmol.jpg',
//     title: 'Paracetamol thuốc bổ giảm giá săn sele sập sàn siêu deal siêu hot siêu sang siêu giàu',
//     oldPrice: '120.000 đ',
//     newPrice: '100.000 đ/Hộp',
//     likes: '35.1k',
//     sold: '6.5k'
// });

// const productGrid = document.getElementById('productGrid');

// products.forEach(product => {
//     const card = document.createElement('div');
//     card.classList.add('card');
//     card.innerHTML = `
//         <img src="${product.imgSrc}" class="card-img-top" alt="">
//         <div class="card-body">
//             <h5 class="card-title line-clamp">${product.title}</h5>
//             <p class="price"><del>${product.oldPrice}</del></p>
//             <div class="product-info">
//                 <p class="price">${product.newPrice}</p>
//                 <div class="rate-and-sold">
//                     <p class="rate"><i class="fa-solid fa-heart"></i>${product.likes}</p>
//                     <p class="vertical-line">|</p>
//                     <p class="sold">Đã bán ${product.sold}</p>
//                 </div>
//             </div>
//             <button>CHỌN MUA</button>
//         </div>
//     `;
//     productGrid.appendChild(card);
// });
