using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.Collections;

public class ScriptManager2 : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created

    public void LoadScene()
    {
        SceneManager.LoadScene("img");
    }
}
