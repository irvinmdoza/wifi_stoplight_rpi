from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)

led = LED(17)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/led/<action>")
def led_control(action):
    if action == "on":
        led.on()
    elif action == "off":
        led.off()
    return f"LED turned {action}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
