/**
 * Created by Nate on 2015/9/5.
 */

function ajaxForm(){
    $.getJSON("/get_student_json", function (data) {
        $.each(data.students, function (i, item) {
            $("#info").append("<h3><em>"+ item.name + "</em></h3>");

            $.each(item.courses, function (i_c, c_item) {
               $("#info").append("<p>" + c_item.name +"</p>");
            });
        });


    });

    return false;

}