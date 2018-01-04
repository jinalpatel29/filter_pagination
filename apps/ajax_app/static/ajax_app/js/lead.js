$(document).ready(function () {
    var page = 1;
    console.log("page load ")
    $(document.body).on('click', 'a', function (e) {
        e.preventDefault();
        page = $(this).html();
        console.log(page)
        getLeads();
    });

    $('form').change(function () {
        console.log("form change ")
        page = 1;
        getLeads();
    });

    $('form').submit(function (e) {
        console.log("form submit ")
        e.preventDefault();
    });

    // as you type name it will trigger getLeads function on keydown
    $('input[type=text]').keydown(function (e) {
        console.log("input key submit ")
        getLeads();
    });  

    function getLeads() {
        $('form').append('<input type="hidden" name="page" value="' + page + '">')      
        $.ajax({
            url: '/',
            method: 'post',
            data: $('form').serialize(),
            success: function (data) {
                $('.pagination').html($(data).find('#page'));
                $('.content').html($(data).find('table'));             
            }
        });
    }
});