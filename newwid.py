# pip install ipywidgets
#%%
import ipywidgets as widgets
from IPython.display import display

slider = widgets.IntSlider(
    value=10,min=0,max=100,step = 5,description="Age:"
)

display(slider)

num = widgets.FloatText(
    value=5.5,description="Marks:"
)

display(num)


toggle = widgets.ToggleButton(
    value=False,description='Dark/Light'
)
display(toggle)

drop = widgets.Dropdown(
    options = ["Python","Java","MERN"],
    description = "Select Course:"
)

display(drop)

pwd = widgets.Password(
    description = "Password:"
)

display(pwd)


name = widgets.Text(description="Name")
age=widgets.IntSlider(description="Age:")
drop = widgets.Dropdown(
    options = ["Python","Java","MERN"],
    description = "Course:"
)
btn = widgets.Button(description="Submit")


output = widgets.Output()

def on_submit(b):
    with output:
        output.clear_output()
        print("Name:",name.value )
        print("Age:",age.value )
        print("Course:",drop.value )


btn.on_click(on_submit)

form =widgets.VBox([name,age,drop,btn,output])

display(form)

# %%
