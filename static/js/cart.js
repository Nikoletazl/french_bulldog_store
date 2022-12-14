var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            UpdateUserOrder(productId, action)
        }
    })
}

function UpdateUserOrder(productId, action) {
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })
        .then((response) => {
            if (response.ok !== true) {
                throw  new Error('Can not update the order!')
            }
            return response.json()
        })
        .then((data) => {
           location.reload()
        })
        .catch(err => {
            alert(err.message)
        })

}