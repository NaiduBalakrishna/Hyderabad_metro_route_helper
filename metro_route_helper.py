import gradio as gr

# Define station lists for each line with additional stations
red_line_stations = [
    "Miyapur", "JNTU College", "KPHB Colony", "Kukatpally", "Balanagar", "Moosapet",
    "Bharat Nagar", "Erragadda", "ESI Hospital", "S.R. Nagar", "Ameerpet", "Punjagutta",
    "Irrum Manzil", "Khairatabad", "Lakdi-ka-Pul", "Assembly", "Nampally", "Gandhi Bhavan",
    "Osmania Medical College", "MG Bus Station", "Malakpet", "New Market", "Musarambagh",
    "Dilsukhnagar", "Chaitanyapuri", "Victoria Memorial", "LB Nagar"
]

blue_line_stations = [
    "Nagole", "Uppal", "Survey of India", "Stadium", "NGRI", "Habsiguda", "Tarnaka",
    "Mettuguda", "Secunderabad East", "Parade Grounds", "Paradise", "Rasoolpura", "Prakash Nagar",
    "Begumpet", "Ameerpet", "Madhura Nagar", "Yusufguda", "Jubilee Hills Road No 5",
    "Jubilee Hills Check Post", "Peddamma Gudi", "Madhapur", "Durgam Cheruvu", "Hitec City", "Raidurg"
]

green_line_stations = [
    "JBS Parade Ground", "Secunderabad West", "Gandhi Hospital", "Musheerabad",
    "RTC Cross Roads", "Chikkadpally", "Narayanguda", "Sultan Bazaar", "MG Bus Station",
    "Salarjung Museum", "Charminar", "Shalibanda", "Shamsherganj", "Jungametta",
    "I.S. Sadan", "Falaknuma"
]


# Combined list for 'to_station'
all_stations = list(set(red_line_stations + blue_line_stations + green_line_stations))

# Route decision logic
def get_route(line, from_station, to_station):
    if from_station == to_station:
        return "You're already at your destination."

    if line == "Red":
        if to_station in red_line_stations:
            return f"You can travel directly from {from_station} to {to_station} on the Red Line."
        elif to_station in blue_line_stations:
            return f"You should change platform at Ameerpet to reach {to_station} from {from_station}."
        elif to_station in green_line_stations:
            return f"You should change platform at MGBS to reach {to_station} from {from_station}."
        else:
            return "Invalid destination station."

    elif line == "Blue":
        if to_station in blue_line_stations:
            return f"You can travel directly from {from_station} to {to_station} on the Blue Line."
        elif to_station in red_line_stations:
            return f"You should change platform at Ameerpet to reach {to_station} from {from_station}."
        elif to_station in green_line_stations:
            return f"You should change platform at JBS Parade Grounds to reach {to_station} from {from_station}."
        else:
            return "Invalid destination station."

    elif line == "Green":
        if to_station in green_line_stations:
            return f"You can travel directly from {from_station} to {to_station} on the Green Line."
        elif to_station in red_line_stations:
            return f"You should change platform at MGBS to reach {to_station} from {from_station}."
        elif to_station in blue_line_stations:
            return f"You should change platform at JBS Parade Grounds to reach {to_station} from {from_station}."
        else:
            return "Invalid destination station."

    return "Invalid selection."

# Function to update the from_station dropdown
def update_stations(line):
    if line == "Red":
        return gr.update(choices=red_line_stations, value=red_line_stations[0])
    elif line == "Blue":
        return gr.update(choices=blue_line_stations, value=blue_line_stations[0])
    elif line == "Green":
        return gr.update(choices=green_line_stations, value=green_line_stations[0])
    else:
        return gr.update(choices=[], value=None)

# Gradio UI
def launch_app():
    with gr.Blocks() as demo:
        gr.Markdown("## 🚇 Hyderabad Metro Route Helper")

        line_input = gr.Radio(["Red", "Blue", "Green"], label="Select Metro Line", value="Red")
        from_station = gr.Dropdown(choices=red_line_stations, label="From Station", value=red_line_stations[0])
        to_station = gr.Dropdown(choices=sorted(all_stations),label="To Station",value="Hitec City",allow_custom_value=True)  # 👈 this lets users type anything

        # Update 'from_station' when metro line changes
        line_input.change(fn=update_stations, inputs=[line_input], outputs=[from_station])

        submit_btn = gr.Button("Get Route")
        output = gr.Textbox(label="Route Suggestion")

        # Show result after clicking button
        submit_btn.click(fn=get_route, inputs=[line_input, from_station, to_station], outputs=output)

    demo.launch()

launch_app()
