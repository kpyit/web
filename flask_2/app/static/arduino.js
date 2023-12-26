// alert(":")
// defer  надо у скрипта обязательно указывать
const paginationButtonEls = document.querySelectorAll('.pagination');
console.log(paginationButtonEls);
for (let index = 0; index < paginationButtonEls.length; index++) {

    const button = paginationButtonEls[index];
    console.log(button);
    // добавляем событие

    //асинхронная фунция вызывает асинхронную функцию и ждет ее ответа перед выводом
    button.addEventListener('click',async function() {
        // console.log(123);
        // получаем заданный атрибут
        // console.log(button.getAttribute('data-page'));
        const page = button.getAttribute('data-page');
        const users = await getUsers(button.getAttribute('data-page'));
        // console.log(users);
        renderUsers(users);

    }); 
}


//Асинхроная функция поскольку нужно дождаться ответа от сервера  "await"
async function getUsers(page){
    const response = await fetch(`/api/v1/arduino/${page}`);//скобки косые
    // console.log(response);
    const json = await response.json();    
    // console.log(json);
    return json;
}
 
function renderUsers(users){
    
    let content = "";
    //тут у него for и в нем он по текстовому шаблону выводит пользователей в 
    // document.querySelector('#app').innerHTML = 'hi';

};