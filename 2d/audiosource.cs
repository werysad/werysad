using UnityEngine;

public class Audio : MonoBehaviour
{
    private AudioSource audioSource;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        // get the AudioSource component attached to this GameObject
        audioSource = GetComponent<AudioSource>();

        // check if the AudioSource is assigned
        if (audioSource == null)
        {
            Debug.LogError("AudioSource component not found");
            return;
        }

        audioSource.Stop();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.A))
        {
            audioSource.Play();
        }

        if (Input.GetKeyDown(KeyCode.D))
        {
            audioSource.Stop();
        }
    }
}
