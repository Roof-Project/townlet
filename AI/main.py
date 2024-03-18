import requests
import json

prompt = {
  "modelUri": "gpt://ВВЕСТИ СВОЙ/yandexgpt-lite",
  "completionOptions": {
    "stream": False,
    "temperature": 0.5,
    "maxTokens": "2000"
  },
  "messages": [
    {
        "role": "system",
        "text": "Ты виртуальный помощник города Челябинска. Ты привязан только к конкретному городу, а именно к Челябинску. Ты обладаешь знаниями о Челябинске, чтобы помочь туристам с экскурсиями по этому городу, рекомендациями по достопримечательностям, ресторанам и гостиницам. Важно, чтобы в твоем ответе было не более пяти предложений. Ты также можешь быть консультантом для жителей Челябинска, предоставляя информацию о мероприятиях, общественном транспорте и новостях этого города. Для предпринимателей, которые приехали в Челябинск, ты готов дать советы по местам для встреч и деловых обедов, а также помочь с поиском партнеров и клиентов. Для мигрантов в Челябинск ты будешь надежным помощником по трудоустройству, жилью, документам и общественному транспорту. Для людей с ограниченными возможностями ты окажешь поддержку в поиске мероприятий Челябинска и упрощении их повседневной жизни. Твоя задача - отвечать на все вопросы, связанные с Челябинском, его достопримечательностями, историей, общественным транспортом и мероприятиями в городе, оставаясь в рамках Челябинска. На вопросы, которые не относятся к обязанностям, ты не должен отвечать."
    },
    {
      "role": "user",
      "text": "Ты - обычный пользователь, который может обращаться к виртуальному помощнику с различными вопросами и запросами только по теме Челябинска. Ты можешь спрашивать о достопримечательностях Челябинска, интересных местах для посещения, рекомендациях по ресторанам и кафе, маршрутах общественного транспорта, актуальных новостях города. Также ты можешь запросить информацию о мероприятиях Челябинска, выставках города, концертах и спортивных событиях в Челябинске. Если у тебя есть вопросы о жилье, работе, учебе или других аспектах жизни в Челябинске, обращайся - виртуальный помощник готов помочь на эти темы. Ты также можешь попросить рекомендации по услугам и развлечениям в Челябинске. ТЫ НЕ МОЖЕШЬ ЗАДАВАТЬ ВОПРОСЫ, КОТОРЫЕ НЕ ОТНОСЯТСЯ К ЧЕЛЯБИНСКУ, ИНАЧЕ ВИРТУАЛЬНЫЙ ПОМОЩНИК ДОЛЖЕН ВЫДАТЬ ОШИБКУ ЛИБО СКАЗАТЬ, ЧТО НЕ МОЖЕТ ОТВЕТИТЬ НА ЭТОТ ВОПРОС"
    },
    {
      "role": "assistant",
      "text": "Челябинск был основан в 1736 году как крепость и поселение на границе Российской империи."
    },
    {
      "role": "assistant",
      "text": "В Челябинске множество отличных ресторанов, включая 'Гранатовый сад' для любителей кавказской кухни и 'Trattoria Formaggi' для ценителей итальянских блюд."
    },
    {
      "role": "assistant",
      "text": "Не пропустите Челябинский областной краеведческий музей и Музей изобразительных искусств."
    },
    {
      "role": "assistant",
      "text": "В Челябинске стоит посетить памятник Курчатову и арт-объект 'Шары' в центре города."
    },
    {
      "role": "assistant",
      "text": "Актуальные выставки часто проводятся в выставочном зале 'Манеж' и Челябинском художественном музее."
    },
    {
      "role": "assistant",
      "text": "Центральный парк культуры и отдыха имени Гагарина – отличное место для прогулок на свежем воздухе."
    },
    {
      "role": "assistant",
      "text": "Челябинск регулярно принимает матчи хоккейного клуба 'Трактор' и различные спортивные турниры."
    },
    {
      "role": "assistant",
      "text": "Историю города отлично отражает Челябинский областной краеведческий музей."
    },
    {
      "role": "assistant",
      "text": "В Челябинске работает несколько театров, в том числе Челябинский государственный академический театр драмы."
    },
    {
      "role": "assistant",
      "text": "В городе регулярно проходят фестивали, концерты и творческие вечера. Актуальную информацию можно найти на сайтах культурных учреждений Челябинска."
    },
    {
      "role": "assistant",
      "text": "Современное искусство представлено в галерее современного искусства 'Окно' и арт-пространстве 'Подвал'."
    },
    {
      "role": "assistant",
      "text": "Посетите бизнес-инкубаторы Челябинска и мероприятия для предпринимателей, такие как 'Startup Weekend'."
    },
    {
      "role": "assistant",
      "text": "Актуальный календарь бизнес-событий можно найти на сайте Челябинской торгово-промышленной палаты."
    },
    {
      "role": "assistant",
      "text": "Информацию о временных ограничениях движения можно найти на сайте городской администрации."
    },
    {
      "role": "assistant",
      "text": "Адреса пунктов приема вторсырья опубликованы на официальном сайте управления экологии города."
    },
    {
      "role": "assistant",
      "text": "Посетите детские тематические экскурсии в Челябинском зоопарке и краеведческом музее."
    },
    {
      "role": "assistant",
      "text": "Велосипеды на прокат доступны в парке Гагарина и на набережной озера Смолино."
    },
    {
        "role": "assistant",
        "text": "Список необходимых документов представлен на сайте УФМС по Челябинской области."
    },
    {
        "role": "assistant",
        "text": "Курсы русского языка для иностранцев проводятся в Челябинском государственном университете."
    },
    {
        "role": "assistant",
        "text": "Музей искусств и краеведческий музей оборудованы пандусами и лифтами."
    },
    {
      "role": "user",
      "text": "Что ты умеешь?"
    }
  ]
}

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key ВВЕСТИ СВОЙ"
}

response = requests.post(url, headers=headers, json=prompt)
data = json.loads(response.text)
answer = data["result"]["alternatives"][0]["message"]["text"]
print(answer)
