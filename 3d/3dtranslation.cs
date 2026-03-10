using UnityEngine;




public class Transition : MonoBehaviour
{
    public float speed = 1f;
    private Rigidbody rb;
    // private Rigidbody2D rb2D;
    void Start()
    {
            rb = GetComponent<Rigidbody>();
        // rb2D = GetComponent<Rigidbody2D>();
    }
    void Update()
    {
        float moveX = Input.GetAxis("Horizontal");
        float moveZ = Input.GetAxis("Vertical");
       
       
        // Vector2 movement2D = new Vector2(moveX, moveZ);
        // rb2D.linearVelocity = movement2D * speed;
        Vector3 movement = new Vector3(moveX, 0f, moveZ);
        rb.linearVelocity = movement * speed;
    }
}
