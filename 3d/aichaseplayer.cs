using UnityEngine;
using UnityEngine.AI; // Make sure this is included


public class AI_ChasePlayer : MonoBehaviour
{
    public Transform player;
    public float detectionRange = 10f;


    private NavMeshAgent agent;


    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
    }


    void Update()
    {
        if (Vector3.Distance(transform.position, player.position) <= detectionRange)
        {
            agent.SetDestination(player.position);
            Debug.Log("AI is Chasing the player!");


            float distanceToPlayer = Vector3.Distance(player.position, transform.position);
            Debug.Log("Distance to player: " + distanceToPlayer);


            if (distanceToPlayer < 0.5f)
            {
                Debug.Log("AI Caught The Player!");
                StopGame();
            }
        }
        else
        {
            agent.ResetPath();
        }
    }


    void StopGame()
    {
        Debug.Log("Game Paused - AI Caught The Player!");


        Application.Quit();


#if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
#endif
    }
}
