<?php
// Устанавливаем кодировку UTF-8
header('Content-Type: text/html; charset=utf-8');
mb_internal_encoding("UTF-8");

// Обработка POST запросов
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $postData = $_POST;
    
    // Записываем данные в файл
    $file = fopen("data/post_data.txt", "a");
    fwrite($file, json_encode($postData, JSON_UNESCAPED_UNICODE) . PHP_EOL);
    fclose($file);
    
    // Преобразуем данные в JSON
    $data_json = json_encode($postData);
    
    // Отправляем текстовые данные на сервер с ИИ
    $url = 'http://188.225.85.124:80/';
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    // Получаем ответ от ИИ
    $response = curl_exec($ch);
    
    // Отправляем данные обратно в Unity APP
    echo $response;
    
    // Закрываем соединение
    curl_close($ch);
    
    // Записываем ответ от сервера в файл
    $file = fopen("data/response_data.txt", "a");
    fwrite($file, $response . PHP_EOL);
    fclose($file);
}

// Обработка GET запросов
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    
    // Отправляем данные из файла как ответ на GET запрос
    $input_file = fopen('data/response_data.txt', 'r');
    $lines = file('data/response_data.txt');
    $line = trim(end($lines));
    echo $line;
    fclose($input_file);
}
?>