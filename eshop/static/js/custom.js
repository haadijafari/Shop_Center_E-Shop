function addProductToCart(productId, productCount=1) {
    $.get('/cart/add-product-tp-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        if (res.status === 'success') {
            Swal.fire({
                title: "محصول به سبد اضافه شد",
                text: "تعداد یک عدد از محصول مورد نظر به سبد خرید شما اضافه شد!",
                icon: "success",
                confirmButtonText: "متوجه شدم"
            });
        } else if (res.status === 'not_authorized') {
            Swal.fire({
                title: "لطفا با حساب خود وارد شوید",
                text: "کاربر گرامی، شما در حال حاضر بدون حساب خود مشغول فعالیت هستید. لطفا برای افزودن محصول به سبد خرید خود ابتدا وارد یک حساب کاربری شوید.",
                icon: "warning",
                confirmButtonText: "وارد شوید"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '/login';
                }
            })
        }
    })
}


function removeCartDetail(itemId) {
    $.get('/cart/remove-cart-detail?item_id=' + itemId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


// detail id => order detail id
// state => increase , decrease
function changeCartDetailCount(itemId, state) {
    $.get('/cart/change-cart-detail?item_id=' + itemId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}
