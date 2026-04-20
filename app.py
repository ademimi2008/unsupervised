# -*- coding: utf-8 -*-
# ПРОСТОЕ ВЕБ-ПРИЛОЖЕНИЕ - С ГРАФИКОМ

from flask import Flask, render_template_string, request, send_file
import joblib
import os

# Создаём приложение
app = Flask(__name__)

# Загружаем модель
print("Загружаю модель...")
model = joblib.load('kmeans_model.pkl')
print("Модель загружена!")


# Маршрут для показа графика (картинки)
@app.route('/graphic')
def show_graphic():
    return send_file('clusters.png', mimetype='image/png')


# HTML код прямо здесь
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тест: Какой у тебя тип личности?</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }

        .question {
            margin-bottom: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 15px;
        }

        .question-text {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 15px;
        }

        .question-text small {
            font-size: 14px;
            color: #666;
            font-weight: normal;
        }

        .slider {
            width: 100%;
            margin: 10px 0;
        }

        .slider-labels {
            display: flex;
            justify-content: space-between;
            margin-top: 5px;
            color: #666;
            font-size: 12px;
        }

        .value-display {
            text-align: center;
            margin-top: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #667eea;
        }

        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 18px;
            cursor: pointer;
            transition: transform 0.3s;
            margin-top: 20px;
        }

        button:hover {
            transform: scale(1.02);
        }

        .info {
            margin-top: 20px;
            padding: 15px;
            background: #e3f2fd;
            border-radius: 10px;
            font-size: 14px;
            color: #1976d2;
            text-align: center;
        }

        .graphic-section {
            margin-top: 20px;
            padding: 15px;
            background: #f0f4ff;
            border-radius: 10px;
            text-align: center;
        }

        .graphic-section h3 {
            color: #333;
            margin-bottom: 15px;
        }

        .graphic-img {
            max-width: 100%;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.3s;
        }

        .graphic-img:hover {
            transform: scale(1.02);
        }

        .result-card {
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
        }

        .result-card.red {
            background: linear-gradient(135deg, #ff6b6b, #c92a2a);
        }

        .result-card.green {
            background: linear-gradient(135deg, #51cf66, #2f9e44);
        }

        .result-card.blue {
            background: linear-gradient(135deg, #4dabf7, #1c7ed6);
        }

        .emoji {
            font-size: 60px;
            margin-bottom: 10px;
        }

        .personality {
            font-size: 32px;
            font-weight: bold;
            color: white;
            margin-bottom: 20px;
        }

        .cluster {
            font-size: 18px;
            color: rgba(255,255,255,0.9);
            margin-bottom: 20px;
        }

        .description {
            text-align: left;
            background: rgba(255,255,255,0.2);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }

        .description p {
            margin: 10px 0;
            color: white;
            font-size: 16px;
        }

        .btn-restart {
            width: 100%;
            padding: 12px;
            background: #6c757d;
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.3s;
        }

        .btn-restart:hover {
            transform: scale(1.02);
        }

        input[type=range] {
            -webkit-appearance: none;
            background: #ddd;
            height: 5px;
            border-radius: 5px;
            outline: none;
        }

        input[type=range]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            background: #667eea;
            border-radius: 50%;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not show_result %}
        <!-- ФОРМА С ВОПРОСАМИ -->
        <h1>🧠 Какой у тебя тип личности?</h1>
        <div class="subtitle">Ответь на 3 вопроса честно (от 0 до 10)</div>

        <form method="POST">
            <!-- Вопрос 1 -->
            <div class="question">
                <div class="question-text">
                    1️⃣ Как сильно ты любишь общаться с людьми?
                    <br><small>0 - ненавижу, 10 - обожаю</small>
                </div>
                <input type="range" class="slider" name="social_energy" 
                       min="0" max="10" step="1" value="5" 
                       oninput="this.nextElementSibling.innerText = this.value">
                <div class="value-display">5</div>
                <div class="slider-labels">
                    <span>😠 Ненавижу</span>
                    <span>😐 Нормально</span>
                    <span>🥰 Обожаю</span>
                </div>
            </div>

            <!-- Вопрос 2 -->
            <div class="question">
                <div class="question-text">
                    2️⃣ Как часто ты хочешь побыть один/одна?
                    <br><small>0 - никогда, 10 - постоянно</small>
                </div>
                <input type="range" class="slider" name="alone_time" 
                       min="0" max="10" step="1" value="5"
                       oninput="this.nextElementSibling.innerText = this.value">
                <div class="value-display">5</div>
                <div class="slider-labels">
                    <span>👥 Никогда</span>
                    <span>😐 Иногда</span>
                    <span>🧘‍♂️ Постоянно</span>
                </div>
            </div>

            <!-- Вопрос 3 -->
            <div class="question">
                <div class="question-text">
                    3️⃣ Насколько ты разговорчив/разговорчива?
                    <br><small>0 - молчун, 10 - говорю без остановки</small>
                </div>
                <input type="range" class="slider" name="talkativeness" 
                       min="0" max="10" step="1" value="5"
                       oninput="this.nextElementSibling.innerText = this.value">
                <div class="value-display">5</div>
                <div class="slider-labels">
                    <span>🤐 Молчун</span>
                    <span>😐 Нормально</span>
                    <span>🗣️ Говорун</span>
                </div>
            </div>

            <button type="submit">🔮 Узнать результат</button>
        </form>

        <!-- БЛОК С ГРАФИКОМ -->
        <div class="graphic-section">
            <h3>📊 Как алгоритм разделил людей</h3>
            <img src="/graphic" alt="График кластеров" class="graphic-img" 
                 onclick="window.open('/graphic', '_blank')" 
                 title="Нажми, чтобы увеличить">
            <p style="font-size: 12px; color: #666; margin-top: 10px;">
                🔴 Красные - Интроверты &nbsp;|&nbsp;
                🟢 Зелёные - Амбиверты &nbsp;|&nbsp;
                🔵 Синие - Экстраверты<br>
                <small>(Нажми на картинку, чтобы увеличить)</small>
            </p>
        </div>

        <div class="info">
            💡 Передвигай ползунки, чтобы выбрать ответ.<br>
            Чем честнее ответишь, тем точнее результат!
        </div>

        {% else %}
        <!-- РЕЗУЛЬТАТ -->
        <div class="result-card {{ color }}">
            <div class="emoji">{{ emoji }}</div>
            <div class="personality">{{ personality }}</div>
            <div class="cluster">Кластер {{ cluster }}</div>

            <div class="description">
                <p>📖 Что это значит:</p>
                {% for item in description %}
                <p>• {{ item }}</p>
                {% endfor %}
            </div>
        </div>

        <!-- ТОЖЕ ПОКАЗЫВАЕМ ГРАФИК НА СТРАНИЦЕ РЕЗУЛЬТАТА -->
        <div class="graphic-section">
            <h3>📊 Как алгоритм разделил людей</h3>
            <img src="/graphic" alt="График кластеров" class="graphic-img" 
                 onclick="window.open('/graphic', '_blank')" 
                 title="Нажми, чтобы увеличить">
            <p style="font-size: 12px; color: #666; margin-top: 10px;">
                🔴 Красные - Интроверты &nbsp;|&nbsp;
                🟢 Зелёные - Амбиверты &nbsp;|&nbsp;
                🔵 Синие - Экстраверты
            </p>
        </div>

        <form method="GET" action="/">
            <button type="submit" class="btn-restart">🔄 Пройти ещё раз</button>
        </form>

        <div class="info">
            💡 Результат основан на трёх вопросах о твоём поведении<br>
            Модель обучена методом K-Means clustering
        </div>
        {% endif %}
    </div>

    <script>
        // Добавляем обработчики для всех ползунков
        var sliders = document.querySelectorAll('input[type=range]');
        sliders.forEach(function(slider) {
            slider.addEventListener('input', function() {
                this.nextElementSibling.innerText = this.value;
            });
        });
    </script>
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем ответы из формы
        social = float(request.form['social_energy'])
        alone = float(request.form['alone_time'])
        talk = float(request.form['talkativeness'])

        # Делаем предсказание
        user_data = [[social, alone, talk]]
        cluster = model.predict(user_data)[0]

        # Определяем тип личности
        if cluster == 0:
            personality = "ИНТРОВЕРТ"
            color = "red"
            emoji = "🔴"
            description = [
                "Ты не очень любишь шумные компании",
                "Тебе нужно время побыть одному/одной",
                "Ты больше слушаешь, чем говоришь",
                "У тебя мало, но очень близких друзей"
            ]
        elif cluster == 1:
            personality = "АМБИВЕРТ"
            color = "green"
            emoji = "🟢"
            description = [
                "Ты - золотая середина!",
                "Можешь быть душой компании, но и дома посидеть любишь",
                "Умеешь и говорить, и слушать",
                "Тебе комфортно в любой ситуации"
            ]
        else:
            personality = "ЭКСТРАВЕРТ"
            color = "blue"
            emoji = "🔵"
            description = [
                "Ты обожаешь быть в компании!",
                "Новые знакомства - твоё всё",
                "Ты очень разговорчив/разговорчива",
                "Одиночество тебя угнетает"
            ]

        # Показываем результат
        return render_template_string(HTML_TEMPLATE,
                                      show_result=True,
                                      personality=personality,
                                      color=color,
                                      emoji=emoji,
                                      description=description,
                                      cluster=cluster)

    # Показываем форму с вопросами
    return render_template_string(HTML_TEMPLATE, show_result=False)


# Запускаем приложение
if __name__ == '__main__':
    print("\n" + "=" * 40)
    print("ЗАПУСКАЮ ВЕБ-ПРИЛОЖЕНИЕ")
    print("=" * 40)
    print("Открой в браузере: http://127.0.0.1:5000")
    print("Нажми Ctrl+C чтобы остановить")
    print("=" * 40 + "\n")
    app.run(debug=True)