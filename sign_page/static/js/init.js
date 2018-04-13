var input_tracking = function () {
    var kinput = document.getElementById('exampleInputEmail1');
    kinput.onkeypress = handle;
    var date = new Date();
    function handle(e) {
        var text = e.type +
            ' keyCode=' + e.keyCode +
            ' which=' + e.which +
            ' charCode=' + e.charCode +
            ' char=' + String.fromCharCode(e.keyCode || e.charCode) +
            (e.shiftKey ? ' +shift' : '') +
            (e.ctrlKey ? ' +ctrl' : '') +
            (e.altKey ? ' +alt' : '') +
            (e.metaKey ? ' +meta' : '') + "\n";
        console.log(text + (new Date() - date));
        date = new Date()
    }


};


$(document).ready(function (){
    input_tracking();
});