using UnityEngine;
using UnityEngine.SceneManagement;

public class scriptmanager1 : MonoBehaviour
{
    public void LoadSceneAdditive()
    {
        SceneManager.LoadScene("img", LoadSceneMode.Additive);
    }
}
