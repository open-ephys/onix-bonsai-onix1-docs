# Style Guide

## General

Follow the style of our other docs sites.

## Hardware Guide

- Don't use moon button to trigger because it's used to toggle dark/light mode.
- Use standard names for saving files:
    - specify standard here
- All hardware guides should include loading scripts and ideally example data
- Unify workflows
    - Headstage workflows should contain a ConfigureBreakoutBoard node
    - Headstage workflows should contain a MemoryMonitor node

## Real World Visuals 

- Include visuals of real world actions wherever possible. 
- Click to play videos and gifs.
- No audio in videos.
- When doing screen records, include visual indicator of mouse clicks and keyboard presses.
    - Specify what those indicators look like and how they are done. jonnew likes screen2gif for this.

## File naming standard

- Use same abbreviation across files:
    - Headstage64: hs64
    - NeuropixelsHeadstage1Ve: np1e
    - NeuropixelsHeadstage2Ve: np2e
    - NeuropixelsHeadstage2VeBeta: np2ebeta
    - Neuropixels 1.0 probes: np1
    - Neuropixels 2.0 probes: np2
    - Neuropixels 2.0 Beta probes: np2beta
- 

## Maintaining screenshots

### Creating Edited Screenshots

There are webpages with edited screenshots of Bonsai. The source material (.xcf GIMP files) belongs in the img-src directory for ease of maintenance. The sections below describe how you can quickly create a new screenshot.

To take the screenshot (in Windows), use the `Windows+Shift+S` hotkey, select the `Window` option, and select the window you would like to screenshot. The preference is to take a screenshot against a grey background (e.g. create a (R: 127, G: 127, B: 127) background in GIMP) because some of the background makes it into the screenshot.

### Bonsai Package Manager Screenshot Edits

The layer group consisting of the highlight layer and 1,2,3,4 layers of the screenshots in the bonsai-install\*.xcf or bonsai-update\*.xcf files can be copy and pasted on top of other screenshots. This enables an expedited editing process for creating new edited screenshots. When creating the screenshot, do not change the size of the package manager after opening it.