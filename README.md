# Wallpaper Reminders
Automatic, customized reminders on your desktop daily. 


<br /> 

# Table of Contents
- [Overview](https://github.com/celenac/Wallpaper_Reminders#overview)
- [What is included](https://github.com/celenac/Wallpaper_Reminders#what-is-included)
- [How to download](https://github.com/celenac/Wallpaper_Reminders#how-to-download-wallpaper-reminders)
- [How to set up Wallpaper Reminders](https://github.com/celenac/Wallpaper_Reminders#setting-up-wallpaper-reminders)
- [How to customize the generated backgrounds](https://github.com/celenac/Wallpaper_Reminders#how-to-change-preferences)

<br />

# Overview

## What does Wallpaper Reminders do?
Wallpaper Reminders picks a note randomly from the your collection of notes. You can add or remove notes to and from the collection at any time. The notes can be used in any way that you want. They can be reminders, quotes, string patterns, etc.

Wallpaper Reminders then creates a simple random solid-colored desktop wallpaper displaying the note.
You can view samples of backgrounds in the **wallpapers** folder.

Schedule a frequency to run the application to have daily, weekly, or monthly reminders.

## How you use Wallpaper Reminders (the general flow)

1. Open My Reminders to edit, add, remove your collection of notes.
2. Run Wallpaper Reminders to genreate your wallpaper. 
3. Schedule the running of Wallpaper Reminders to get periodic wallpaper updates.

<br />

# What is included
## My Reminders
The My Reminders application file is where you add, edit, and remove the notes that will be randomly displayed on your background.
### Tips on using My Reminders:
- Click "Save" to save your changes!
- You cannot reedit your notes. To make changes to an existing note
    1. click on the note
    2. edit the note in the text line
    3. hit Enter (or click Add). A new note is now created.
    4. Delete the previous version of the note.
## Wallpaper Reminders
Running this application will generate a new wallpaper for the day.

<br />


# How to download Wallpaper Reminders
Download "application" folder in the "build" folder and save it somewhere on your computer.

<br />

# Setting up Wallpaper Reminders
For Windows, use **Task Scheduler**:

![](reference_images/Windows%20Task%20Scheduler%20Wallpaper%20Reminders.JPG)

1. Search "Task Scheduler" in the Windows Start menu

2. After opening Task Scheduler, click "Task Scheduler Library" on the leftmost panel  

3. Under "Actions" on the rightmost panel, click "Create Task..."

4. In the "General" tab, do the following:

    i. Select "Run whether user is logged on or not"
    
    ii. Select "Run with highest privileges"
    
    iii. At "Configure for", select the appropriate configuration for your system.
    
    ![](reference_images/Windows%20Task%20Scheduler%20General.JPG)
    
5. In the "Triggers" tab, do the following:

    i. Create a new trigger
    
    ii. Select "On a scedule" at "Begin the task" (or however you want the background to change)
    
    iii. Select "Daily" and edit the time of day you want your background to change automatically. 
    
    iv. In "Advanced settings," make sure "Enabled" is checked.
    
    ![](reference_images/Windows%20Task%20Scheduler%20Trigger%20edit.JPG)

6. In "Actions", do the following:

    i. Select "Start a program" for "Action"
       
    ii. Under "Settings" and "Program/script," browse for the Wallpaper Reminders.exe file you downloaded
    
    iii. Next to "Start in (optional)", paste the path of the Wallpaper Reminders.exe file (without quotes)
    
    ![](reference_images/Windows%20Task%20Scheduler%20Acitons%20edit.JPG)

7. In the "Conditions" tab, deselect ALL checkboxes to ensure that the application runs on schedule

8. In the "Settings" tab, do the following
    
    i. Check "Allow task to be run on demand"
    
    ii. Check "Run task as soon as possible after a scheduled start is missed"
    
    ![](reference_images/Windows%20Task%20Scheduler%20Settings.JPG)

9. Wallpaper Reminders is not set up to run every day on your Windows computer!

<br />

# How to change preferences
To change the appearance of the backgrounds generated, edit the "settings.txt" file. 
## Settings details:
- font size: size of the text on the background (in px)
- font: the name of the font file for the text. To change the font, add a copy of the font file to the /fonts folder and change the value of this field to the name of that file.  
- paragraph width: the width that the text spans on the background
- background color: the rgb ranges of the background color. Wallpaper Reminders will pick a random color within the ranges specified for RGB
- text color: the color of the text displayed on the background. The color must be either "white" or "black."
- text position: the x, y positions of the start of the text. ((0,0) is the top left corner of the background and x and y increase rightwards and downwrads, respecively).
