//Phân trang các sản phẩm 

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
