# 🚇 Hyderabad Metro Route Helper

The **Hyderabad Metro Route Helper** is an interactive Python application built with **Gradio** that helps users determine the best travel route between metro stations in Hyderabad.  
By selecting a metro line, choosing a starting station, and setting a destination, the app provides **direct travel routes** or **interchange suggestions** when switching between lines is necessary.

---

## Features
- **Line Selection:** Choose from **Red**, **Blue**, or **Green** metro lines.
- **Dynamic Station Dropdown:** "From Station" updates automatically based on the selected line.
- **All Stations Destination List:** Destination dropdown includes stations from all lines without duplicates.
- **Route Suggestion Logic:** Provides direct travel or interchange station instructions based on your selection.
- **Interactive Web UI:** Built using Gradio for an easy-to-use browser interface.

---

## How It Works
1. **Select Metro Line** → Red, Blue, or Green.
2. **Choose Starting Station** → Dropdown updates dynamically.
3. **Select Destination Station** → Choose from all stations in the network.
4. **Click "Get Route"** → See whether you can travel directly or need to change at an interchange station.

---

## Tech Stack
- **Language:** Python  
- **Framework:** [Gradio](https://gradio.app/)  
- **Data Structure Choice:**  
  - **Lists** for ordered station data (preserves travel sequence).  
  - **Set** temporarily used to remove duplicates from the combined station list.  

---

## Example
**Input:**  
- Line: Red  
- From: Miyapur  
- To: Hitec City  

**Output:**  
```
You should change platform at Ameerpet to reach Hitec City from Miyapur.
```

---

## Future Improvements
- Add fare calculation based on distance.
- Include travel time estimation.
- Support real-time metro updates and delays.
- Display route maps visually.

---

## Installation & Usage

1. **Clone this repository:**
```bash
git clone https://github.com/your-username/hyderabad-metro-route-helper.git
```
2. **Navigate into the project folder:**
```bash
cd hyderabad-metro-route-helper
```
3. **Install required dependencies:**
```bash
pip install gradio
```
4. **Run the app:**
```bash
python app.py
```
5. **Open in Browser:**  
   The app will open automatically in your default browser.

---

## License
This project is licensed under the MIT License.
