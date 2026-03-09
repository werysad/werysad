using UnityEngine;
using UnityEngine.UI;


public class ToggleHandler : MonoBehaviour
{
    public Toggle toggle;


    void Start()
    {
        // Register listener
        toggle.onValueChanged.AddListener(UserValueChanged);
    }


    // Called when toggle value changes
    public void UserValueChanged(bool value)
    {
        Debug.Log("Toggle Value Changed: " + value);
    }
}
