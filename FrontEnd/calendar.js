document.addEventListener('DOMContentLoaded', function() {
    const icsFileUrl = 'test.ics'; // Update this path

    fetch(icsFileUrl)
        .then(response => response.text())
        .then(parseICSText)
        .then(displayEvents)
        .catch(console.error);

    function parseICSText(data) {
        // This is a very basic parser and might not work for all ICS files
        const events = [];
        const lines = data.split(/\r\n|\n|\r/);
        let currentEvent = {};

        lines.forEach(line => {
            if (line.startsWith('BEGIN:VEVENT')) {
                currentEvent = {};
            } else if (line.startsWith('END:VEVENT')) {
                events.push(currentEvent);
            } else {
                const [key, value] = line.split(':');
                currentEvent[key] = value;
            }
        });

        return events;
    }

    function displayEvents(events) {
        const container = document.getElementById('calendarEvents');

        events.forEach(event => {
            const eventDiv = document.createElement('div');
            eventDiv.className = 'event';
            eventDiv.innerHTML = `
                <h3>${event.SUMMARY}</h3>
                <p>Start: ${event.DTSTART}</p>
                <p>End: ${event.DTEND}</p>
                <p>Description: ${event.DESCRIPTION || 'N/A'}</p>
            `;
            container.appendChild(eventDiv);
        });
    }
});