using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using TMPro;

public class GetSender : MonoBehaviour
{
    [SerializeField] private string url;

    [SerializeField] private TextMeshProUGUI textArea;

    public void GetDataButton()
    {
        StartCoroutine(SendRequest());
    }

    private IEnumerator SendRequest()
    {
        UnityWebRequest request = UnityWebRequest.Get(this.url);

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.ConnectionError || request.result == UnityWebRequest.Result.ProtocolError)
            textArea.text = request.error;
        else
            textArea.text = request.downloadHandler.text;
    }
}