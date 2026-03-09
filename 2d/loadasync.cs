using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class ScriptManager : MonoBehaviour
{
    public void LoadSceneAsyncMethod()
    {
        StartCoroutine(LoadSceneAsync());
    }

    private IEnumerator LoadSceneAsync()
    {
        AsyncOperation operation = SceneManager.LoadSceneAsync("img");
        operation.allowSceneActivation = true;

        while (!operation.isDone)
        {
            yield return null;
        }
    }
}
