$('document').ready(function(){
    $('#run').on('click', function(e){
        var program = document.getElementById('program').value;
        var name = $('#name').value;
        console.log(program, name);
        $.ajax({type: 'GET',
                url: '/run',
                data: {'name': name, 'program': program},
                success: function(html){
                        out = html
                        $("#out").html(out)
                        console.log(html)
                        }
        });
    });
});