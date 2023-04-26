$('#load-more-comments').click(function() {
    var post_id = $(this).data('post-id');
    var offset = $(this).data('offset');

    $.get('/load_more_comments/', {post_id, offset}, function(data) {
        $('#comments-list').append(data.html);
        $('#load-more-comments').data('offset', offset + 6);
        if ( !data.has_more_comments) {
            $('#load-more-comments').hide();
        }
    }).fail(function() {
        console.log('Failed to load more comments');
    });;
});