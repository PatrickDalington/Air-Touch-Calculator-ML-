# Air Touch Calculator
Air Touch Calculator is an innovative machine-learning computer vision application that turns your computer into a touchless calculator. Using a webcam and hand gestures, the app allows you to perform calculations without physically touching the device. The application leverages the OpenCV library for real-time hand detection and gesture recognition.

![](https://i.imgur.com/YyRmNNs.png)

* LinkedIn Page: https://www.linkedin.com/in/patrick-olumba/



## Table of Content
* [Installation](#Setup-and-Installation)
* [How it Works](#How-It-Works)
* [Calculating Logic](#Calculating-Logic)
* [Technologies Used](#Technologies-Used)
* [Using the Calculator](#Using-the-Calculator)
* [Contribution](#contribution)
* [Usage](#usage)
* [Related Project](#related-project)
* [Authors](#authors)
* [License](#license)


## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Air-Touch-Calculator.git
   cd Air-Touch-Calculator
   
2. **Make sure you have Python installed. Then, install the required packages using pip:**

    ```bash
    pip install opencv-python cvzone gTTS playsound

3. **Execute the following command in your terminal:**

    ```bash
   python app.py
   




## How It Works

1. **Hand Detection:** The app uses OpenCV and the `cvzone` Hand Tracking Module to detect hand movements in real-time via the computer's webcam. The hand's landmarks are identified and used to interpret touch gestures.

2. **User Interface:** A virtual calculator is displayed on the screen, with buttons drawn using OpenCV. The layout includes digits, arithmetic operators, and control buttons such as "C" for clear and "=" for calculation.

3. **Gesture Recognition:** The app tracks the distance between specific landmarks on the hand to determine when a button is "pressed." If the distance is less than a threshold, it registers a touch input.

4. **Text-to-Speech (TTS):** Although currently commented out, the app includes a TTS feature using the `gTTS` library. This can read out the numbers and results when enabled.

![](https://i.imgur.com/RcMzkob.png)


## Calculating Logic:
* The app supports basic arithmetic operations: addition, subtraction, multiplication, and division.
* It ensures valid equations by checking for improper endings before evaluating the expression.
* A simple interface displays the current input and result.




## Technologies Used

- **OpenCV:** For computer vision tasks such as capturing webcam input and drawing UI elements.
- **cvzone HandTrackingModule:** Simplifies hand detection and tracking.
- **gTTS and playsound:** Libraries used for text-to-speech functionality.



## Using the Calculator

- Ensure your webcam is properly connected.
- The calculator interface will appear on the screen.
- Use your index and middle fingers to simulate button presses.
- Perform calculations using gestures without touching your device.



## Contribution
`This project is a solo project. Feel free to contribute ☕️`


## License
All Right Reserved © 2024


## Authors
Patrick Olumba - [Github](https://github.com/PatrickDalington) / [LinkedIn](https://www.linkedin.com/in/patrick-olumba)  

