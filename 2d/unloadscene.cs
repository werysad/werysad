using UnityEngine;
using UnityEngine.SceneManagement;

public class ScriptManager1 : MonoBehaviour
{
    public void UnloadScene()
    {
        SceneManager.UnloadSceneAsync("img");
    }
}
