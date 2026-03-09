using UnityEngine;


public class Goal : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            Debug.Log("Player Wins!");
            Time.timeScale = 0;
        }
        else if (other.CompareTag("Enemy"))
        {
            Debug.Log("AI Wins!");
            Time.timeScale = 0;
        }
    }
}
