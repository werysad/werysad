//Scaling
using UnityEngine;




public class Scaling : MonoBehaviour
{
    public float scaleSpeed = 1f;
    public float minScale = 0.2f;
    public float maxScale = 5f;
    void Update()
    {
       
        float scaleInput = Input.GetAxis("Vertical");
        Vector3 newScale = transform.localScale + Vector3.one * scaleInput * scaleSpeed * Time.deltaTime;
        newScale.x = Mathf.Clamp(newScale.x, minScale, maxScale);
        newScale.y = Mathf.Clamp(newScale.y, minScale, maxScale);
        newScale.z = 1;


        transform.localScale = newScale;
       
        // //3d Method
        // float scaleInput = Input.GetAxis("Vertical");
        // float currentScale = transform.localScale.x;
        // float newScale = currentScale + scaleInput * scaleSpeed * Time.deltaTime;
        // newScale = Mathf.Clamp(newScale, minScale, maxScale);
        // transform.localScale = new Vector3(newScale, newScale, newScale);


    }
}
