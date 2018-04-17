//save_data('file text', 'myfilename.txt', 'text/plain')"
var arr_delta = [];

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
        var delta = (new Date() - date);
        console.log(text + (new Date() - date));
        date = new Date();
        arr_delta.push(delta)
    }
};

//var submit = document.getElementById('SaveData');
//submit.click = save_data();

var data_transfer = function () {
    document.cookie = "arr=" + arr_delta;
};

var save_data = function (data, filename, type) {
    var file = new Blob([data], {type: type});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function() {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
    alert("Saved");

    console.log("Файл сохранён.");
};


$(document).ready(function (){
    input_tracking();
});