from flask import Flask, request, render_template_string, send_file
import openai
import os

app = Flask(__name__)

# 将你的OpenAI API密钥替换到这里
openai.api_key = ""

# 简单的HTML表单模板
HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>Event Scheduler</title></head>
<body>
<h2>Schedule an Event</h2>
<form method="post">
  Event Name:<br>
  <input type="text" name="name" required><br>
  Description:<br>
  <input type="text" name="description" required><br>
  Duration (hours):<br>
  <input type="number" name="duration" min="1" max="12" required><br>
  Preferences (e.g., 'next Monday afternoon'):<br>
  <input type="text" name="preferences" required><br>
  <input type="submit" value="Schedule Event">
</form>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def schedule_event():
    if request.method == 'POST':
        # 获取表单数据
        event_name = request.form['name']
        description = request.form['description']
        duration = request.form['duration']
        preferences = request.form['preferences']

        # 调用OpenAI API获取事件时间建议
        prompt = f"Given an event with the following details, suggest a suitable time and date.\nEvent Name: {event_name}\nDescription: {description}\nDuration: {duration} hours\nPreferences: {preferences}\n\nSuggest a suitable date and time:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        suggested_time = response.choices[0].message['content']  # 更新这里以正确地获取建议的时间

        # 生成ICS文件内容
        ics_content = f"BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Your Company//Your App//EN\nBEGIN:VEVENT\nSUMMARY:{event_name}\nDESCRIPTION:{description}\nDTSTART:{suggested_time}\nDTEND:{suggested_time}\nEND:VEVENT\nEND:VCALENDAR"

        # 保存到临时文件
        file_path = "event.ics"
        with open(file_path, "w") as file:
            file.write(ics_content)
            print("Hi")


        return send_file(file_path, as_attachment=True, download_name='event.ics')

    # 显示表单
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True)


