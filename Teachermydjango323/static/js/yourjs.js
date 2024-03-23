function onsale(){
    var name=document.getElementById('name');
    var price=document.getElementById('price');
    var qty=document.getElementById('qty');

    document.getElementById('demo').innerHTML="咖啡名稱：" + name.value + "<br>"
                                             +"咖啡價格：" + price.value + "<br>"
                                             +"訂購數量：" + qty.value + "<br>"
                                             +"訂購總額：" + (price.value * qty.value) + " 元<br>";
                                             
}