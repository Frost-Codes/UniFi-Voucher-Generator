$('.mark-used').click(function(){
    var id = $(this).attr("pid").toString();

    var to_remove = this.parentNode.parentNode.parentNode.parentNode
    $.ajax({
        type:"GET",
        url:"/markused",
        data:{
            used_id:id
        },
        success:function(data){
            to_remove.remove()

            
        }
    })
})