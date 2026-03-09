Practical 1
Q) Using If find number odd or even 
Code 
using UnityEngine;




public class p1 : MonoBehaviour
{
    void Start()
    {
        CheckOddEven(5); 
        CheckOddEven(10); 
    }
    void Update()
    {
        
    }


    void CheckOddEven(int num)
    {
        if (num % 2 == 0)
        {
            Debug.Log(num + " is even");
        }
        else
        {
            Debug.Log(num + " is odd");
        }
    }
}

Q2) Using Switch Case Calculate grade of a Student.
Code:
using UnityEngine;
public class p2 : MonoBehaviour
{
    void Start()
    {
        CalculateGrade(85); // Example: 85 is B
        CalculateGrade(92); // Example: 92 is A
    }
    void Update()
    { 
    }
    void CalculateGrade(int marks)
    {
        string grade;
        switch (marks / 10)
        {
            case 10:
            case 9:
                grade = "A";
                break;
            case 8:
                grade = "B";
                break;
            case 7:
                grade = "C";
                break;
            case 6:
                grade = "D";
                break;
            default:
                grade = "F";
                break;
        }
        Debug.Log("Marks: " + marks + " Grade: " + grade);
    }
}

Q3) Using for loop find sum of N number.
Code:
using UnityEngine;
public class p3 : MonoBehaviour
{
    void Start()
    {
        SumOfN(10); // Sum of first 10 numbers
    }
    void Update()
    {  
    }
    void SumOfN(int n)
    {
        int sum = 0;
        for (int i = 1; i <= n; i++)
        {
            sum += i;
        }
        Debug.Log("Sum of first " + n + " numbers: " + sum);
    }
}


Q4) Using While loop find Some of all Even Number in a Given Range.
Code:
using UnityEngine;




public class p4 : MonoBehaviour
{
    void Start()
    {
        SumEvenInRange(1, 10); // Sum of even numbers from 1 to 10
    }
    void Update()
    {  
    }
    void SumEvenInRange(int start, int end)
    {
        int sum = 0;
        int current = start;
        while (current <= end)
        {
            if (current % 2 == 0)
            {
                sum += current;
            }
            current++;
        }
        Debug.Log("Sum of even numbers from " + start + " to " + end + ": " + sum);
    }
}


Practical 2
AIM : Implement Physical Characteristics (Translation, Rotation, Scaling)

Create a 2d/3d project 
Add 2d/3d obj > add rigidbody2d > gravity = 0 
Add comp > script 
Edit > proj Setting > Player > other setting > active input handeling both

(This code is for 3D project for 2D uncomment the commented code and remove the rest ) 
Code: Translation 
using UnityEngine;




public class Transition : MonoBehaviour
{
    public float speed = 1f;
    // private Rigidbody rb;
    private Rigidbody2D rb2D;
    void Start()
    {
            // rb = GetComponent<Rigidbody>();
        rb2D = GetComponent<Rigidbody2D>();
    }
    void Update()
    {
        float moveX = Input.GetAxis("Horizontal");
        float moveZ = Input.GetAxis("Vertical");
       
       
        Vector2 movement2D = new Vector2(moveX, moveZ);
        rb2D.linearVelocity = movement2D * speed;
        // Vector3 movement = new Vector3(moveX, 0f, moveZ);
        // rb.linearVelocity = movement * speed;
    }
}





(Og code is 3D commented is 2D)
CODE : Scaling 
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





CODE : Rotation  (same code of 2d & 3d)
//Rotation
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






Practical 3


Aim: Implement Physics Characteristics (Jump) to an object and bind Surface Effector.
Create a 2D
ADD Obj > Triangle & Box 
Triangle > Rigid body 2d > box collider (use by effector on) > surface effect 
Platform > box collider (use by effector on) > surface effect 
To triangle > Now add comp > script 
Q)only jump
using UnityEngine;
public class Jump : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public float jumpforce = 4f;
    private Rigidbody2D rb;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpforce);
        }
    }
}




