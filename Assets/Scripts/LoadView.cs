using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadView : MonoBehaviour
{
    public void LoadMap()
    {
        SceneManager.LoadScene(1);
    }

    public void LoadCam()
    {
        SceneManager.LoadScene(0);
    }
}
