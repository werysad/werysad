using UnityEngine;
public class Rotation : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public float rotationSpeed =150f;
    void Update()
    {
        float rotateInput =Input.GetAxis("Horizontal");
        transform.Rotate(0,0,-rotateInput*rotationSpeed*Time.deltaTime);
    }
}