Q) Jump and Move
Code:
using UnityEngine;
public class jumpmove : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public float moveSpeed = 5f;
    public float jumpforce = 8f;
    private float moveX;
    private Rigidbody2D rb;
    void Start()
    {
          rb = GetComponent<Rigidbody2D>();
    }
    // Update is called once per frame
    void Update()
    {
        moveX = Input.GetAxis("Horizontal");
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpforce);
        }
    }
    void FixedUpdate()
    {
        rb.linearVelocity = new Vector2(moveX * moveSpeed, rb.linearVelocity.y);
    }
}


Q) Jump & Move & Colour Change.
Code:
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
        rb.linearVelocity = new Vector2(moveX * moveSpeed, rb.linearVelocity.y);




        if(Input.GetKeyDown(KeyCode.Space))
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpForce);
        }
        if (Mathf.Abs(rb.linearVelocity.y) > 0.1f)
        {
            sr.color = Color.blue;
        }
        else if(Mathf.Abs(moveX) > 0.1f)
        {
            sr.color = Color.red;
        }
        else
        {
            sr.color = Color.white;
        }




    }
}


Practical 4 
AIM : UI Components
1. Image -
2d project
upload your png image in assets
select image and change texture type in sprite
rigidbody 2D
Click on main camera in hierarchy > right click > UI > Image (a white box will appear on the scene)
Click on that white box (image)> go to source and select the your image(png) & give rigid body 2d
Add translation code for movement
using UnityEngine;
public class Sample : MonoBehaviour
{
    public float speed = 1f;
    private Rigidbody2D rb2d;


    void Start()
    {
        rb2d = GetComponent<Rigidbody2D>();
    }
    void Update()
    {
        float moveX = Input.GetAxis("Horizontal");
        float moveY = Input.GetAxis("Vertical");
        Vector2 movement = new Vector2(moveX, moveY);
        rb2d.linearVelocity = movement * speed;
    }
}


2. Button -
click on main camera < UI < legacy < button < Rename the button
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class button : MonoBehaviour
{
    public Button button1;


    void Start()
    {
        button1.onClick.AddListener(ButtonClicked);


    }
    public void ButtonClicked()
    {
        Debug.Log("Button Is Clicked!");
    }
}
Bind this script with the button and press + on the on click event () Drag and drop the button from (hierarchy) in the event and select the function from our code. Then run.


3. Toggle - 
click on main camera < UI < Toggle
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
Bind this script with the Toggle and press + on the on Value changed event () Drag and drop the toggle from (hierarchy) in the event and select the function from our code. Then run.




4. Slider
click on main camera < UI < Slider
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
Bind this script with the Slider and press + on the on Value changed event () Drag and drop the Slider from (hierarchy) in the event and select the function from our code. Then run.


5. Dropdown
click on main camera < UI < DropDown (TextMeshPro)
High chances of getting an text mesh pro error so to avoid this < Window tab < TextMeshPro < import TMP Essential Resources
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;


public class DropdownExample : MonoBehaviour
{
    [SerializeField] private TMP_Dropdown m_Dropdown;
    void Start()
    {
        // Optional: you can initialize or add listeners here
    }


    // Update is called once per frame
    public void GetDropDownValue()
    {
        int picked = m_Dropdown.value;
        string selectedOption = m_Dropdown.options[picked].text;
        Debug.Log(selectedOption);
    }
}
- Click on the Dropdown and go to the inspector panel < Scroll down <in the options fill in what all you want to be displayed in the Dropdown.
- Now Bind this script with the DropDown < and in the dropdown option select your dropdown, now press + on the on Value changed event () Drag and drop the Dropdown from (hierarchy) in the event and select the function from our code. Then run.


6. Input text field -
click on main camera < UI < legacy < Input Field
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class InputFieldExample : MonoBehaviour
{
    public InputField inputField;


    public void InputFieldValueChanged(string value)
    {
        Debug.Log("Input field value changed " + value);
    }
}
Bind this script with the inputfield and press + on the on Value changed event () Drag and drop the inputfield from (hierarchy) in the event and select the function from our code. Then run.


