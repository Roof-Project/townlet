using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using TMPro;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Net;
using Unity.VisualScripting;
using UnityEngine.UIElements;


class WeatherData
{
    public MainData main { get; set; }
    public WindData wind { get; set; }
    public WeatherDescription[] weather { get; set; }
}

class MainData
{
    public double temp { get; set; }
    public double feels_like { get; set; }
    public double temp_min { get; set; }
    public double temp_max { get; set; }
    public int pressure { get; set; }
    public int humidity { get; set; }
}

class WeatherDescription
{
    public string main { get; set; }
    public string description { get; set; }
}

class WindData
{
    public double speed { get; set; }
    public int deg { get; set; }
}

public class QAPair
    {
        public string request { get; set; }
        public string response { get; set; }
    }

public class PostSender : MonoBehaviour
{
    [SerializeField] private string url;
    private static string City = "Chelyabinsk";
    private string Pogurl = "https://api.openweathermap.org/data/2.5/weather?q="+City+"&appid=9ba0d269c5d5511613b307110089a55a";

    private string jsonFilePath = Path.Combine(Application.streamingAssetsPath, "q_amp_amp_a.json");

    [SerializeField] private TextMeshProUGUI textArea;
    [SerializeField] private TMP_InputField textField;

    public Dictionary<string, string> myDictionary = new Dictionary<string, string>();

    private void Start()
    {

        ServicePointManager.ServerCertificateValidationCallback = (a, b, c, d) => true;
        
        string jsonText = File.ReadAllText(jsonFilePath);

        var qaPairs = JsonConvert.DeserializeObject<List<QAPair>>(jsonText);

        foreach (var pair in qaPairs)
        {
            if (!myDictionary.ContainsKey(pair.request))
            {
                myDictionary.Add(pair.request, "");
                myDictionary[pair.request] = pair.response;
                textArea.text += "1";
            }
            textArea.text += "2";
        }
        textArea.text += "3";
    }

    public void SendQuestion(string question)
    {
        switch (question)
        {
            case "Что это за памятник?":
                textArea.text = "Памятник Курчатову — памятник знаменитому физику-ядерщику Игорю Васильевичу Курчатову был открыт в 1986 году к 250-летию Челябинска на вновь созданной площади Науки около здания Южно-Уральского государственного университета";
            break;
            case "Какие музеи стоит посетить в Челябинске?":
                textArea.text = "Не пропустите Челябинский областной краеведческий музей и Музей изобразительных искусств.";
            break;
            case "Какие памятники искусства есть в Челябинске?":
                textArea.text = "В Челябинске стоит посетить памятник Курчатову и арт-объект 'Шары' в центре города.";
            break;
            case "Где в Челябинске проводятся интересные выставки?":
                textArea.text = "Актуальные выставки часто проводятся в выставочном зале 'Манеж' и Челябинском художественном музее.";
            break;
            case "Какие есть зеленые зоны для прогулок в Челябинске?":
                textArea.text = "Центральный парк культуры и отдыха имени Гагарина – отличное место для прогулок на свежем воздухе.";
            break;
        }
        
    }

    public void SendData() => StartCoroutine(SendRequest());

    public void Pogoda() => StartCoroutine(SendPogoda());

    private IEnumerator SendPogoda()
    {

        UnityWebRequest request = UnityWebRequest.Get(this.Pogurl);

        yield return request.SendWebRequest();

        WeatherData weatherData = JsonConvert.DeserializeObject<WeatherData>(request.downloadHandler.text);

        textArea.text = $"Температура: { Math.Round(weatherData.main.temp - 273.15, 0)} градус";
        
    }

    private IEnumerator SendRequest()
    {

        WWWForm form = new WWWForm();
        form.AddField("text", textField.text);

        using (UnityWebRequest www = UnityWebRequest.Post(url, form))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("Error: " + www.error);
            }
            else
            {
                Debug.Log("Post request sent successfully");
            }

            textArea.text = www.downloadHandler.text;
            print(www.downloadHandler.text);

        }
    }
}