<?php
// Обработка POST запросов
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $postData = $_POST;
    
    // Записываем данные в файл
    $file = fopen("data/post_data.txt", "a");
    fwrite($file, json_encode($postData) . PHP_EOL);
    fclose($file);
}

// Обработка GET запросов
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $getData = file_get_contents("data/post_data.txt");
    
    //Отправляем данные из файла как ответ на GET запрос
    echo $getData;
}
?>