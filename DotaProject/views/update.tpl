% rebase('layout.tpl',  year=year)

<div class="Update">
    <p></p>
    <h1>ОБНОВЛЕНИЕ 7.33<br>НОВЫЕ ГОРИЗОНТЫ</h1> <!-- Заголовок обновления -->
    <p class="update">Новая карта, масштабные игровые изменения и многое, многое другое. <br>Перед вами открывается новый мир.</p>
    <div style="display: flex; justify-content: center;">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/k2gaw3wc_P4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <h2>ОБНОВЛЕНИЕ КАРТЫ</h2> <!-- Информация по обновлению карты -->
    <p class="updateMap">Карта значительно расширилась, но цель игры осталась прежней. Линии не отдалились друг от <br>друга, и всё нужное для победы по-прежнему находится в центре карты.<br><br>
На расширившейся на 40% территории нашлось место и новым ресурсам,<br> и неизведанным стратегиям. <br>Оба основных леса тоже не обошлись без масштабных изменений обзора, тропинок, лагерей крипов и не только.</p>
    
    <div style="margin-bottom: 40px;"> <!-- Картинка карты и стиль -->
      <img src="static\images\maps.png">
    </div>

    <div style="overflow: auto; margin-bottom: 40px;"> <!-- Блоки и стили подробности обновлений -->
      <img src="static\images\roshan_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\logovo.jpg">НОВЫЕ ДОМА РОШАНА</h3>
      <p class="updateText">{{ text }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\portal_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\portalmini.png">ПАРНЫЕ ПОРТАЛЫ</h3>
      <p class="updateText">{{ text2 }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\lotus_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\lotusmini.png">ПРУДЫ ЛОТУСОВ</h3>
      <p class="updateText">{{ text3 }}</p>
    </div>

     <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\terz_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\tormentormini.png">ТЕРЗАТЕЛИ</h3>
      <p class="updateText">{{ text4 }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\smotr_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\watchermini.png">СМОТРИТЕЛИ</h3>
      <p class="updateText">{{ text5 }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\vrat_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\gatesmini.png">ЗАЩИТНЫЕ ВРАТА</h3>
      <p class="updateText">{{ text6 }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\mudrrune_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\wisdom_runesmini.png">РУНЫ МУДРОСТИ</h3>
      <p class="updateText">{{ text7 }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\shieldrune_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\shield_runesmini.png">РУНЫ ЩИТА</h3>
      <p class="updateText">{{ text8 }}</p>
    </div>

    <div style="overflow: auto; margin-bottom: 40px;">
      <img src="static\images\outpost_wide.gif" style="float: left; margin-right: 10px;">
      <h3> <img src="static\images\outpost_radiantmini.png">НОВЫЕ АВАНПОСТЫ</h3>
      <p class="updateText">{{ text9 }}</p>
    </div>

    <h2>Оставить отзыв:</h2> <!-- Блок отзывов с воодом данных имени, отзыва и номера телефона -->
    <form method="POST" action="/update">
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
        % for review in reviews:
            <li><strong>{{ review['nickname'] }}</strong>: {{ review['review'] }} </strong>: {{ review['timestamp'] }} )</li> <!-- Список всех отзывов -->
         % end
    </ul>




</div>
