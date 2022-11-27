"use strict";


$(document).ready(function (event) {
    $(".like_button").on('click', function (event) {
        let id = this.id;
        let split_id = id.split('_');
        let action = split_id[0];
        let post_id = split_id[1];

        $.ajax({
            url: '/like/' + post_id + '/' + action,
            type: 'POST',
            data: {post_id: post_id, action: action},
            dataType: 'json',
            success: function (data) {
                $("like_" + post_id).html(data);
                $('unlikes_' + post_id).html(data);
            }
        });
    });
});

// $(document).ready(function (event) {
//     // like and unlike click
//     $(".like_button").click(function () {
//         // event.preventDefault();
//         let id = this.id;   // Getting Button id
//         let split_id = id.split("_");
//
//         let text = split_id[0];
//         let post_id = split_id[1];  // post_id
//
//         // AJAX Request
//         $.ajax({
//             url: '/like_action',
//             type: 'post',
//             data: {
//                 post_id: post_id,
//                 likeunlike: text
//             },
//             dataType: 'json',
//             success: function (data) {
//                 let like = data['like'];
//                 let unlike = data['unlike'];
//
//                 $("#like_" + post_id).json(data);      // setting likes
//                 $("#unlike_" + post_id).json(data);    // setting unlikes
//             }
//         });
//     });
// });