using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class button : MonoBehaviour
{
    public Button button1;


    void Start()
    {
        button1.onClick.AddListener(ButtonClicked);


    }
    public void ButtonClicked()
    {
        Debug.Log("Button Is Clicked!");
    }
}
