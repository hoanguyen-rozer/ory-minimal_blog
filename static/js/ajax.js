const btn = document.querySelector('#submit');
const form = document.querySelector('#comment-form');

const url = `/${post_id}/comment/`;
const request = new Request(
    url,
    {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
        body: new FormData(form),
    }
);

const messageEl = document.querySelector('#message');

btn.addEventListener('click', (e) => {
    e.preventDefault();
    submitComment();
});

const submitComment = async () => {
    try {
        let response = await fetch(request);
        const result = await response.json();
        console.log(result);
        renderLastComment(result);
        // showMessage(result.message, response.status == 200 ? 'success' : 'error');
    } catch (error) {
        // showMessage(error.message, 'error');
        console.log(error)
    }
};

const showMessage = (message, type = 'success') => {
    messageEl.innerHTML = `
        <div class="alert alert-${type}">
        ${message}
        </div>
    `;
};

const renderLastComment = (commentData) => {
    const formattedDate = toFormatDate(commentData.created_at)
    const commentsNode = document.querySelector('#comments');
    const lastComment = document.querySelector('#last-comment');
    let newComment = document.createElement("li");
    newComment.classList.add('comment');
    newComment.innerHTML = `<div class="thumbnail">
                        <img src="/static/images/Akatsuki.png"
                             alt="guess avatar">
                    </div>
                    <div class="details">
                        <h4 class="name">
                            <a href="#">${commentData.username}</a>
                        </h4>
                        <span class="date">${formattedDate}</span>
                        <p>
                            ${commentData.content}
                        </p>
                    </div>`
    lastComment.parentNode.insertBefore(newComment, lastComment);
}

const toFormatDate = (value) => {
    const months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    const dateObj = new Date(value);
    const year = dateObj.getFullYear();
    const monthName = months[dateObj.getMonth()]
    const date = dateObj.getDate();
    const formattedDate = `${date} ${monthName} ${year}`;
    return formattedDate
}