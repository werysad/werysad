using UnityEngine;
using UnityEngine.AI;


public class AI_Player : MonoBehaviour
{
    public Transform target;
    public float speed = 3.5f;


    private NavMeshAgent agent;


    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        agent.speed = speed;
    }


    void Update()
    {
        if (target != null)
        {
            agent.SetDestination(target.position);
        }
    }
}
