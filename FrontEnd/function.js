var currentSectionId = '';


function updateEndTimeOptions() {
    var startTime = document.getElementById('startTime').value;
    var endTime = document.getElementById('endTime');
    var timeOptions = ['6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm'];
    var startIndex = timeOptions.indexOf(startTime);

    // Clear existing options in endTime
    while (endTime.options.length > 0) {
        endTime.remove(0);
    }

    // Populate endTime with times after the selected startTime
    for (var i = startIndex + 1; i < timeOptions.length; i++) {
        var option = document.createElement('option');
        option.value = timeOptions[i];
        option.text = timeOptions[i];
        endTime.add(option);
    }
}

function showNext(nextSectionId) {
    currentSectionId = nextSectionId;
    hideAllSections();
    document.getElementById(nextSectionId).classList.remove('hidden');
    manageBackButtonVisibility(nextSectionId);
}

function showPrevious(previousSectionId) {
    hideAllSections();
    document.getElementById(previousSectionId).classList.remove('hidden');
    manageBackButtonVisibility(previousSectionId);
}

function hideAllSections() {
    var allSections = document.querySelectorAll('form > div');
    allSections.forEach(function(section) {
        section.classList.add('hidden');
    });
}

function manageBackButtonVisibility(currentSectionId) {
    var backButtons = document.querySelectorAll('.backBtn');
    backButtons.forEach(function(btn) {
        btn.classList.add('hidden');
    });
    if (currentSectionId !== 'studyDurationSection') {
        var currentSection = document.getElementById(currentSectionId);
        var backButton = currentSection.querySelector('.backBtn');
        if (backButton) {
            backButton.classList.remove('hidden');
        }
    }
}

function resetSubjectSection() {
    var subjectInputs = document.getElementById('subjectInputs');
    subjectInputs.innerHTML = '';
}


function addSubject() {
    var subjectIndex = document.querySelectorAll('.subject').length;
    var subjectDiv = document.createElement('div');
    subjectDiv.className = 'subject';
    subjectDiv.innerHTML = `
        <label>Subject Name:</label>
        <input type="text" name="subjectName[]"><br>
        <div class="tasks" id="tasks${subjectIndex}">
            <!-- Initial Task -->
            <div>
                <label>Task:</label>
                <input type="text" name="subjectTask${subjectIndex}[]"><br>
                <label>End Date for Task (optional):</label>
                <input type="date" name="subjectTaskEndDate${subjectIndex}[]"><br>
            </div>
        </div>
        <button type="button" onclick="addTask(${subjectIndex})">Add Task</button><br>`;
    document.getElementById('subjectInputs').appendChild(subjectDiv);
}

function addTask(subjectIndex) {
    var tasksDiv = document.getElementById('tasks' + subjectIndex);
    var taskDiv = document.createElement('div');
    taskDiv.innerHTML = `
        <label>Task:</label>
        <input type="text" name="subjectTask${subjectIndex}[]"><br>
        <label>End Date for Task (optional):</label>
        <input type="date" name="subjectTaskEndDate${subjectIndex}[]"><br>`;
    tasksDiv.appendChild(taskDiv);
}

document.getElementById('studyPlanForm').onsubmit = function(event) {
    event.preventDefault();
    alert('Form submitted. Implement AJAX or form submission logic here.');
};