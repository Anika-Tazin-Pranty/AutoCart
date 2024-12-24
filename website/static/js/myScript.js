$('.plus-cart').click(function(){
<<<<<<< Updated upstream
    console.log('Button clicked')

    var id = $(this).attr('pid').toString()
    var quantity = this.parentNode.children[2]

    $.ajax({
        type: 'GET',
        url: '/pluscart',
        data: {
            cart_id: id
        },
        
=======
    console.log('Button Clicked!')

    var id = $(this).attr('pid').toString()
    var quantity = this.parentNode.children[2]
    
    $.ajax({
        type: 'GET',
        url: '/pluscart',
        data: {cart_id: id},
>>>>>>> Stashed changes
        success: function(data){
            console.log(data)
            quantity.innerText = data.quantity
            document.getElementById(`quantity${id}`).innerText = data.quantity
            document.getElementById('amount_tt').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        }
    })
})

<<<<<<< Updated upstream

$('.minus-cart').click(function(){
    console.log('Button clicked')

    var id = $(this).attr('pid').toString()
    var quantity = this.parentNode.children[2]

    $.ajax({
        type: 'GET',
        url: '/minuscart',
        data: {
            cart_id: id
        },
        
=======
$('.minus-cart').click(function(){
    console.log('Button Clicked!')

    var id = $(this).attr('pid').toString()
    var quantity = this.parentNode.children[2]
    
    $.ajax({
        type: 'GET',
        url: '/minuscart',
        data: {cart_id: id},
>>>>>>> Stashed changes
        success: function(data){
            console.log(data)
            quantity.innerText = data.quantity
            document.getElementById(`quantity${id}`).innerText = data.quantity
            document.getElementById('amount_tt').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        }
    })
})

<<<<<<< Updated upstream

$('.remove-cart').click(function(){
    var id = $(this).attr('pid').toString()
    var to_remove = this.parentNode.parentNode.parentNode.parentNode

    $.ajax({
        type: 'GET',
        url: 'removecart',
        data: {
            cart_id: id
        },

        success: function(data){
            document.getElementById('amount_tt').innerText = data.amount
            document.getElementById('totalamount').innnerText = data.total
=======
$('.remove-cart').click(function(){
    console.log('Button Clicked!')

    var id = $(this).attr('pid').toString()
    var to_remove = this.parentNode.parentNode.parentNode.parentNode // removes the whole div (nested 4)

    $.ajax({
        type: 'GET',
        url: '/remove-cart',
        data: {cart_id: id},
        success: function(data){
            document.getElementById('amount_tt').innerText = data.amount
            document.getElementById('totalamount').innerText = data.total
>>>>>>> Stashed changes
            to_remove.remove()
        }
    })
})