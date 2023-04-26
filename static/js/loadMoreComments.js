$('#load-more-comments').click(function() {
    var post_id = $(this).data('post-id');
    var offset = $(this).data('offset');

    $.get('/load_more_comments/', {post_id, offset}, function(data) {
        $('#comments-list').append(data.html);
        $('#load-more-comments').data('offset', offset + 6);
        console.log(data.html);
        if ( data.html === null || data.html.trim() === '') {
            console.log('if statement')
            $('#load-more-comments').hide();
        }
    });
});