% rebase('layout.tpl',  year=year)

<div class="Update">
    <p></p>
    <h1>ОБНОВЛЕНИЕ 7.33<br>НОВЫЕ ГОРИЗОНТЫ</h1> <!-- Заголовок обновления -->
    <p class="update">Новая карта, масштабные игровые изменения и многое, многое другое. <br>Перед вами открывается новый мир.</p>
    

    
    <h2>Оставить отзыв:</h2> <!-- Блок отзывов с воодом данных имени, отзыва и номера телефона -->
    <form method="POST" action="/activeusers">
        <label for="nickname">Никнейм:</label>
        <input type="text" id="nickname" name="nickname" required><br>
        <label for="review">Отзыв:</label>
        <textarea id="review" name="review" required></textarea><br>
        <label for="phone">Номер телефона:</label>
        <input type="text" id="phone" name="phone" required><br>
        <input type="submit" value="Добавить отзыв">
    </form>

    <h2>Все отзывы:</h2>
    <ul>
    % for review1 in reviews1:            
                <li><strong>{{ review1['nickname'] }}</strong>: {{ review1['review'] }} </strong>: {{ review1['timestamp'] }} )</li> <!-- Список всех подготовленных отзывов -->          
         % end
        % for review in reviews:
            <li><strong>{{ review['nickname'] }}</strong>: {{ review['review'] }} </strong>: {{ review['timestamp'] }} )</li> <!-- Список всех отзывов -->
         % end        
    </ul>