7. Text mesh pro
click on main camera < UI < TextMeshPro
using UnityEngine;
using TMPro;
public class Text : MonoBehaviour
{
    public TextMeshProUGUI output;
    public void HandleInput(int val)
    {
        if (val == 0)
        {
            output.text = "One Piece";
        }
        else if (val == 1)
        {
            output.text = "Demon Slayer";
        }
        else if (val == 2)
        {
            output.text = "Bleach";
        }
    }
}[a][b][c]
PRACTICAL 5 


AIM : Use of Effector 
Same Setup as Practical 3
Add 1 triangle with rigibody2d, boxcollider and surface effector & 1 Rectangle with boxcollider and any one effector from below as asked in question:
Bind the Jump & move script to the triangle.

Using Platform Effector
1. Add 1 Rectangle 
2. Add Box Collider and Platform Effector on the rectangle 
3. Enable Used by effector for Box Collider 2d 


Area Effector
4. Add 1 Rectangle 
5. Add Box Collider and Area Effector on the rectangle 
6. Enable Used by effector for Box Collider 2d 


Floating Effect
7. Add 1 Rectangle 
8. Add Box Collider and Buoyancy Effector on the rectangle 
9. Enable Used by effector for Box Collider 2d 
   1. Surface level 0.8
   2. Increase the Density if your object object doesn't float on top of the Rectangle


Q) Jump and Move
Code:
using UnityEngine;
public class jumpmove : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public float moveSpeed = 5f;
    public float jumpforce = 8f;
    private float moveX;
    private Rigidbody2D rb;
    void Start()
    {
          rb = GetComponent<Rigidbody2D>();
    }
    // Update is called once per frame
    void Update()
    {
        moveX = Input.GetAxis("Horizontal");
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpforce);
        }
    }
    void FixedUpdate()
    {
        rb.linearVelocity = new Vector2(moveX * moveSpeed, rb.linearVelocity.y);
    }
}


Practical 6
Scene Management in Unity
create an extra scene to use later
in the main scene add 4 Legacy button -> rename it LoadScene,LoadAdditive,LoadAsync,UnloadScene
click on each code and add component -> add script
click on click on all button drag & drop the button and select respective function
then run the game
code
LoadScene
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.Collections;


public class ScriptManager2 : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created


    public void LoadScene()
    {
        SceneManager.LoadScene("SampleScene");
    }
}
LoadAdditive
using UnityEngine;
using UnityEngine.SceneManagement;


public class scriptmanager1 : MonoBehaviour
{
    public void LoadSceneAdditive()
    {
        SceneManager.LoadScene("SampleScene", LoadSceneMode.Additive);
    }
}
LoadAsync
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;


public class ScriptManager : MonoBehaviour
{
    public void LoadSceneAsyncMethod()
    {
        StartCoroutine(LoadSceneAsync());
    }


    private IEnumerator LoadSceneAsync()
    {
        AsyncOperation operation = SceneManager.LoadSceneAsync("SampleScene");
        operation.allowSceneActivation = true;


        while (!operation.isDone)
        {
            yield return null;
        }
    }
}
UnloadScene
using UnityEngine;
using UnityEngine.SceneManagement;


public class ScriptManager1 : MonoBehaviour
{
    public void UnloadScene()
    {
        SceneManager.UnloadSceneAsync("SampleScene");
    }
}


Practical 7 - Audio 
create a 2D Project
go to google and download any audio -> drag and drop to the asset folder
right click on hierarchy -> main camera - > Audio-> Audio source & attach the script
Click on main camera > in inspector add component audio source > drag out audio in there
code
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




Unity Prac 8 - Find Range & degree for 3D
Range and Angle checking between two 3D objects


