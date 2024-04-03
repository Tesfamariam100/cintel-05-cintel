from shiny import reactive, render
from shiny.express import ui
from faicons import icon_svg
import random
from datetime import datetime

# Define the update interval in seconds
UPDATE_INTERVAL_SECS = 1

# UI page options
ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# Sidebar
with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )
    ui.hr()
    ui.h6("Related Links:")
    ui.a(
        "View on GitHub",
        href="https://github.com/Tesfamariam100/cintel-05-cintel",
        target="_blank",
    )
    ui.a(
        "Live Demo",
        href="https://denisecase.github.io/cintel-05-cintel-basic/",
        target="_blank",
    )
    ui.a("Learn more about PyShiny", href="https://shiny.posit.co/py/", target="_blank")

# Main Section
ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("warmer than usual")
icon_svg("sun")

ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest reading and return a timestamp string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"

# Reactive calculation
@reactive.calc()
def reactive_calc_combined():
    """Generate fake temperature and timestamp data."""
    # Invalidate every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    # Generate random temperature between -20 and -10 degrees Celsius
    temperature = round(random.uniform(-20, -10), 1)
    # Get current timestamp
    current_timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # Create dictionary entry
    latest_data_entry = {"temp": temperature, "timestamp": current_timestamp}
    return latest_data_entry
