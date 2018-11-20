$(document).ready(function(){
    $("#submitPostButton").click(function(){
        alert( $("#invoice").val());
        $.post("http://127.0.0.1:5000/invoice",
        $("#invoice").val(),
        function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });
});