Game Obj-> 3D -> drop cube & sphere
click on sphere -> add comp -> script -> in the target box drag the cube from hierarchy
in the toggle click the move icon "+" and drag the sphere near the cube youll see the output in the console
Same for degree wala code
Code
Distance
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class RangeChecker : MonoBehaviour
{
    [SerializeField] Transform target;
    [SerializeField] float range = 5;
    private bool targetWasInRange = false;
    // Update is called once per frame
    void Update()
    {
        var distance = (target.position - transform.position).magnitude;
        if(distance <=range && targetWasInRange == false)
        {
            Debug.LogFormat("Target {0} entered range", target.name);
            targetWasInRange = true;
        }
        else if(distance > range && targetWasInRange == true)
        {
            Debug.LogFormat("Target {0} exited range", target.name);
            targetWasInRange = false;
        }
    }
}




Angle/Degree
using UnityEngine;
public class DegreeChecker : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    [SerializeField] Transform target;
    [SerializeField] float moveSpeed = 5f;
    // Update is called once per frame
    void Update()
    {
        var direction = target.position - transform.position;
        var directionToTarget = direction.normalized;
        var dotproduct = Vector3.Dot(transform.forward, directionToTarget);
        var angle = Mathf.Acos(dotproduct);
        Debug.LogFormat("Angle to target {0} is {1} degrees", target.name, angle * Mathf.Rad2Deg);
        float moveX = Input.GetAxis("Horizontal");
        float moveZ = Input.GetAxis("Vertical");
        Vector3 moveDirection = new Vector3(moveX, 0, moveZ);
        transform.Translate(moveDirection * moveSpeed * Time.deltaTime, Space.World);           
    }
}






Practical 9A 
Implement AI based game in Unity
create a 3D project


game obj - > 3D obj -> add plain
in the toggle click the box icon and spread the borders of plain obj


game obj - > 3D obj -> add 2 capsule
select capsule -> in inspector make scale 2 (for x,y,z)


game obj - > 3D obj -> cube
select cube -> in inspector make scale 10 (for x,y,z)


right click on asset and Create 4 material with different base map colour


drag & drop the material to the game obj to assign the colour


choose 1 capsule for player and 1 for AI
setting for player cap
in inspect - > assign tag player -> capsule collider (already there), add rigid body -> use gravity uncheck & constraint-> freeze Rotation check


for ai
in inspect - > assign add tag "Enemy" -> capsule collider (already there) -> - > tick "is trigger"
add rigid body
add nav mesh agent


now click the box (goal) inspector
in box collider -> tick "is trigger" -> assign add tag "Goal"


right click on hierarchy - > add 2 empty obj rename "nav mesh" , "gameManager"


click on nav mesh empty obj -> add comp -> add nav mesh surface -> click bake (it should blink blue)
on ball icon (gizmo)




click on player -> add comp -> add script
code
using UnityEngine;




public class PlayerScript : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
   
    public float speed = 5f;




    Rigidbody rb;
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }




    // Update is called once per frame
    void FixedUpdate()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");




        Vector3 movement = new Vector3(horizontal, 0, vertical) * speed;
        rb.linearVelocity = new Vector3(movement.x, rb.linearVelocity.y, movement.z);
    }
   
}


click on ai -> add compo -> script
drag & drop goal in target
code
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


click on goal-> add compo -> script
code
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


click on game manager -> script
drag & drop player enemy and goal in inspector
code
using UnityEngine;




public class GameManager : MonoBehaviour
{
    public GameObject player;
    public GameObject ai;
    public GameObject goal;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
   




    // Update is called once per frame
    void Update()
    {
        float playerDistance = Vector3.Distance(player.transform.position,goal.transform.position);
        float aiDistance = Vector3.Distance(ai.transform.position,goal.transform.position);
        if (playerDistance < 1.0f)
        {
            Debug.Log("Player Wins");
            QuitGame();
        }
        else if (aiDistance < 1.0f)
        {
            Debug.Log("AI Wins!");
            QuitGame();
        }
    }




    void QuitGame()
    {
        Application.Quit();
        UnityEditor.EditorApplication.isPlaying=false;
    }
}




to see the game in the camera mode
click the ball(gizmo) icon in the scene drag and adjust


 
run the game


Practical 9B 
Implement AI Player Chasing the User Player


