from ipywidgets import HTMLMath

def return_title_slide(title, text, color='red'):
	return HTMLMath(f"""
	<div style="height:100%; min-height:700px; width:100%; min-width:600px">
		<div style="
		height: 50%; 
		min-height: 450px; 
		background-color: {color}; 
		width: 85%; min-width: 700px; 
		display: flex; 
		align-items: center; 
		padding:20px
		">
			<h1 style="color:white; font-size: 40px">
				{title}
			</h1>
		</div>
		<div 
		style="display: flex; 
		justify-content: flex-end; 
		align-items: center; 
		min-height: 100px; 
		padding-right: 50px
		">
			<h4 style="
			font-size: 20px;
			">
				{text}
			</h4>
		</div>
	</div>
	""")

def return_index_slide(title, text, color='red'):
	return HTMLMath(f"""
	<div style="height:100%; min-height:700px; width:100%; min-width:600px">
		<div style="
		height: 20%; 
		min-height: 150px; 
		background-color: {color}; 
		width: 85%; min-width: 700px; 
		display: flex; 
		align-items: center; 
		padding:20px
		">
			<h1 style="color:white; font-size: 35px">
				{title}
			</h1>
		</div>
		<div 
		style="display: flex; 
		justify-content: flex-end; 
		align-items: center; 
		height: 50%;
		min-height: 400px; 
		padding-right: 50px;
		">
			{text}
		</div>
	</div>
	""")