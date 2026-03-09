using UnityEngine;


public class GameManager : MonoBehaviour
{
    public GameObject player;
    public GameObject ai;
    public GameObject goal;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
   


    // Update is called once per frame
    void Update()
    {
        float playerDistance = Vector3.Distance(player.transform.position,goal.transform.position);
        float aiDistance = Vector3.Distance(ai.transform.position,goal.transform.position);
        if (playerDistance < 1.0f)
        {
            Debug.Log("Player Wins");
            QuitGame();
        }
        else if (aiDistance < 1.0f)
        {
            Debug.Log("AI Wins!");
            QuitGame();
        }
    }


    void QuitGame()
    {
        Application.Quit();
        UnityEditor.EditorApplication.isPlaying=false;
    }
}
