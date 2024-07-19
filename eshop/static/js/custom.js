function addProductToCart(productId, productCount) {
    $.get('/cart/add-product-tp-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        if (res.status === 'success') {
            Swal.fire({
                title: "محصول به سبد اضافه شد",
                text: "تعداد یک عدد از محصول مورد نظر به سبد خرید شما اضافه شد!",
                icon: "success",
                confirmButtonText: "متوجه شدم"
            });
        }
        else if (res.status === 'not_authorized') {
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