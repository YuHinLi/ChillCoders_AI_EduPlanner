events = [
    {
        "summary": "Meeting with Team",
        "location": "Office 101",
        "description": "Weekly team meeting",
        "start": "20240405T090000",
        "end": "20240405T100000",
    },
    {
        "summary": "Doctor's Appointment",
        "location": "City Hospital",
        "description": "Yearly check-up",
        "start": "20240406T110000",
        "end": "20240406T120000",
    }
]
# Start the ICS content
ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//ChatGPT//Calendar Event//EN\n"

# Loop through each event and add it to the ICS content
for event in events:
    ics_content += "BEGIN:VEVENT\n"
    ics_content += f"SUMMARY:{event['summary']}\n"
    ics_content += f"DTSTART:{event['start']}\n"
    ics_content += f"DTEND:{event['end']}\n"
    ics_content += f"DESCRIPTION:{event['description']}\n"
    ics_content += f"LOCATION:{event['location']}\n"
    ics_content += "END:VEVENT\n"

# End the ICS content
ics_content += "END:VCALENDAR"

# Save the ICS content to a file
file_path = "保存到ics的一个路径下"
with open(file_path, "w") as file:
    file.write(ics_content)

file_path