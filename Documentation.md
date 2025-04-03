# 11 Software Engineering Task 1 Documentation

---

## Functional Requirements

---

### Data Retrieval

---

1. The user must be capable of obtaining the Astronomy Picture Of the Day and any related data including the title, date and explanation of what the picture is. They must be capable of retriving this data for any previous APOD dates.
2. It should be able of accessing NASA's photos of Earth.
(More would be done... but rate limits exist prohibiting use of a majority of the API's uses)

---

### User Interface

---

The user must be capable of interacting with the system via a tkinter GUI, with seperate tabs for each individual function of the program. They must be capable of viewing the generated images or data within the GUI, the GUI must also be capable of presenting Errors caused by user input or general API issues.

---

### Data Display

---

The user must be capable of retrieving the daily APOD of any date and the explanation of what it is from the system, the user must also be capable of opening the link to the APOD in the case they wish to save the image for personal use. The user should also be capable of retriving some of NASA's earth photos (high chance it'll fail due to the API's limitations) and opening a link to the image to save for personal use.

---
---

## Non-Functional Requirements

---

### Performance

---

The program should be able to access and load anything from the priorly mentioned sections of the NASA API in a matter of seconds (unless rate limited). It shouldn't require multiple attempts to access one piece of data (unless ratelimited).

---

### Reliability

---

The system must be consistently functional (unless rate-limited) explaining any possible issues that may have occured and it should always be capable of accessing the most recent daily APOD immediately and access any specific date if desired without issue.

---

### Usability and Accessibility

---

The system must be easily navigatable to the degree such that it is immediately clear what is required for the user to do and the definition of a valid input is immediately clear, it should also be obvious on how to access each tab of the GUI and what each button does.

---
---

## Functional Specifications

---
---

### User Requirements

---

The user must be capable of:

1. Accessing the daily APOD
2. Accesing the explanation of the daily APOD
3. Opening the image URL of the daily APOD from within the program
4. Doing 1-3 with the APOD of any previous dates
5. Access NASA's earth images service
6. Doing 3 but with the NASA earth images service

---

### Inputs and Outputs

---

The program will be capable of recieving the following inputs:

1. The date for the select APOD
2. The date for the NASA earth images service
3. The latitude for the NASA earth images service
4. The longtitude for the NASA earth images service
5. The dimensions (1 number) for the NASA earth images service

and the following outputs:

1. The daily APOD
2. The APOD of any previous date
3. The APOD explanation for any date
4. The NASA earth images
5. The image URLs for 1,2 and 4

---

### Core Features

---

The program must essetinally be capable of accessing the daily APOD (and its explanation) and the APOD and explanation of any previous date and load all of these within the GUI itself whilst also letting the user open the image link with the press of a button. The program must also be capable of accessing the NASA earth images service, load those images within a GUI and finally open the image URL with the press of a button.

---

### User interaction

---

The user will interact with the program via a tkinter GUI, using buttons and tkinter entry boxes and text boxes to allow the user to interact with the program, it must provide information such as the nessecary formatting for inputs to allow the user to enter in their input in a format that can be used.
