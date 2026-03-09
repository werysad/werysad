using UnityEngine;


public class sliders : MonoBehaviour
{
    void Start()
    {
        // Start is called before the first frame update
    }


    // Called when slider value changes
    public void SliderValueChanged(float value)
    {
        Debug.Log("Slider Value Changed: " + value);
    }


    // Update is called once per frame
    void Update()
    {
    }
}
