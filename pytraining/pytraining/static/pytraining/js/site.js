$(document).on('click', '.hint-control', function(){
    $(this).toggle()
    $(this).next().toggle()
})

$(document).on('click', '.hint', function(){
    $(this).toggle()
    $(this).prev().toggle()
})
