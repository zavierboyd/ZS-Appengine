$('document').ready(function(){
    env = {'a' : 'sd'}
    $("#input").on('keyup', function (e) {
        if (e.keyCode == 13) { // if key pressed was enter

            var com = $("#input").val()
            console.log(com)
            $("#input").val('')
            $("#repl").html('<tt> >>> '+com+'<tt><br/>'+$("#repl").html())

            $.ajax({type: 'POST',
                    url: '/eq',
                    data :{'com':com},
                    success :function(html){
                        html=html.split(':=:=:')
                        out = html[0]
                        nenv = html[1]
                        console.log(nenv)
                        out = '<pre>'+out+'</pre><br/>'+$("#repl").html()
                        $('#env').html('<pre>'+nenv+'</pre>')
                        $("#repl").html(out)
                        console.log(out)
                        }
            });
        }
    });
})