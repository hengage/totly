$('#load-more-comments').click(function() {
    console.log('load more clicked')
    console.log($(this).data('offset'))
    var post_id = $(this).data('post-id');
    var offset = $(this).data('offset');
    $.get('/load_more_comments/', {post_id: post_id, offset: offset}, function(data) {
        $('#comments-list').append(data.html);
        $('#load-more-comments').data('offset', offset + 6);
        if (data.html == '') {
            $('#load-more-comments').hide();
        }
    });
});
