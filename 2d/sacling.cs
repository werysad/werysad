using UnityEngine;

public class Scale : MonoBehaviour
{
    public float scaleSpeed = 1f;
    public float minScale = 0.2f;
    public float maxScale = 5f;

    void Update()
    {
        float scaleInput = Input.GetAxis("Vertical");

        Vector3 newScale = transform.localScale 
                           + Vector3.one * scaleInput * scaleSpeed * Time.deltaTime;

        newScale.x = Mathf.Clamp(newScale.x, minScale, maxScale);
        newScale.y = Mathf.Clamp(newScale.y, minScale, maxScale);
        newScale.z = 1f;

        transform.localScale = newScale;
    }
}