Create game same as 9A
add  game objects plain, 2 capsule Enemy player
setting for player cap
in inspect - > assign tag player -> capsule collider (already there), add rigid body -> use gravity uncheck & container -> freeze Rotation check


for ai
in inspect - > assign add tag "Enemy" -> capsule collider (already there) -> - > tick "is trigger"
add rigid body
add nav mesh agent




add empty obj rename nav mesh
click on nav mesh empty obj -> add comp -> add nav mesh surface -> click bake (it should blink blue)
on ball icon (gizmo)




click on player -> add comp -> add script
code
using UnityEngine;




public class Player1 : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    public float speed = 5f;
    void Start()
    {
       
    }




    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        Vector3 movement = new Vector3(horizontal, 0f, vertical);
        transform.Translate(movement * speed * Time.deltaTime, Space.World);
    }
}


click on ai -> add compo -> script
drag & drop player in target
code
using UnityEngine;
using UnityEngine.AI; // Make sure this is included




public class AI_ChasePlayer : MonoBehaviour
{
    public Transform player;
    public float detectionRange = 10f;




    private NavMeshAgent agent;




    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
    }




    void Update()
    {
        if (Vector3.Distance(transform.position, player.position) <= detectionRange)
        {
            agent.SetDestination(player.position);
            Debug.Log("AI is Chasing the player!");




            float distanceToPlayer = Vector3.Distance(player.position, transform.position);
            Debug.Log("Distance to player: " + distanceToPlayer);




            if (distanceToPlayer < 0.5f)
            {
                Debug.Log("AI Caught The Player!");
                StopGame();
            }
        }
        else
        {
            agent.ResetPath();
        }
    }




    void StopGame()
    {
        Debug.Log("Game Paused - AI Caught The Player!");




        Application.Quit();




#if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
#endif
    }
}


Practical 10 
- Implement 3D Animation in Unity 
open mixamo website sign in
select character
chose animation beathing and download with skin
choose running & walking download without skin


create a 3D project
create a folder inside assets -> animations add all the items downloaded
grad & drop character in scene -> inspector rotation y=180
how to extract material -> click on the character -> inspector -> material -> extract (no use of this in prac)
now click the character -> inspector -> animation -> change name instead of "maxiamo" rename to animation name and tick loop time
right click in animation folder -> animation ->animation controller
double click on animation controller -> drag & drop all animation
right click on the animation -> make transition connect the sequent till exit
click on arrows and edit duration if needed


click on the character -> add comp -> animator -> in controller grad & drop controller
 


Practical 10B
select character
chose animation beathing and download with skin
choose running & walking download without skin


create a 3D project
create a folder inside assets -> animations add all the items downloaded
grad & drop character in scene -> inspector rotation y=180
now click the character -> insecptor -> animation -> change name instead of "maxiamo" rename to animation name and tick loop time
right click in animation folder -> animation ->animation controller
double click on animation controller -> drag & drop all animation


right click on the breath -> make transition connect to run
from run connect back to breath


right click on the breath -> make transition connect to walk
from walk connect back to breath


make parameters - add(bool) for animation2 & animation2
run and walk


click on arrow untick the "Has exit time" for all the arrow
and condition to all arrow
arrow going out from breath true
arrow going in from breath false


click on the character -> add comp -> animator -> in controller grad & drop controller


add component -> write script
code
using UnityEngine;




public class Animation_script : MonoBehaviour
{
    private Animator myanim;




    bool iswalking = false;
    bool isrunning = false;




    // Start is called before the first frame update
    void Start()
    {
        myanim = GetComponent<Animator>();
    }




    // Update is called once per frame
    void Update()
    {
        iswalking = Input.GetKey(KeyCode.W);
        myanim.SetBool("Walk", iswalking);
        //make sure the name of the bool in the
        // animator is the same as the one in the code




        isrunning = Input.GetKey(KeyCode.D);
        myanim.SetBool("Run", isrunning);
    }
}
[a]is wale me issue hai dk kya but implement karke dekh ek baar
[b]_Marked as resolved_
[c]_Re-opened_