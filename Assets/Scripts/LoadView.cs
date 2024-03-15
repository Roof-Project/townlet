using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadView : MonoBehaviour
{
    private Animator panelAnim;

    private void Start()
    {
        panelAnim = GetComponent<Animator>();
    }

    public void Hide()
    {
        panelAnim.Play("hide");
    }

    public void Show()
    {
        panelAnim.Play("show");
    }
}
