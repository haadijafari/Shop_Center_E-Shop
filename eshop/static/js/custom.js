function addProductToCart(productId, productCount) {
    $.get('/cart/add-product-tp-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        console.log(res)
    })
}
