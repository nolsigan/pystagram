var Blog = {
    init: function() {
        this.subscribe();
    },

    // 블로그를 구독한다
    subscribe: function() {
        $('.blog_subscribe').on('click', function() {
            console.log(window.location.host);
        });
    }
}

$(function() {
    Blog.init();
});