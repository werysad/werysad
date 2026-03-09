using UnityEngine;

public class jumpcolor : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float jumpForce = 8f;

    private SpriteRenderer sr;
    private Rigidbody2D rb;
    private float moveX;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        sr = GetComponent<SpriteRenderer>();
    }

    void Update()
    {
        moveX = Input.GetAxis("Horizontal");

        // Horizontal movement
        rb.linearVelocity = new Vector2(moveX * moveSpeed, rb.linearVelocity.y);

        // Jump
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpForce);
        }

        // Change color based on state
        if (Mathf.Abs(rb.linearVelocity.y) > 0.1f)
        {
            sr.color = Color.blue;   // Jumping
        }
        else if (Mathf.Abs(moveX) > 0.1f)
        {
            sr.color = Color.red;    // Moving
        }
        else
        {
            sr.color = Color.white;  // Idle
        }
    }
}