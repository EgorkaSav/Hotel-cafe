// Получаем модальное окно

var modal = document.getElementById("myModal");


// Получаем элемент <span>, который закрывает модальное окно

var span = document.getElementsByClassName("close")[0];


// При клике на <span> (x), закрыть модальное окно

span.onclick = function() {

    modal.style.display = "none";

}


// Показать модальное окно

function showModal() {

    modal.style.display = "block";

}


// Когда пользователь кликает в любом месте за пределами модального окна, закрыть его

window.onclick = function(event) {

    if (event.target == modal) {

        modal.style.display = "none";

    }

}


// Допустим, это функция, которая вызывается при успешном входе пользователя

function onLoginSuccess() {

    showModal();

}


// Пример использования

// Предположим, у вас есть обработчик события отправки формы, который проверяет учетные данные пользователя

document.querySelector('.login-form').addEventListener('submit', function(event) {

    event.preventDefault(); // Предотвращаем стандартную отправку формы

    // Здесь должна быть ваша логика проверки учетных данных пользователя...

    

    // Если проверка успешна, показываем модальное окно

    showModal();

});