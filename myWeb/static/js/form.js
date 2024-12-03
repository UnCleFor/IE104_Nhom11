// Lấy các phần tử modal và nút mở/đóng modal
const openModalBtn = document.getElementById("openModalBtn");
const modal = document.getElementById("modal");
const closeModalBtn = document.getElementById("closeModalBtn");

const openChildModalBtn = document.getElementById("openChildModalBtn");
const childModal = document.getElementById("childModal");
const closeChildModalBtn = document.getElementById("closeChildModalBtn");

// Mở Modal Cha
openModalBtn.onclick = function() {
    modal.style.display = "block";
}

// Đóng Modal Cha
closeModalBtn.onclick = function() {
    modal.style.display = "none";
}

// Mở Modal Con
openChildModalBtn.onclick = function() {
    childModal.style.display = "block";
}

// Đóng Modal Con
closeChildModalBtn.onclick = function() {
    childModal.style.display = "none";
}

// Đóng modal khi nhấp ra ngoài
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    if (event.target == childModal) {
        childModal.style.display = "none";
    }
}