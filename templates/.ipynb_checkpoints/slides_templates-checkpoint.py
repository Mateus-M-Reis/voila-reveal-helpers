from ipywidgets import GridspecLayout, AppLayout, HTMLMath, Box, HBox, VBox

def return_slide_1(title, col_1):
	grid = GridspecLayout(7,2)
	grid[0,:] = HTMLMath(f"<h1>{title}</h1>")
	grid[1:,:] = col_1 if not type(col_1) == str else HTMLMath(f"{col_1}")
	return grid

def return_slide_11(title, col_1, col_2):
	grid = GridspecLayout(7,2)
	grid[0,:] = HTMLMath(f"<h1>{title}</h1>")
	grid[1:,0] = col_1 if not type(col_1) == str else HTMLMath(f"{col_1}")
	grid[1:,1] = col_2 if not type(col_2) == str else HTMLMath(f"{col_2}")
	return grid

def return_slide_22(title, col_1_up, col_1_down, col_2_up, col_2_down):
	grid = GridspecLayout(7,2)
	grid[0,:] = HTMLMath(f"<h1>{title}</h1>")
	grid[1:,0] = VBox([
		col_1_up if not type(col_1_up) == str else HTMLMath(f"{col_1_up}"),
		col_1_down if not type(col_1_down) == str else HTMLMath(f"{col_1_down}")
	], layout={'height':'50%'})
	grid[1:,1] = VBox([
		col_2_up if not type(col_2_up) == str else HTMLMath(f"{col_2_up}"),
		col_2_down if not type(col_2_down) == str else HTMLMath(f"{col_2_down}")
	], layout={'height':'50%'})
	return grid