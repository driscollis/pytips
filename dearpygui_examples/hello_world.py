import dearpygui.dearpygui as dpg

def hello_callback():
    print("Hello from DPG")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world text")
    dpg.add_button(label="Hello button", callback=hello_callback)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()